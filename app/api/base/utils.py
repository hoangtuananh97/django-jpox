import datetime
import os

from api.base import EnumConst


def format_date_now(format_date=None):
    try:
        if not format_date:
            format_date = EnumConst.DATE_FORMAT
        return datetime.date.today().strftime(format_date)
    except ValueError:
        raise


def format_datetime_now(format_datetime=None):
    try:
        if not format_datetime:
            format_datetime = EnumConst.DATETIME_FORMAT
        return datetime.datetime.now().strftime(format_datetime)
    except ValueError:
        raise


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
