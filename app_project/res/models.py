import os
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from app_project.base.models import BaseModel


def upload_country_image(instance, filename):
    path = 'countries/'
    ext = filename.split('.')[-1]
    name = '%s.%s' % (uuid4().hex, ext)
    return os.path.join(path, name)


class Country(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    code = models.CharField(max_length=2, verbose_name=_("Code"),
                            help_text="The ISO country code in two chars. \nYou can use this field for quick search.")
    image = models.ImageField(upload_to=upload_country_image, verbose_name=_("Image"))
