from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View
from django.conf import settings
import requests

class Main(generic.TemplateView):
	template_name = "gba.html"

	def get(self, request, name):
		url = requests.get(r'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyDXYDYmpNXAo01aw71oMT6KJXoI1aTTyvg')
		response = url.json()
		return HttpResponse(str(response))

class Location(generic.TemplateView):
	template_name = "location.html"