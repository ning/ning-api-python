from ningapi.types.contentbase import ContentBase
from ningapi.util import timezone


class Photo(ContentBase):

    field_map = {
        "id": "id",
        "author": "author",
        "createdDate": ("created_date", timezone.to_datetime),
        "updatedDate": ("updated_date", timezone.to_datetime),
        "title": "title",
        "description": "description",
        "visibility": "visibility",
        "approved": "approved",
        "commentCount": "comment_count",
        "url": "url",
        "topTags": "top_tags",
    }

    sub_resources = [
        "author.fullName",
        "author.iconUrl",
        "author.url",
        "image.url",
        "image.width",
        "image.height",
    ]

    recent_endpoint = "Photo/recent"
    count_endpoint = "Photo/count"

    def __init__(self, **kwargs):
        super(Photo, self).__init__(**kwargs)
