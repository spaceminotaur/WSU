import unittest
from UnifiedOrderSystem_05152025 import Order
from DrinkModule_EnumBased_05052025 import Drink, Base, Flavor, Size
from FoodModule_05092025 import Hotdog, Frenchfries
from IceStormDessertModule_05152025 import IceStorm, IceStormTopping, IceCreamFlavor


class TestUnifiedOrderSystem(unittest.TestCase):

    def test_add_drink_to_order(self):
        drink = Drink()
        drink.set_size(Size.LARGE)
        drink.add_base(Base.HILL_FOG)
        drink.add_flavor(Flavor.LEMON)
        drink.add_flavor(Flavor.STRAWBERRY)

        order = Order()
        order.add_item(drink)

        self.assertEqual(len(order.total_items), 1)
        self.assertIn(drink, order.total_items)
        self.assertGreater(order.total_price, 0)
        order.get_receipt()

    def test_add_food_to_order(self):
        hotdog = Hotdog()
        hotdog.set_topping_from_dict("Chili")

        fries = Frenchfries()
        fries.set_topping_from_dict("Ketchup")

        order = Order()
        order.add_item(hotdog)
        order.add_item(fries)

        self.assertEqual(len(order.total_items), 2)
        self.assertIn(hotdog, order.total_items)
        self.assertIn(fries, order.total_items)
        order.get_receipt()

    def test_add_ice_storm_to_order(self):
        dessert = IceStorm()
        dessert.set_flavor(IceCreamFlavor.MINT_CHOCOLATE_CHIP)
        dessert.add_topping(IceStormTopping.COOKIE_DOUGH)
        dessert.add_topping(IceStormTopping.CHOCOLATE_SAUCE)

        order = Order()
        order.add_item(dessert)

        self.assertEqual(len(order.total_items), 1)
        self.assertIn(dessert, order.total_items)
        self.assertAlmostEqual(dessert.get_total(), 4.00 + 1.00 + 0.50)
        order.get_receipt()

    def test_combined_order_receipt(self):
        drink = Drink()
        drink.set_size(Size.SMALL)
        drink.add_base(Base.SBRITE)
        drink.add_flavor(Flavor.LIME)

        hotdog = Hotdog()
        hotdog.set_topping_from_dict("Bacon Bits")

        dessert = IceStorm()
        dessert.set_flavor(IceCreamFlavor.BUTTER_PECAN)
        dessert.add_topping(IceStormTopping.STORIOS)

        order = Order()
        order.add_item(drink)
        order.add_item(hotdog)
        order.add_item(dessert)

        self.assertEqual(len(order.total_items), 3)
        order.get_receipt()


if __name__ == "__main__":
    unittest.main()
