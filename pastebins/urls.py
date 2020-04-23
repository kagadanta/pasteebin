from django.urls import path

from pastebins import views

urlpatterns = [
    path('', views.index, name='index'),
]