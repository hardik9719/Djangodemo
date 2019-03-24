from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'inventory/homepage.html')
def items(request):
	return render(request, 'inventory/index.html')
def details(request):
	return render(request,'inventory/details.html')
