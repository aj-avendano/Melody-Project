from django.urls import path
from . import views

##Function Written by Jason Eissayou
urlpatterns = [
    path('', views.dashboard, name="Dashboard")
]
