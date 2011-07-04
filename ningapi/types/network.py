from ningapi.types.contentbase import ContentBase
from ningapi.util import timezone


class Network(ContentBase):

    field_map = {
        "id": "id",
        "author": "author",
        "createdDate": ("created_date", timezone.to_datetime),
        "subdomain": "subdomain",
        "name": "name",
        "iconUrl": "icon_url",
        "defaultUserIconUrl": "default_url_icon_url",
        "blogPostModeration": "blog_post_moderation",
        "userModeration": "user_moderation",
        "photoModeration": "photo_moderation",
        "eventModeration": "event_moderation",
        "groupModeration": "group_moderation",
        "videoModeration": "video_moderation",
        'xapiStatus': 'api_status'
    }

    sub_resources = [
        "author.fullName",
        "author.iconUrl",
        "author.url",
    ]

    alpha_endpoint = "Network/alpha"

    def __init__(self, **kwargs):
        super(Network, self).__init__(**kwargs)
