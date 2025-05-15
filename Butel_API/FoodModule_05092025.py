
from enum import Enum, auto


# Enums for drink sizes, bases, and flavors
class Size(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    MEGA = auto()


class Base(Enum):
    WATER = auto()
    SBRITE = auto()
    POKE_COLA = auto()
    MR_SALT = auto()
    HILL_FOG = auto()
    LEAF_WINE = auto()


class Flavor(Enum):
    LEMON = auto()
    LIME = auto()
    CHERRY = auto()
    STRAWBERRY = auto()
    BLUEBERRY = auto()


# Drink class
class Drink:
    SIZE_PRICES = {
        Size.SMALL: 1.50,
        Size.MEDIUM: 1.75,
        Size.LARGE: 2.05,
        Size.MEGA: 2.15
    }

    def __init__(self):
        self._base = None
        self._flavors = []
        self._used_flavors = set()
        self._size = Size.SMALL

    def set_size(self, size):
        if isinstance(size, Size):
            self._size = size

    def add_flavor(self, flavor):
        if isinstance(flavor, Flavor) and flavor not in self._used_flavors:
            self._used_flavors.add(flavor)
            self._flavors.append(flavor)

    def add_base(self, base):
        if isinstance(base, Base) and self._base is None:
            self._base = base

    @property
    def flavors(self):
        return self._flavors

    @property
    def flavor_count(self):
        return len(self._flavors)

    @property
    def base(self):
        return self._base

    def get_size(self):
        return self._size

    def get_total(self):
        size_price = Drink.SIZE_PRICES.get(self._size, 0)
        flavor_charge = 0.15 * self.flavor_count
        return size_price + flavor_charge

    @property
    def name(self):
        return "Drink"


# Topping handler
class Topping:
    AVAILABLE_TOPPING = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Nacho Cheese": 0.30,
        "Chili": 0.60,
        "Bacon Bits": 0.30,
        "Ketchup": 0.00
    }

    @staticmethod
    def get_topping_info(topping_name: str):
        if topping_name in Topping.AVAILABLE_TOPPING:
            return topping_name, Topping.AVAILABLE_TOPPING[topping_name]
        return "", 0.0


# Food item template
class FoodItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._topping = ""
        self._topping_price = 0.0

    def set_topping_from_dict(self, topping_name):
        topping, price = Topping.get_topping_info(topping_name)
        self._topping = topping
        self._topping_price = price

    def get_total(self):
        return self._price + self._topping_price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def topping(self):
        return self._topping

    @property
    def topping_price(self):
        return self._topping_price


# Specific food items
class Hotdog(FoodItem):
    def __init__(self):
        super().__init__("Hot Dog", 2.30)


class Corndog(FoodItem):
    def __init__(self):
        super().__init__("Corn Dog", 2.00)


class Icecream(FoodItem):
    def __init__(self):
        super().__init__("Ice Cream", 3.00)


class Onionrings(FoodItem):
    def __init__(self):
        super().__init__("Onion Rings", 1.75)


class Frenchfries(FoodItem):
    def __init__(self):
        super().__init__("French Fries", 1.50)


class Tatertots(FoodItem):
    def __init__(self):
        super().__init__("Tater Tots", 1.70)


class Nachos(FoodItem):
    def __init__(self):
        super().__init__("Nacho Chips", 1.90)


# Unified Order class
class Order:
    TAX_RATE = 0.0725

    def __init__(self):
        self.total_items = []

    def add_item(self, item):
        self.total_items.append(item)

    def remove_item(self, item):
        if item in self.total_items:
            self.total_items.remove(item)

    @property
    def item_cost(self):
        return sum(item.get_total() for item in self.total_items)

    @property
    def total_tax(self):
        return self.item_cost * self.TAX_RATE

    @property
    def total_price(self):
        return self.item_cost + self.total_tax

    def get_receipt(self):
        print("Receipt Summary")
        print("=" * 30)
        for index, item in enumerate(self.total_items, start=1):
            print(f"Item #{index}: {item.name}")
            if hasattr(item, "get_size") and hasattr(item, "flavors"):
                print(f"  Size: {item.get_size().name.replace('_', ' ').title()}")
                print(f"  Base: {item.base.name.replace('_', ' ').title() if item.base else 'None'}")
                flavor_list = ", ".join(f.name.title() for f in item.flavors)
                print(f"  Flavors: {flavor_list if item.flavors else 'None'}")
            if hasattr(item, "topping") and item.topping:
                print(f"  Topping: {item.topping} (${item.topping_price:.2f})")
            print(f"  Item Total: ${item.get_total():.2f}")
            print("-" * 30)
        print(f"Subtotal: ${self.item_cost:.2f}")
        print(f"Tax (7.25%): ${self.total_tax:.2f}")
        print(f"Total: ${self.total_price:.2f}")
        print("=" * 30)

# ======== Example Usage ========
if __name__ == "__main__":
    order = Order()

    # Create and configure a drink
    drink = Drink()
    drink.set_size(Size.LARGE)
    drink.add_base(Base.SBRITE)
    drink.add_flavor(Flavor.CHERRY)
    drink.add_flavor(Flavor.LIME)

    # Create and configure a food item
    hotdog = Hotdog()
    hotdog.set_topping_from_dict("Chili")

    # Add both to the order
    order.add_item(drink)
    order.add_item(hotdog)

    # Print the receipt
    order.get_receipt()
