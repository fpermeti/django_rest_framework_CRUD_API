from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Create your models here.


def min_max_range(value):
    if value < 0 and value > 1000000:
        raise ValidationError(gettext_lazy(
            '%(value)s is out of range(legal range is between 0 and 1000000)'), params={'value': value})


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=50)
    author = models.CharField(null=False, blank=False, max_length=50)
    price = models.FloatField(null=False, blank=False,
                              validators=[min_max_range])
