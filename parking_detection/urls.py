from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('harris-commons', views.parking_lot, name='parking_lot'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us')
]