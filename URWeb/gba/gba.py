from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View
from django.conf import settings
import re
import requests
import time
import json
# import urllib

class Main(generic.TemplateView):
	template_name = "gba.html"

	def constructData(self, googlePlacesResponse, apiKey, count = None):
		data = []
		resultCode = 0
		firstResultCode = 0
		counter = 0
		while True:
			if count and counter >= count:
				break

			if "status" in googlePlacesResponse:
				if googlePlacesResponse['status'] == "OK":
					resultCode = -1
				elif googlePlacesResponse['status'] == "ZERO_RESULTS":
					resultCode = 0
				elif googlePlacesResponse['status'] == "OVER_QUERY_LIMIT":
					resultCode = 1
				elif googlePlacesResponse['status'] == "REQUEST_DENIED":
					resultCode = 2
				elif googlePlacesResponse['status'] == "INVALID_REQUEST":
					resultCode = 3
				else:
					resultCode = 4

				if counter == 0:
					firstResultCode = resultCode
				
				if resultCode == -1:
					if "results" in googlePlacesResponse:
						for result in googlePlacesResponse["results"]:
							data.append(result)

					if "next_page_token" in googlePlacesResponse:
						if len(googlePlacesResponse["next_page_token"]):
							url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={}&key={}".format(googlePlacesResponse["next_page_token"], apiKey)
							currentTime = time.time()
							limitTime = currentTime + 10
							while limitTime < time.time():
								time.sleep(1)
								ret = requests.get(url)
								googlePlacesResponse = ret.json()
								if googlePlacesResponse['status'] == "OK":
									break
						else:
							break
					else:
						break
				else:
					break
			else:
				break
			counter += 1

		return firstResultCode, resultCode, data


			

	def get(self, request, name):
		# url = requests.get(r'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyDXYDYmpNXAo01aw71oMT6KJXoI1aTTyvg')
		apiKey = "AIzaSyDXYDYmpNXAo01aw71oMT6KJXoI1aTTyvg"
		# url = requests.get(r'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=500&key={}'.format(lat, lng, apiKey))
		url = requests.get(r'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=500&key={}'.format("-33.8670522", "151.1957362", apiKey))
		response = url.json()
		firstResultCode, resultCode, data = self.constructData(response, apiKey, 2)
		
		# for items in response['results']:
		# 	for types in items['types']:
		# 		if types not in allTypes:
		# 			allTypes.append(types)
		result = "<html>{}<br>{}<br><ol>".format(firstResultCode, resultCode)
		allTypes = []
		for items in data:
			result += "<li>" + str(items) + "</li>"
		result += "</ol></html>"
		return HttpResponse(str(result))

	def post(self, request, name):
		# url = requests.get(r'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyDXYDYmpNXAo01aw71oMT6KJXoI1aTTyvg')
		apiKey = "AIzaSyDXYDYmpNXAo01aw71oMT6KJXoI1aTTyvg"
		# url = requests.get(r'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=500&key={}'.format(lat, lng, apiKey))
		url = requests.get(r'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=500&key={}'.format(request.POST["lat"], request.POST["lng"], apiKey))
		response = url.json()
		firstResultCode, resultCode, data = self.constructData(response, apiKey, 2)
		
		# for items in response['results']:
		# 	for types in items['types']:
		# 		if types not in allTypes:
		# 			allTypes.append(types)
		# result = "<html>{}<br>{}<br><ol>".format(firstResultCode, resultCode)
		# allTypes = []
		# for items in data:
		# 	result += "<li>" + str(items['name'].encode('ascii', 'ignore')) + "</li>"
		# result += "</ol></html>"
		# result = ""
		# for items in data:
		# 	result += items['name'].encode('ascii', 'ignore') + "\n"
		allTypes = []
		for item in data:
			for types in item['types']:
				if types not in allTypes:
					allTypes.append(types)
		result = allTypes
		return HttpResponse(str(result))

class Location(generic.TemplateView):
	template_name = "location.html"