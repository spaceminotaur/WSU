class Drink:
    BASE_OPTIONS = ["water", "sbrite", "pokecola", "Mr.Salt", "hill fog", "leaf wine"]
    FLAVOR_OPTIONS = ["lemon", "lime", "cherry", "strawberry", "blueberry", "mint"]

    def __init__(self):
        self._base = ""
        self._flavors = []
        self._used_flavors = []
        self._max_base = 0

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, new_base):
        if new_base in Drink.BASE_OPTIONS:
            self._base = new_base
            self._max_base = 1
        else:
            print("Invalid base option.")

    @property
    def flavors(self):
        return self._flavors

    @flavors.setter
    def flavors(self, new_flavors):
        if isinstance(new_flavors, list):
            self._flavors = new_flavors
        else:
            print("Flavors must be a list.")

    @property
    def used_flavors(self):
        return self._used_flavors

    @used_flavors.setter
    def used_flavors(self, new_used):
        if isinstance(new_used, list):
            self._used_flavors = new_used
        else:
            print("Used flavors must be a list.")

    @property
    def max_base(self):
        return self._max_base

    @max_base.setter
    def max_base(self, value):
        if isinstance(value, int) and value >= 0:
            self._max_base = value
        else:
            print("Max base must be a non-negative integer.")

    def add_flavor(self, flavor):
        if flavor not in self._used_flavors:
            if flavor in Drink.FLAVOR_OPTIONS:
                self._flavors.append(flavor)
                self._used_flavors.append(flavor)
            else:
                print("Flavor not available.")
        else:
            print("Flavor already added.")

    def add_base(self, base):
        if self._max_base < 1:
            if base in Drink.BASE_OPTIONS:
                self._base = base
                self._max_base += 1
            else:
                print("Invalid base option.")
        else:
            print("You may only have one base.")

    def add_mint(self):
        """Adds mint flavor specifically."""
        self.add_flavor("mint")

    @property
    def flavor_count(self):
        return len(self._flavors)


class Order:
    def __init__(self):
        self._total_drinks = []
        self._drink_total = 0

    @property
    def total_drinks(self):
        return self._total_drinks

    @total_drinks.setter
    def total_drinks(self, drinks):
        if isinstance(drinks, list):
            self._total_drinks = drinks
        else:
            print("Total drinks must be a list.")

    @property
    def drink_total(self):
        return self._drink_total

    @drink_total.setter
    def drink_total(self, total):
        if isinstance(total, int) and total >= 0:
            self._drink_total = total
        else:
            print("Drink total must be a non-negative integer.")

    @property
    def drink_cost(self):
        return self._drink_total * 3.00

    @property
    def total_tax(self):
        return self._drink_total * 0.075

    @property
    def total_price(self):
        return self.drink_cost + self.total_tax

    def get_receipt(self):
        print(f"Drink Cost: ${self.drink_cost:.2f}")
        print(f"Tax: ${self.total_tax:.2f}")
        print(f"Total Price: ${self.total_price:.2f}")

    def add_item(self, item):
        self._total_drinks.append(item)
        self._drink_total += 1

    def remove_item(self, item):
        if item in self._total_drinks:
            self._total_drinks.remove(item)
            self._drink_total -= 1

    

order = Order()

# Create the first Drink
drink1 = Drink()

# Add base: water
drink1.add_base("water")

# Try to add another base: sbrite (should print "you may only have one base")
drink1.add_base("sbrite")

# Add a flavor: lemon
drink1.add_flavor("lemon")

# Try to add the same flavor again (should print "Flavor already added")
drink1.add_flavor("lemon")

# Add the drink to the order
order.add_item(drink1)

# Create the second Drink
drink2 = Drink()

# Add base: pokecola
drink2.add_base("pokecola")

# Add two flavors: blueberry and mint
drink2.add_flavor("blueberry")
drink2.add_mint()

# Add the second drink to the order
order.add_item(drink2)

# Display the receipt
order.get_receipt()

# Remove the first drink from the order
order.remove_item(drink1)

# Display the updated receipt
order.get_receipt()