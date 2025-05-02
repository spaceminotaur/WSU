class Drink:
    BASE_OPTIONS = ["water", "sbrite", "poke cola", "Mr.Salt", "hill fog", "leaf wine"]
    FLAVOR_OPTIONS = ["lemon", "lime", "cherry", "strawberry", "blueberry"]

    def __init__(self):
        self._base = ""
        self._flavors = []
        self._used_flavors = []
        self._max_base = 0

    def add_flavor(self, flavor):
        if isinstance(flavor, str) and flavor in Drink.FLAVOR_OPTIONS:
            if flavor not in self._used_flavors:
                self._used_flavors.append(flavor)
                self._flavors.append(flavor)
            else:
                print("Flavor already added")

    def add_base(self, base):
        if isinstance(base, str) and base in Drink.BASE_OPTIONS:
            if self._max_base < 1:
                self._max_base = 1
                self._base = base
            else:
                print("Base already set")

    @property
    def flavors(self):
        return self._flavors

    @property
    def flavor_count(self):
        return len(self._flavors)

    @property
    def base(self):
        return self._base


class Order:
    def __init__(self):
        self.total_drinks = []
        self.drink_total = 0

    @property
    def drink_cost(self):
        return self.drink_total * 3.00

    @property
    def total_tax(self):
        
        return self.drink_cost * 0.075

    @property
    def total_price(self):
        return self.drink_cost + self.total_tax

    def get_receipt(self):
        print(f"Drink Cost: ${self.drink_cost:.2f}")
        print(f"Tax: ${self.total_tax:.2f}")
        print(f"Total: ${self.total_price:.2f}")

    def add_item(self, item):
        self.total_drinks.append(item)
        self.drink_total += 1

    def remove_item(self, item):
        if item in self.total_drinks:
            self.total_drinks.remove(item)
            self.drink_total -= 1