import json


menu_items = [
  {
    "img_src": "Bestseller",
    "order_name": "Java Chip Frappuccino",
    "order_desc": "We blend mocha sauce and Frappuccino® chips with Frappuccino..."[:60],
    "order_price": "351.75",
  },
  {
    "img_src": "Drinks",
    "order_name": "Caffe Americano",
    "order_desc": "Rich in flavour, full-bodied espresso with hot water in true European style."[:60],
    "order_price": "252.00",
  },
  {
    "img_src": "Cappuccino",
    "order_name": "Cappuccino",
    "order_desc": "Dark, Rich in flavour espresso lies in wait under a smoothed and stretched layer of thick foam."[:60],
    "order_price": "273.00",
  },
  {
    "img_src": "CaffeLatte",
    "order_name": "Caffe Latte",
    "order_desc": "Our dark, Rich in flavour espresso balanced with steamed milk and a light layer of foam. A perfect coffee warm up."[:60],
    "order_price": "273.00",
  },
]



class TeaBase():
  tea_leaves = 0
  sugar = 0
  milk = 0
  cardemon = 0
  ginger = 0
  price = 0


class RegularTea(TeaBase):
  def __init__(self) -> None:
    self.order_name = "Regular Tea"
    self.tea_leaves = 2
    self.sugar = 2
    self.milk = 2
    self.cardemon = 2
    self.ginger = 2
    self.price = 39.99

  def get_regular_tea(self):
    return json.dumps(self, default=lambda o: o.__dict__)