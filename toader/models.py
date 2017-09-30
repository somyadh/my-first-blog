# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from random import randint
from django.db.models import Count
# Create your models here.

# class UserManager(models.Manager):
	# def random(self):
		# count = self.aggregate(	count=Count('id'))['count']
		# random_index = randint(0, count -1)
		# return self.all()[random_index]



class People(models.Model):
	#username = models.ForeignKey('auth.User')
	#objects = UserManager()
	fullname = models.CharField(max_length=200, null=True)
	age = models.IntegerField()
	reading_now = models.TextField()
	
	def __str__(self):
		return self.fullname
	def __unicode__(self):
		return unicode(self.fullname)
		
	
	
