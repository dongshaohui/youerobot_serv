#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render_to_response, redirect
import json
# Create your views here.

def upload_android_id(request):
	android_id = None
	if 'android_id' in request.POST:
		android_id = request.POST['android_id']
	else:
		android_id = request.GET['android_id']

	Falimy.objects.create(android_id=android_id)
	response = {}
	response['status'] = 1
	return HttpResponse(json.dumps(response,ensure_ascii=False,indent=2))