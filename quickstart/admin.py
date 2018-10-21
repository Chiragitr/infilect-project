# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Photo_Group, Photo
from django.contrib import admin

# Register your models here.
admin.site.register(Photo_Group)
admin.site.register(Photo)