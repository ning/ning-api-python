from ningapi.types.contentbase import ContentBase
from ningapi.util import timezone


class Activity(ContentBase):

    field_map = {
        "id": "id",
        "author": "author",
        "type": "type",
        "createdDate": ("created_date", timezone.to_datetime),
        "contentId": "content_id",
        "url": "url",
        "title": "title",
        "description": "description",
        "attachedTo": "attached_to",
        "attachedToType": "attached_to_type",
        "attachedToAuthor": "attached_to_author",
        "image": "image",
    }

    sub_resources = [
        "author.fullName",
        "author.iconUrl",
        "author.url",
        "image.url",
        "image.width",
        "image.height",
    ]

    recent_endpoint = "Activity/recent"
    count_endpoint = "Activity/count"

    def __init__(self, **kwargs):
        super(Activity, self).__init__(**kwargs)
