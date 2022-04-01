from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
def index(request):
    return render(request, 'parking_detection/index.html')

def parking_lot(request):
    return render(request, 'parking_detection/parking_lot.html')

def report(request):
    return render(request, 'parking_detection/report.html')

@csrf_exempt
def model_output(request):
    if request.method == "PUT":
        nn_output = {
            "zone1": 1,
            "zone2": 0,
            "zone3": 1,
            "zone4": 0, 
        }
        return JsonResponse(nn_output)
    else:
        return JsonResponse({})
