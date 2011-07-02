from ningapi.types.contentbase import ContentBase


class Token(ContentBase):

    field_map = {
        "oauthToken": "oauth_token",
        "oauthTokenSecret": "oauth_token_secret",
        "oauthConsumerKey": "oauth_consumer_key",
        "author": "author",
    }

    def __init__(self, **kwargs):
        super(Token, self).__init__(**kwargs)
