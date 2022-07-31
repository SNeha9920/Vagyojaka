from django.urls import path
from appVāgyojaka import views

urlpatterns = [
    path('xmldata', views.xmldata)
]
