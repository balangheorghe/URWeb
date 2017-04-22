from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class Plugins(generic.View):
    def get(self, request, name, format):
        return HttpResponse("OKOKOKOK")

    def put(self, request):
    	return HttpResponse("OK")
