# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Count

# Create your models here.


class Photo_Group(models.Model):
    id = models.TextField(null=False, blank=False, primary_key=True)
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.id

    @property
    def total_photos(self):
        return self.photos.aggregate(total=Count('id'))['total']


class Photo(models.Model):
    gid = models.ForeignKey(Photo_Group, related_name='photos')
    id = models.TextField(null=False, blank=False, primary_key=True)
    url = models.TextField(null=False)

    def __str__(self):
        return str(self.gid)
