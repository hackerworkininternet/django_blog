from django.shortcuts import render
from django.shortcuts import HttpResponse


def about(request):
	# return HttpResponse("hi there i am evil spirit in About")
	return render(request , 'about.html')

def home(request):
	# return HttpResponse("hi there i am evil spirit in Home")
	return render(request , 'home.html')