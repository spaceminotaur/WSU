from enum import Enum, auto


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
        else:
            print("Invalid size. Use the Size enum.")

    def add_flavor(self, flavor):
        if isinstance(flavor, Flavor) and flavor not in self._used_flavors:
            self._used_flavors.add(flavor)
            self._flavors.append(flavor)
        else:
            print("Invalid or duplicate flavor.")

    def add_base(self, base):
        if isinstance(base, Base) and self._base is None:
            self._base = base
        else:
            print("Invalid base or base already set.")

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


class Order:
    def __init__(self):
        self.total_drinks = []
        self.drink_total = 0

    @property
    def drink_cost(self):
        return sum(drink.get_total() for drink in self.total_drinks)

    @property
    def total_tax(self):
        return self.drink_cost * 0.0725

    @property
    def total_price(self):
        return self.drink_cost + self.total_tax

    def add_item(self, item):
        self.total_drinks.append(item)
        self.drink_total += 1

    def remove_item(self, item):
        if item in self.total_drinks:
            self.total_drinks.remove(item)
            self.drink_total -= 1

    def get_total(self):
        return self.drink_total

    def get_receipt(self):
        print("Receipt Summary")
        print("=" * 30)
        for index, drink in enumerate(self.total_drinks, start=1):
            print(f"Drink #{index}")
            print(f"  Size: {drink.get_size().name.replace('_', ' ').title()}")
            print(f"  Base: {drink.base.name.replace('_', ' ').title() if drink.base else 'None'}")
            print(f"  Flavors: {', '.join(f.name.title() for f in drink.flavors) if drink.flavors else 'None'}")
            print(f"  Drink Total: ${drink.get_total():.2f}")
            print("-" * 30)
        print(f"Subtotal: ${self.drink_cost:.2f}")
        print(f"Tax (7.25%): ${self.total_tax:.2f}")
        print(f"Total: ${self.total_price:.2f}")
        print("=" * 30)