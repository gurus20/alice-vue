import json
from django.http import JsonResponse
from coffee_house.order_book import Myorders, check_orderbook, Order
from coffee_house.menu import RegularTea

def home(request):
  return JsonResponse({'status': '200'})

myorder = Myorders("ACH00021223") 
order1 = Order() 
order2 = Order()  
order3 = Order()  

def myorders(request): 
  regular_tea = RegularTea()

  myorder.order_list[regular_tea.order_name] = order1

  myorder.order_list[regular_tea.order_name].per_price = regular_tea.price
  myorder.order_list[regular_tea.order_name].quantity += 1
  myorder.order_list[regular_tea.order_name].order_total_price += regular_tea.price


  myorder.total_price += regular_tea.price
  myorder.final_price = myorder.total_price

  myorder.order_list["Coffee"] = order2
  myorder.order_list["Coffee"].per_price = regular_tea.price
  myorder.order_list["Coffee"].quantity += 1
  myorder.order_list["Coffee"].order_total_price += regular_tea.price

  myorder.total_price += regular_tea.price
  myorder.final_price = myorder.total_price

  myorder.order_list["Orea Shake"] = order2
  myorder.order_list["Orea Shake"].per_price = regular_tea.price
  myorder.order_list["Orea Shake"].quantity += 1
  myorder.order_list["Orea Shake"].order_total_price += regular_tea.price

  myorder.total_price += regular_tea.price
  myorder.final_price = myorder.total_price

  json_object = json.loads(myorder.get_myorders())
   
  # print(json.dumps(json_object, indent = 2))

  return JsonResponse(myorder.get_myorders(), safe=False) 