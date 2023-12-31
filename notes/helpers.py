import re
import datetime
from django.utils import timezone
import shutil


def camel_snake_case(camel_case_string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()


def convert_time_from_usec_to_timezoned_utc(usec_time):
    timestamp_in_seconds = usec_time / 1000000
    utc_time = datetime.datetime.utcfromtimestamp(timestamp_in_seconds)
    timezoned_utc_time = timezone.make_aware(utc_time, timezone.get_current_timezone())
    return timezoned_utc_time


def copy_file(source, destination):
    shutil.copyfile(source, destination)
    


