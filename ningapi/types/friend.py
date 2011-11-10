from ningapi.types.contentbase import ContentBase
from ningapi.util import timezone


class Friend(ContentBase):

    field_map = {
        "author": "author",
        "friend": "friend",
        "state": "state",
        "createdDate": ("created_date", timezone.to_datetime),
        "updatedDate": ("updated_date", timezone.to_datetime),
    }

    admin_field_map = {
    }

    sub_resources = [
        "author.fullName",
        "author.iconUrl",
        "author.url",
    ]

    recent_endpoint = "Friend/recent"
    alpha_endpoint = "Friend/alpha"
    count_endpoint = "Friend/count"

    def __init__(self, **kwargs):
        super(Friend, self).__init__(**kwargs)
