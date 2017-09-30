# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import People
from django.http import HttpResponse
from random import randint


# Create your views here.

def people_list(request):
	persons = People.objects.all()
	return render(request, 'toader/people_list.html', {'persons':persons})
	
	
def user_front(request):
	
	filtered_list = People.objects.filter(reading_now="Steve Jobs")
	slice = randint(0, filtered_list.count() -1)
	person = filtered_list[slice]
	#html = "<html><body>It is now %s. </body></html>" % persons
	#return HttpResponse(html)
	return render(request, 'toader/user_front.html', {'person':person} )
	
