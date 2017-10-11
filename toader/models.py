# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from random import randint
from django.db.models import Count
# Create your models here.

class Books(models.Model):
	book_title = models.CharField(max_length=200)
	#book_author = models.CharField(max_length=200, default = "")
	
	def __unicode__(self):
		return unicode(self.book_title)

class People(models.Model):
	fullname = models.CharField(max_length=200)
	age = models.IntegerField()
	#reading_now = models.TextField(null = True)
	#reading_now = models.ForeignKey(Books, on_delete=models.CASCADE)
	reading_now = models.ManyToManyField(Books)
	
	def __str__(self):
		return self.fullname
	def __unicode__(self):
		return unicode(self.fullname)
		
class Myself(models.Model):
	my_name = models.ForeignKey('auth.User')
	my_age = models.IntegerField()
	my_reading_now = models.CharField(max_length=200)
	
	def __unicode__(self):
		return unicode(self.my_reading_now)
	def __str__(self):
		return unicode(self.my_reading_now)