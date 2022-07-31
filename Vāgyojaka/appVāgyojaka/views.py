from django.shortcuts import render
import xml.etree.ElementTree as ET
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http.response import JsonResponse, HttpResponse

# Create your views here.
# @csrf_exempt
@api_view(['POST', 'GET'])
def xmldata(request):
	tree = ET.parse("C:/Users/admin/OneDrive/Desktop/malhar_5.xml")
	root = tree.getroot()
	st = []
	for line in root.findall('./line'):
		w = ""
		for word in line.findall('./word'):
			w += word.text + " "
		w = w[:-1]
		st.append({"timestamp" : line.attrib["timestamp"], "line": w})
	context = {
	'st': st
	}
	return render(request, 'Vāgyojaka.html', context)