from django.db import models
from django.core.exceptions import ValidationError


def validate_min(value):
    if value < 0:
        raise ValidationError('Value must be at least 0')


def validate_max(value):
    if value > 100:
        raise ValidationError('Value must be at most 100')


class Thing(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30,
        blank=False
    )
    description = models.CharField(
        unique=False,
        blank=True,
        max_length=120
    )
    quantity = models.IntegerField(
        validators=([validate_min, validate_max])
    )