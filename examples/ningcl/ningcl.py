from optparse import OptionParser
import json
import ConfigParser
import oauth2 as oauth

import ningapi


class NingToken(object):

    def create(self, client, options, args):
        email = args.pop(0)
        password = args.pop(0)

        content = client.login(email, password)
        print(content)

    def dump(self, content):
        print json.dumps(content, sort_keys=True, indent=4)


class NingResource(object):

    def list(self, client, options, args, params={}):
        sort = "recent"

        if options.count:
            params['count'] = options.count
        if options.fields:
            params['fields'] = options.fields
        if options.approved is not None:
            params["approved"] = repr(options.approved).lower()

        if options.sort:
            sort = options.sort

        path = "%s/%s" % (self.resource_type, sort)

        content = client.get(path, params)
        self.dump(content)

    def get(self, client, options, args):
        # TODO: support multiple GET parameters

        params = {}

        if options.fields:
            params['fields'] = options.fields

        try:
            params["id"] = args.pop(0)
        except IndexError:
            pass

        content = client.get(self.resource_type, params)
        self.dump(content)

    def create(self, client, options, args):
        raise NotImplementedError

    def update(self, client, options, args):
        raise NotImplementedError

    def delete(self, client, options, args):
        raise NotImplementedError

    def dump(self, content):
        print json.dumps(content, sort_keys=True, indent=4)


class NingWriteResource(NingResource):

    def create(self, client, options, args, resource_fields={}):

        if options.title:
            resource_fields["title"] = options.title
        if options.description:
            resource_fields["description"] = options.description

        # If we have an extra argument, assume it's a file to upload
        if len(args) == 1:
            resource_fields["file"] = args.pop(0)

        content = client.post(self.resource_type, resource_fields)
        self.dump(content)

    def update(self, client, options, args, resource_fields={}):
        resource_fields["id"] = args.pop(0)

        if options.title:
            resource_fields["title"] = options.title
        if options.description:
            resource_fields["description"] = options.description
        if options.approved is not None:
            resource_fields["approved"] = repr(options.approved).lower()

        content = client.put(self.resource_type, resource_fields)
        self.dump(content)

    def delete(self, client, options, args, resource_fields={}):
        params = {"id": args.pop(0)}
        content = client.delete(self.resource_type, params)
        self.dump(content)


class NingPhoto(NingWriteResource):
    resource_type = "Photo"


class NingBlogPost(NingWriteResource):
    resource_type = "BlogPost"


class NingActivity(NingWriteResource):
    resource_type = "Activity"

    def create(self, client, options, args, resource_fields={}):
        raise NotImplementedError

    def update(self, client, options, args, resource_fields={}):
        raise NotImplementedError


class NingUser(NingResource):
    resource_type = "User"

    def update(self, client, options, args, resource_fields={}):
        """
        Update the member's status message
        """

        try:
            resource_fields["id"] = args.pop(0)
        except IndexError:
            pass

        if options.description:
            resource_fields["statusMessage"] = options.description
        if options.approved is not None:
            resource_fields["approved"] = options.approved
        if options.blocked is not None:
            resource_fields["isBlocked"] = options.blocked

        content = client.put(self.resource_type, resource_fields)
        self.dump(content)

    def delete(self, client, options, args, resource_fields={}):
        params = {"id": args.pop(0)}
        content = client.delete(self.resource_type, params)
        self.dump(content)


class NingVideo(NingResource):
    resource_type = "Video"

class NingTopic(NingResource):
    resource_type = "Topic"


class NingComment(NingWriteResource):
    resource_type = "Comment"

    def list(self, client, options, args):
        """
        List the comments attached to a specific content ID
        """

        params = {}
        try:
            params["attachedTo"] = args.pop(0)
        except IndexError:
            print "Missing the content ID, unable to attach comment"
            return

        return super(NingComment, self).list(client, options, args,
                params)

    def create(self, client, options, args):
        """
        Create a new comment attached to the specified content ID
        """

        resource_fields = {}
        try:
            resource_fields["attachedTo"] = args.pop(0)
        except IndexError:
            print "Missing the content ID, unable to attach comment"
            return

        return super(NingComment, self).create(client, options, args,
                resource_fields)


