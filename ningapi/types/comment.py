from ningapi.types.contentbase import ContentBase


class Photo(ContentBase):

    field_map = {
        "id": "id",
        "author": "author",
        "createdDate": "created_date",
        "updatedDate": "updated_date",
        "description": "description",
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
