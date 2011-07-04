from ningapi.types.contentbase import ContentBase
from ningapi.util import timezone


class User(ContentBase):

    field_map = {
        "id": "id",
        "author": "author",
        "createdDate": ("created_date", timezone.to_datetime),
        "updatedDate": ("updated_date", timezone.to_datetime),
        "approved": "approved",
        "visibility": "visibility",
        "url": "url",
        "fullName": "full_name",
        "iconUrl": "icon_url",
        "birthdate": "birthdate",
        "commentCount": "comment_count",
        "gender": "gender",
        "location": "location",
        "isOwner": "is_owner",
        "isAdmin": "is_admin",
        "isMember": "is_member",
        "isBlocked": "is_blocked",
        "state": "state",
        "statusMessage": "status_message",
    }

    admin_field_map = {
        "profileQuestions": "profile_questions",
        "email": "email",
    }

    sub_resources = [
        "author.fullName",
        "author.iconUrl",
        "author.url",
    ]

    recent_endpoint = "User/recent"
    alpha_endpoint = "User/alpha"
    count_endpoint = "User/count"

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
