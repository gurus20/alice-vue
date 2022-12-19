import json

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