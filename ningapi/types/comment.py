from ningapi.types.contentbase import ContentBase
from ningapi.util import timezone


class Photo(ContentBase):

    field_map = {
        "id": "id",
        "author": "author",
        "createdDate": ("created_date", timezone.to_datetime),
        "updatedDate": ("updated_date", timezone.to_datetime),
        "description": ("description", timezone.to_datetime),
        "attachedTo": "attached_to",
        "attachedToType": "attached_to_type",
        "attachedToAuthor": "attached_to_author",
        "approved": "approved",
    }

    sub_resources = [
        "author.fullName",
        "author.iconUrl",
        "author.url",
    ]

    recent_endpoint = "Photo/recent"
    count_endpoint = "Photo/count"

    def __init__(self, **kwargs):
        super(Photo, self).__init__(**kwargs)
