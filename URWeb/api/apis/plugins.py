from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import json


class Plugins(generic.View):
	def get(self, request, name, format):
		result = ''
		result += '<option>Find Nearby Person</option>'
		result += '<option>Not find</option>'
		result += '<option>Not null find</option>'
		result += '<option>Find Nearby Person</option>'
		result += '<option>Not find</option>'
		result += '<option>Not null find</option>'
		result += '<option>Find Nearby Person</option>'
		result += '<option>Not find</option>'
		result += '<option>Not null find</option>'
		result += '<option>Find Nearby Person</option>'
		result += '<option>Not find</option>'
		result += '<option>Not null find</option>'
		return HttpResponse(result)

	def put(self, request, name, format):
		data = json.loads(request.body)
		if data['name'] == 'adi_plugin':
			return HttpResponse("OK")
		else:
			return HttpResponse("Bad plugin name")
