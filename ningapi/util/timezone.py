from datetime import tzinfo, timedelta, datetime


class UTC(tzinfo):
    """UTC timezone"""

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return timedelta(0)

utc_tzinfo = UTC()

iso_8601_format = "%Y-%m-%dT%H:%M:%S.%fZ"


def to_datetime(date_str):
    return datetime.strptime(date_str, iso_8601_format).replace(tzinfo=utc_tzinfo)
