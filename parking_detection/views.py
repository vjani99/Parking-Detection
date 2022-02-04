from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'parking_detection/index.html')

def parking_lot(request):
    return render(request, 'parking_detection/parking_lot.html')