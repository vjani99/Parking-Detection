from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('harris-commons', views.parking_lot, name='parking_lot')
]