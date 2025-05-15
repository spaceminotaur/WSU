from enum import Enum, auto


class IceCreamFlavor(Enum):
    MINT_CHOCOLATE_CHIP = auto()
    CHOCOLATE = auto()
    VANILLA_BEAN = auto()
    BANANA = auto()
    BUTTER_PECAN = auto()
    SMORE = auto()


class IceStormTopping:
    CHERRY = "Cherry"
    WHIPPED_CREAM = "Whipped Cream"
    CARAMEL_SAUCE = "Caramel Sauce"
    CHOCOLATE_SAUCE = "Chocolate Sauce"
    PECANS = "Pecans"
    STORIOS = "Storios"
    DIG_DOGS = "Dig Dogs"
    TANDTS = "TandT's"
    COOKIE_DOUGH = "Cookie Dough"

    AVAILABLE_TOPPING = {
        CHERRY: 0.00,
        WHIPPED_CREAM: 0.00,
        CARAMEL_SAUCE: 0.50,
        CHOCOLATE_SAUCE: 0.50,
        PECANS: 0.50,
        STORIOS: 1.00,
        DIG_DOGS: 1.00,
        TANDTS: 1.00,
        COOKIE_DOUGH: 1.00
    }


class IceStorm:
    FLAVOR_PRICES = {
        IceCreamFlavor.MINT_CHOCOLATE_CHIP: 4.00,
        IceCreamFlavor.CHOCOLATE: 3.00,
        IceCreamFlavor.VANILLA_BEAN: 3.00,
        IceCreamFlavor.BANANA: 3.50,
        IceCreamFlavor.BUTTER_PECAN: 3.50,
        IceCreamFlavor.SMORE: 4.00
    }

    def __init__(self):
        self._flavor = None
        self._toppings = []
        self._topping_total = 0.0

    def set_flavor(self, flavor):
        if isinstance(flavor, IceCreamFlavor):
            self._flavor = flavor

    def add_topping(self, topping_name):
        if (
            topping_name in IceStormTopping.AVAILABLE_TOPPING and
            topping_name not in self._toppings
        ):
            self._toppings.append(topping_name)
            self._topping_total += IceStormTopping.AVAILABLE_TOPPING[topping_name]

    def get_total(self):
        if self._flavor is None:
            return 0.0
        base_price = IceStorm.FLAVOR_PRICES[self._flavor]
        return base_price + self._topping_total

    def get_base(self):
        return self._flavor.name.replace("_", " ").title() if self._flavor else "None"

    @property
    def flavor(self):
        return self._flavor

    @property
    def toppings(self):
        return self._toppings

    @property
    def topping_total(self):
        return self._topping_total

    @property
    def topping_count(self):
        return len(self._toppings)

    @property
    def name(self):
        return "Ice Storm Dessert"
