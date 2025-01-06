# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    organization = models.CharField(max_length=255, null=True, blank=True)
    inspection_count = models.IntegerField(null=True, blank=True)
    last_inspection = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sidewalk Inspection(models.Model):

    #__Sidewalk Inspection_FIELDS__
    file name = models.CharField(max_length=255, null=True, blank=True)
    path = models.CharField(max_length=255, null=True, blank=True)
    deficiency = models.CharField(max_length=255, null=True, blank=True)
    number_of_deficiency = models.IntegerField(null=True, blank=True)
    number_of_deficiency_above_5mm = models.IntegerField(null=True, blank=True)
    number_of_deficiency_above_20mm = models.IntegerField(null=True, blank=True)
    list_of_measurements = models.TextField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    altitude = models.CharField(max_length=255, null=True, blank=True)
    severity = models.CharField(max_length=255, null=True, blank=True)
    inspection_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    inspector = models.CharField(max_length=255, null=True, blank=True)

    #__Sidewalk Inspection_FIELDS__END

    class Meta:
        verbose_name        = _("Sidewalk Inspection")
        verbose_name_plural = _("Sidewalk Inspection")



#__MODELS__END
