from django.urls import path
from coffee_house import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myorders/', views.myorders, name='myorders')
]