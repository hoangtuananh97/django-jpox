import time

from api.base import EnumConst
from api.base.utils import get_filename_ext, format_date_now


def upload_avatar_path(instance, filename):
    path = "images/avatar"
    date_today = format_date_now(format_date=EnumConst.DATE_UPLOAD_FORMAT)
    new_filename = time.time()
    name, ext = get_filename_ext(filename)
    return f"{path}/{date_today}/{new_filename}{ext}"
