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

    recent_endpoint = "Friend/recent"

    def __init__(self, **kwargs):
        super(Friend, self).__init__(**kwargs)
