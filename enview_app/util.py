import datetime
import uuid


def get_uuid() -> str:
    return str(uuid.uuid4())


def get_time_object(timestamp) -> datetime:
    time_str = timestamp[0:-3] + timestamp[-2:]
    datetime_obj = datetime.datetime.strptime(
        time_str, '%Y-%m-%dT%H:%M:%S%z')
    return datetime_obj
