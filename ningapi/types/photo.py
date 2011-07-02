from ningapi.types.contentbase import ContentBase


class Photo(ContentBase):

    field_map = {
        "id": "id",
        "author": "author",
        "createdDate": "created_date",
        "updatedDate": "updated_date",
        "title": "title",
        "description": "description",
        "visibility": "visibility",
        "approved": "approved",
        "commentCount": "comment_count",
        "url": "url",
        "tags": "tags",
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
