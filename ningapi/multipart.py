# -*- encoding: utf-8 -*-

'''Module for encoding data as form-data/multipart'''

'''
Copyright (c) 2007 by the respective coders, see
http://www.stuvel.eu/projects/flickrapi

This code is subject to the Python licence, as can be read on
http://www.python.org/download/releases/2.5.2/license/

For those without an internet connection, here is a summary. When this
summary clashes with the Python licence, the latter will be applied.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import os
import base64

class Part(object):
    '''A single part of the multipart data.
    
    >>> Part({'name': 'headline'}, 'Nice Photo')
    ... # doctest: +ELLIPSIS
    <flickrapi.multipart.Part object at 0x...>

    >>> image = open('tests/photo.jpg')
    >>> Part({'name': 'photo', 'filename': image}, image.read(), 'image/jpeg')
    ... # doctest: +ELLIPSIS
    <flickrapi.multipart.Part object at 0x...>
    '''
    
    def __init__(self, parameters, payload, content_type=None):
        self.content_type = content_type
        self.parameters = parameters
        self.payload = payload

    def render(self):
        '''Renders this part -> List of Strings'''
        
        parameters = ['%s="%s"' % (k, v)
                      for k, v in self.parameters.iteritems()]
        
        lines = ['Content-Disposition: form-data; %s' % '; '.join(parameters)]
        
        if self.content_type:
            lines.append("Content-Type: %s" % self.content_type)
        
        lines.append('')
        
        if isinstance(self.payload, unicode):
            lines.append(self.payload.encode('utf-8'))
        else:
            lines.append(self.payload)
        
        return lines

class FilePart(Part):
    '''A single part with a file as the payload
    
    This example has the same semantics as the second Part example:

    >>> FilePart({'name': 'photo'}, 'tests/photo.jpg', 'image/jpeg')
    ... #doctest: +ELLIPSIS
    <flickrapi.multipart.FilePart object at 0x...>
    '''
    
    def __init__(self, parameters, filename, content_type):
        parameters['filename'] = filename
        
        imagefile = open(filename, 'rb')
        payload = imagefile.read()
        imagefile.close()

        Part.__init__(self, parameters, payload, content_type)

def boundary():
    """Generate a random boundary, a bit like Python 2.5's uuid module."""

    bytes = os.urandom(16)
    return base64.b64encode(bytes, 'ab').strip('=')
   
class Multipart(object):
    '''Container for multipart data'''
    
    def __init__(self):
        '''Creates a new Multipart.'''
        
        self.parts = []
        self.content_type = 'form-data/multipart'
        self.boundary = boundary()
        
    def attach(self, part):
        '''Attaches a part'''
        
        self.parts.append(part)
    
    def __str__(self):
        '''Renders the Multipart'''

        lines = []
        for part in self.parts:
            lines += ['--' + self.boundary]
            lines += part.render()
        lines += ['--' + self.boundary + "--"]
        
        return '\r\n'.join(lines)
    
    def header(self):
        '''Returns the top-level HTTP header of this multipart'''
        
        return ("Content-Type",
                "multipart/form-data; boundary=%s" % self.boundary)
