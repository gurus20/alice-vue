from django.urls import path
from coffee_house import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myorders/', views.myorders, name='myorders'),
    path('ordernow/', views.ordernow, name='ordernow'),
    path('getmenu/', views.get_menu, name='getmenu'),
]