# Ning XAPI OAuth library
# Copyright (C) 2010 Ning, Inc.
#
# Depends on python-oauth2 -- http://github.com/simplegeo/python-oauth2

import binascii
import multipart
import oauth2 as oauth
import urllib

try:
    import json
except ImportError:
    import simplejson as json


class NingError(Exception):

    def __init__(self, status, reason, error_code=None, error_subcode=None,
        trace=None):
        self.status = status
        self.reason = reason
        self.error_code = error_code
        self.error_subcode = error_subcode
        self.trace = trace

    def __str__(self):
        if self.error_code and self.error_subcode:
            return "%s (%d) %d-%d" % (self.reason, self.status,
                self.error_code, self.error_subcode)
        else:
            return "%s (%d)" % (self.reason, self.status)


class Client(object):
    
    SECURE_PROTOCOL = "https://"
    INSECURE_PROTOCOL = "http://"

    def __init__(self, host, network, consumer, token=None, screenName=None):

        self.host = host
        self.network = network
        self.consumer = consumer
        self.token = token
        self.screenName = screenName
        self.method = oauth.SignatureMethod_HMAC_SHA1()

    def call(self, url, method="GET", body=None, token=None, headers=None,
        secure=False):
        
        if self.method.name == 'PLAINTEXT':
            secure = True
        
        if secure:
            protocol = self.SECURE_PROTOCOL
        else:
            protocol = self.INSECURE_PROTOCOL

        url = '%s%s/xn/rest/%s/1.0/%s' % (protocol, self.host, self.network, url)
        self.client = oauth.Client(self.consumer, token)
        if self.method is not None:
            self.client.set_signature_method(self.method)

        resp, content = self.client.request(url, method, headers=headers,
            body=body)
        if int(resp['status']) != 200:
            try:
                result = json.loads(content)
                if result:
                    raise NingError(result['status'], result['reason'],
                        result['code'], result['subcode'], result['trace'])
                else:
                    raise NingError(int(resp['status']),
                        "HTTP response %s and %s" % (resp, content))
            except ValueError:
                raise NingError(int(resp['status']),
                    "HTTP response %s and %s" % (resp, content))

        return json.loads(content)

    def post(self, path, body):
        if 'file' in body:
            mp = multipart.Multipart()
            mp.attach(multipart.FilePart({'name': 'file'}, body['file'],
                body['content_type']))
            for k, v in body.items():
                if k != 'file' and k != 'content_type':
                    mp.attach(multipart.Part({'name': k}, v))
            return self.call("Photo", method="POST", token=self.token,
                headers={'Content-Type': mp.header()[1]}, body=str(mp))

        elif 'bin' in body:
            mp = multipart.Multipart()
            mp.attach(multipart.Part({'name': 'file', 'filename': 'file'},
                body['bin'], body['content_type']))

            for k, v in body.items():
                if k != 'bin' and k != 'content_type':
                    mp.attach(multipart.Part({'name': k}, v))
            return self.call("Photo", method="POST", token=self.token,
                headers={'Content-Type': mp.header()[1]}, body=str(mp))

        else:
            return self.call(path, method="POST", token=self.token,
                body=urllib.urlencode(body))

    def put(self, path, body):
        return self.call(path, method="PUT", token=self.token,
            body=urllib.urlencode(body))

    def delete(self, path, attrs=None):
        if attrs is not None:
            path += ('&' if path.find("?") != -1 else '?') + \
                urllib.urlencode(attrs)
        return self.call(path, method="DELETE", token=self.token)

    def get(self, path, attrs=None):
        if attrs is not None:
            path += ('&' if path.find("?") != -1 else '?') + \
                urllib.urlencode(attrs)
        return self.call(path, token=self.token)

    def login(self, login, password):
        info = self.call("Token", method="POST", headers={
            'Authorization': 'Basic %s' %
                binascii.b2a_base64('%s:%s' % (login, password)),
            }, secure=True)

        self.screenName = info['entry']['author']
        self.token = oauth.Token(key=info['entry']['oauthToken'],
            secret=info['entry']['oauthTokenSecret'])
        return self.token
