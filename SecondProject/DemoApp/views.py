from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'DemoApp/homepage.html')
def login(request):
	return render(request,'DemoApp/login.html')
def create_user(request):
	if request.method=='POST':
		first_name=request.POST["first_name"]
		last_name=request.POST["last_name"]
		context={"first_name":  first_name}
		return render(request,"DemoApp/login.html",context)
