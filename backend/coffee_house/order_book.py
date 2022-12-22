import json

"""

Orderbook Structure

{
    "order_list": [
        {
            "order_name": {
                "quantity": "",
                "per_price": "",
                "order_total_price": ""
            }
        }
    ],
    "total_price": "",
    "discount": "",
    "final_price": ""
}



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

"""


def check_orderbook(token):
  f = open("coffee_house/order_book.json", "r")
  order_data = json.loads(f.read())

  if order_data[token] != None:
    return order_data
  else:
    return None

class Order():
  def __init__(self):  
    self.quantity = 0
    self.per_price = 0
    self.order_total_price = 0

  def get_order(self):
    return json.dumps(self, default=lambda o: o.__dict__)

class Ordername():
  def __init__(self, name):
    self.order_name = ""
    name = Order()

  def get_order_name(self):
    return json.dumps(self, default=lambda o: o.__dict__)

class Myorders():
  def __init__(self, token):
    self.token = token
    self.order_list = {}
    self.total_price = 0
    self.discount = 0
    self.final_price = 0
  
  def get_myorders(self):
    return json.dumps(self, default=lambda o: o.__dict__)
