from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'parking_detection/index.html')

def parking_lot(request):
    return render(request, 'parking_detection/parking_lot.html')

def parking_lot2(request):
    return render(request, 'parking_detection/parking_lot2.html')

def about_us(request):
    return render(request, 'parking_detection/about_us.html')

def contact_us(request):
    return render(request, 'parking_detection/contact_us.html')