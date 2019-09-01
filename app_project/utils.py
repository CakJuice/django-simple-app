import os
from datetime import date
from uuid import uuid4


def get_upload_path(instance, filename):
    """ Upload path should be year/month/uuid_filename.ext """
    today = date.today()
    path = '%d/%02d/' % (today.year, today.month,)
    ext = filename.split('.')[-1]
    name = '%s.%s' % (uuid4().hex, ext)
    return os.path.join(path, name)
