from django.db import models
from django.utils.translation import gettext_lazy as _

from app_project.base.models import BaseModel
from app_project.utils import get_upload_path


class Country(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    code = models.CharField(max_length=2, verbose_name=_("Code"), unique=True,
                            help_text="The ISO country code in two chars. \nYou can use this field for quick search.")
    image = models.ImageField(upload_to=get_upload_path, verbose_name=_("Image"))
