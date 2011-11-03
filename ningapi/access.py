from ningapi.types import BlogPost, Photo, User, Network, Friend


class BaseAccessor(object):

    DEFAULT_PAGE_SIZE = 50

    def __init__(self, ning_api):
        self.ning_api = ning_api

    def base_lister(self, cls, endpoint):
        """Generate a lister for the given class"""

        def lister(count, fields=None):
            if not fields:
                fields = cls.get_field_names()

            attrs = {
                "fields": ",".join(fields),
                "count": self.DEFAULT_PAGE_SIZE,
            }
            total = 0

            while True:

                content = self.ning_api.get(endpoint, attrs)
                attrs["anchor"] = content["anchor"]

                for entry in content["entry"]:
                    total += 1
                    if total > count:
                        raise StopIteration
                    yield cls.from_json_dict(entry)

                if content["lastPage"]:
                    raise StopIteration

        return lister


class BlogPostAccessor(BaseAccessor):

    def __init__(self, ning_api):
        super(BlogPostAccessor, self).__init__(ning_api)

        self.list_recent = super(BlogPostAccessor, self).base_lister(
                BlogPost, BlogPost.recent_endpoint)


class PhotoAccessor(BaseAccessor):

    def __init__(self, ning_api):
        super(PhotoAccessor, self).__init__(ning_api)

        self.list_recent = super(PhotoAccessor, self).base_lister(
                Photo, Photo.recent_endpoint)


class NetworkAccessor(BaseAccessor):

    def __init__(self, ning_api):
        super(NetworkAccessor, self).__init__(ning_api)

        self.list_alpha = super(NetworkAccessor, self).base_lister(
                Network, Network.alpha_endpoint)


class UserAccessor(BaseAccessor):

    # User endpoint is a bit slower, so request fewer items per request
    DEFAULT_PAGE_SIZE = 20

    def __init__(self, ning_api):
        super(UserAccessor, self).__init__(ning_api)

        self.list_alpha = super(UserAccessor, self).base_lister(
                User, User.alpha_endpoint)

        self.list_recent = super(UserAccessor, self).base_lister(
                User, User.recent_endpoint)


class FriendAccessor(BaseAccessor):

    def __init__(self, ning_api):
        super(FriendAccessor, self).__init__(ning_api)

        self.list_recent = super(FriendAccessor, self).base_lister(
                Friend, Friend.recent_endpoint)
