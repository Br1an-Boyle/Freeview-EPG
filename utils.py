import pytz
import re
import unicodedata
from datetime import datetime, timedelta, time, timezone
import math

bt_dt_format = '%Y-%m-%dT%H:%M:%SZ'
tz = pytz.timezone('Europe/London')


# From https://stackoverflow.com/questions/4324790/removing-control-characters-from-a-string-in-python
def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


# From spatialtime/iso8601_duration.py
def parse_duration(iso_duration):
    """Parses an ISO 8601 duration string into a datetime.timedelta instance.
    Args:
        iso_duration: an ISO 8601 duration string.
    Returns:
        a datetime.timedelta instance
    """
    m = re.match(r'^P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:.\d+)?)S)?$',
                 iso_duration)
    if m is None:
        raise ValueError("invalid ISO 8601 duration string")

    days = 0
    hours = 0
    minutes = 0
    seconds = 0.0

    # Years and months are not being utilized here, as there is not enough
    # information provided to determine which year and which month.
    # Python's time_delta class stores durations as days, seconds and
    # microseconds internally, and therefore we'd have to
    # convert parsed years and months to specific number of days.

    if m[3]:
        days = int(m[3])
    if m[4]:
        hours = int(m[4])
    if m[5]:
        minutes = int(m[5])
    if m[6]:
        seconds = float(m[6])

    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

def get_days(src: str, days_to_grab: int) -> list:
    """
Generate appropriate list of dates for the required API
    :param src: The EPG source required
    :param days_to_grab: Number of days of data to grab
    :return: List of dates in required formats
    """
    dates = []

    if src == "sky":
        now = int(datetime.timestamp(datetime.now() - timedelta(hours=1)))
        for idx in range(1, days_to_grab):
            dates.append(int(datetime.timestamp(datetime.combine(datetime.now(), time(0, 0)) + timedelta(idx))))

    elif src == "bt":
        now = datetime.now() - timedelta(hours=1)
        for idx in range(1, days_to_grab + 1):
            dates.append((datetime.combine(datetime.now(), time(0, 0)) + timedelta(idx)))

    elif src == "freeview":
        now = math.trunc(datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
        for idx in range(1, days_to_grab + 1):
            dates.append(math.trunc((datetime.now(timezone.utc).replace(hour=0, minute=0, second=0,
                                                                        microsecond=0) + timedelta(idx)).timestamp()))

    dates.insert(0, now)
    return dates

