import os

from django import template
from django.db import models

register = template.Library()


@register.filter
def repr(value):
    return value.__repr__()


@register.filter
def fval(value: models.FileField):
    print("Recebi, ", repr(value), type(value))
    return value.name


@register.filter
def filename(value):
    print("Recebi, ", repr(value), type(value))
    return os.path.basename(value.file.name)