class NingNetwork(NingResource):
    resource_type = "Network"

    def list(self, client, options, args):
        options.sort = "alpha"
        return super(NingNetwork, self).list(client, options, args)


service_directory = {
        "activity": NingActivity(),
        "blog": NingBlogPost(),
        "comment": NingComment(),
        "network": NingNetwork(),
        "photo": NingPhoto(),
        "token": NingToken(),
        "user": NingUser(),
        "video": NingVideo(),
        "forum": NingTopic(),
        }


def setup_optparse():
    parser = OptionParser()

    parser.add_option(
            "-t",
            "--title",
            action="store",
            dest="title",
            help="Item title")

    parser.add_option(
            "-d",
            "--description",
            action="store",
            dest="description",
            help="Item description")

    parser.add_option(
            "-s",
            "--sort",
            action="store",
            dest="sort",
            help="Sort order")

    parser.add_option(
            "-i",
            "--visibility",
            action="store",
            dest="visibility",
            help="Visibility")

    parser.add_option(
            "-c",
            "--count",
            action="store",
            dest="count",
            type="int",
            help="Number of items to return")

    parser.add_option(
            "-f",
            "--fields",
            action="store",
            dest="fields",
            help="List of fields to return")

    parser.add_option(
            "-n",
            "--network",
            action="store",
            dest="subdomain",
            help="Ning Network to access")

    parser.add_option(
            "-e",
            "--email",
            action="store",
            dest="email",
            help="Email address of the member")

    parser.add_option(
            "-a",
            "--approve",
            action="store_true",
            dest="approved",
            help="Set the item's 'approved' field is set to true or filter out rejected items")

    parser.add_option(
            "-r",
            "--reject",
            action="store_false",
            dest="approved",
            help="Set the item's 'approved' field is set to false or filter out accepted items")

    parser.add_option(
            "-b",
            "--block",
            action="store_true",
            dest="blocked",
            help="Set the item's 'isBlocked' field is set to true or filter out blocked items")

    parser.add_option(
            "-u",
            "--unblock",
            action="store_false",
            dest="blocked",
            help="Set the item's 'isBlocked' field is set to false or filter out un-blocked items")

    return parser


def main():

    parser = setup_optparse()
    (options, args) = parser.parse_args()


    config = ConfigParser.ConfigParser()
    config.read("config.cfg")

    if options.subdomain:
        subdomain = options.subdomain
    else:
        subdomain = config.get("DEFAULTS", "network")

    if options.email:
        email = options.email
    else:
        email = config.get("DEFAULTS", "email")

    config_header = "%s:%s" % (subdomain, email)


    try:
        consumer_key = config.get(subdomain, "consumer_key")
        consumer_secret = config.get(subdomain, "consumer_secret")
    except ConfigParser.NoSectionError:
        try:
            print "Unable to find a key for this network, using the default"
            consumer_key = config.get("DEFAULTS", "consumer_key")
            consumer_secret = config.get("DEFAULTS", "consumer_secret")
        except ConfigParser.NoOptionError:
            print "No consumer key found, unable to continue"
            return

    consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

    try:
        access_key = config.get(config_header, "access_key")
        access_secret =config.get(config_header, "access_secret")
        token = oauth.Token(key=access_key, secret=access_secret)
    except ConfigParser.NoSectionError:
        print "Couldn't find a token, going without it"
        token = None


    host = "external.ningapis.com"
    client = ningapi.Client(host, subdomain, consumer, token)

    try:
        resource_name = args.pop(0)
    except IndexError:
        # TODO: Output list of available resources
        print "Missing resource name"
        return

    try:
        action_name = args.pop(0)
    except IndexError:
        # TODO: Output list of available options
        print "Missing action name"
        return

    resource = service_directory.get(resource_name, None)
    if not resource:
        print "Invalid resource name: %s" % resource_name
        return

    action = getattr(resource, action_name, None)
    if not action:
        print "Invalid action for %s: %s" % (action_name, resource_name)
        return

    try:
        action(client, options, args)
    except ningapi.NingError, e:
        print "Ning Error: %s" % str(e)


if __name__ == "__main__":
    main()
