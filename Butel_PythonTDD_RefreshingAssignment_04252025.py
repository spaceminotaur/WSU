class Drink:
    # Class-level constants for valid base and flavor options
    BASE_OPTIONS = ["water", "sbrite", "poke cola", "Mr.Salt", "hill fog", "leaf wine"]
    FLAVOR_OPTIONS = ["lemon", "lime", "cherry", "strawberry", "blueberry"]

    def __init__(self):
        # Instance variables to hold the base, flavor list, and control values
        self._base = ""                # Stores the selected base
        self._flavors = []             # Stores added flavors
        self._used_flavors = []        # Tracks added flavors to prevent duplicates
        self._max_base = 0             # Allows only one base to be set

    def add_flavor(self, flavor):
        """
        Adds a flavor if it's a valid string and not already added.
        """
        if isinstance(flavor, str) and flavor in Drink.FLAVOR_OPTIONS:
            if flavor not in self._used_flavors:
                self._used_flavors.append(flavor)
                self._flavors.append(flavor)
            else:
                print("Flavor already added")  # Prevent duplicate flavor addition

    def add_base(self, base):
        """
        Sets the base only once if it's valid and not already set.
        """
        if isinstance(base, str) and base in Drink.BASE_OPTIONS:
            if self._max_base < 1:
                self._max_base = 1
                self._base = base
            else:
                print("Base already set")  # Prevent base overwrite

    @property
    def flavors(self):
        """
        Getter for the list of added flavors.
        """
        return self._flavors

    @property
    def flavor_count(self):
        """
        Getter for the number of flavors added.
        """
        return len(self._flavors)

    @property
    def base(self):
        """
        Getter for the selected base.
        """
        return self._base


class Order:
    def __init__(self):
        # Initialize list of drinks and count of total drinks
        self.total_drinks = []
        self.drink_total = 0

    @property
    def drink_cost(self):
        """
        Returns the total drink cost ($3.00 per drink).
        """
        return self.drink_total * 3.00

    @property
    def total_tax(self):
        """
        Returns the tax amount (7.5% of drink cost).
        """
        return self.drink_cost * 0.075

    @property
    def total_price(self):
        """
        Returns the final price after tax.
        """
        return self.drink_cost + self.total_tax

    def get_receipt(self):
        """
        Prints the receipt with cost, tax, and total price.
        """
        print(f"Drink Cost: ${self.drink_cost:.2f}")
        print(f"Tax: ${self.total_tax:.2f}")
        print(f"Total: ${self.total_price:.2f}")

    def add_item(self, item):
        """
        Adds a drink item to the order and increments drink count.
        """
        self.total_drinks.append(item)
        self.drink_total += 1

    def remove_item(self, item):
        """
        Removes a drink item from the order and decrements drink count.
        """
        if item in self.total_drinks:
            self.total_drinks.remove(item)
            self.drink_total -= 1