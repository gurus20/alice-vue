import json
from django.http import JsonResponse
from coffee_house.order_book import Myorders, check_orderbook, Order
from coffee_house.menu import RegularTea, menu_items

def home(request):
  return JsonResponse({'status': '200'})

myorder = Myorders("ACH00021223") 
order1 = Order() 
order2 = Order()  
order3 = Order()  

def ordernow(request):
  return JsonResponse({'status': 'ok'})

def get_menu(request):
  return JsonResponse(menu_items, safe=False)

def myorders(request): 
  regular_tea = RegularTea()

 

  return JsonResponse(myorder.get_myorders(), safe=False) 