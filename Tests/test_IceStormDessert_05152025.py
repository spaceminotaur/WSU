import unittest
from IceStormDessert_WithToppingCount_05152025 import IceStorm, IceStormTopping, IceCreamFlavor


class TestIceStormDessert(unittest.TestCase):

    def test_flavor_set_and_base_retrieval(self):
        dessert = IceStorm()
        dessert.set_flavor(IceCreamFlavor.BUTTER_PECAN)
        self.assertEqual(dessert.get_base(), "Butter Pecan")

    def test_add_valid_toppings(self):
        dessert = IceStorm()
        dessert.set_flavor(IceCreamFlavor.CHOCOLATE)
        dessert.add_topping(IceStormTopping.CHERRY)
        dessert.add_topping(IceStormTopping.STORIOS)
        self.assertIn(IceStormTopping.CHERRY, dessert.toppings)
        self.assertIn(IceStormTopping.STORIOS, dessert.toppings)
        self.assertEqual(dessert.topping_count, 2)

    def test_duplicate_toppings_are_ignored(self):
        dessert = IceStorm()
        dessert.set_flavor(IceCreamFlavor.BANANA)
        dessert.add_topping(IceStormTopping.CHERRY)
        dessert.add_topping(IceStormTopping.CHERRY)
        self.assertEqual(dessert.topping_count, 1)

    def test_invalid_topping_is_ignored(self):
        dessert = IceStorm()
        dessert.set_flavor(IceCreamFlavor.VANILLA_BEAN)
        dessert.add_topping("INVALID")
        self.assertEqual(dessert.topping_count, 0)

    def test_total_price_calculation(self):
        dessert = IceStorm()
        dessert.set_flavor(IceCreamFlavor.MINT_CHOCOLATE_CHIP)
        dessert.add_topping(IceStormTopping.CHOCOLATE_SAUCE)  # $0.50
        dessert.add_topping(IceStormTopping.COOKIE_DOUGH)     # $1.00
        expected_total = 4.00 + 0.50 + 1.00
        self.assertAlmostEqual(dessert.get_total(), expected_total)

    def test_default_total_with_no_flavor(self):
        dessert = IceStorm()
        self.assertEqual(dessert.get_total(), 0.0)


if __name__ == "__main__":
    unittest.main()
