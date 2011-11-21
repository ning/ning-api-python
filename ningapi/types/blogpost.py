from ningapi.types.contentbase import ContentBase
from ningapi.util import timezone


class BlogPost(ContentBase):

    field_map = {
        "id": "id",
        "author": "author",
        "createdDate": ("created_date", timezone.to_datetime),
        "publishTime": ("publish_date", timezone.to_datetime),
        "publishStatus": "publish_status",
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
    ]

    recent_endpoint = "BlogPost/recent"
    count_endpoint = "BlogPost/count"

    def __init__(self, **kwargs):
        super(BlogPost, self).__init__(**kwargs)
