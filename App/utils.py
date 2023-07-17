class Food:
    def __init__(self, name, price, shelf_life, location, quantity=1):
        self.name = name
        self.price=price
        self.shelf_life=shelf_life
        self.location=location
        self.quantity=quantity

class Meal:
    def __init__(self, ingredients, planned_date, shelf_life):
        self.ingredients = ingredients
        self.planned_date = planned_date
        self.actual_date = None
        self.shelf_life = shelf_life


