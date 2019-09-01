import os
from datetime import date
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from app_project.base.models import BaseModel


class Country(BaseModel):
    def upload_country_image(self, filename):
        """ Upload country image path. """
        today = date.today()
        path = '%d/%02d/' % (today.year, today.month)
        ext = filename.split('.')[-1]
        name = '%s.%s' % (uuid4().hex, ext)
        return os.path.join(path, name)

    name = models.CharField(max_length=128, verbose_name=_("Name"))
    code = models.CharField(max_length=2, verbose_name=_("Code"), unique=True,
                            help_text="The ISO country code in two chars. \nYou can use this field for quick search.")
    image = models.ImageField(upload_to=upload_country_image, verbose_name=_("Image"))
