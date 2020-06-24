from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Contact(models.Model):

    name=models.CharField(_(""), max_length=50)
    email=models.CharField(_(""), max_length=50)
    phone=models.CharField(_(""), max_length=50)
    desc=models.TextField(_(""))
    date=models.DateField(_(""), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name