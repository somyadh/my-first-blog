# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import People, Myself, Books

# Register your models here.
admin.site.register(People)
admin.site.register(Books)
admin.site.register(Myself)