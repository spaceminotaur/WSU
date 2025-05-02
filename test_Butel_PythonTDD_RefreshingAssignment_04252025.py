import unittest
from Butel_PythonTDD_RefreshingAssignment_04252025 import Drink, Order

class TestDrinkAndOrder(unittest.TestCase):

    def test_add_base_once(self):
        drink = Drink()
        drink.add_base("poke cola")
        self.assertEqual(drink.base, "poke cola")

        drink.add_base("sbrite")  # Should not overwrite
        self.assertEqual(drink.base, "poke cola")

    def test_invalid_base_does_nothing(self):
        drink = Drink()
        drink.add_base("invalid base")
        self.assertEqual(drink.base, "")

    def test_add_flavor_once(self):
        drink = Drink()
        drink.add_flavor("lemon")
        self.assertIn("lemon", drink.flavors)
        self.assertEqual(drink.flavor_count, 1)

    def test_add_duplicate_flavor(self):
        drink = Drink()
        drink.add_flavor("lime")
        drink.add_flavor("lime")  # Duplicate should be ignored
        self.assertEqual(drink.flavor_count, 1)

    def test_invalid_flavor_does_nothing(self):
        drink = Drink()
        drink.add_flavor("mango")  # Not in allowed list
        self.assertEqual(drink.flavor_count, 0)

    def test_drink_getters(self):
        drink = Drink()
        drink.add_base("hill fog")
        drink.add_flavor("strawberry")
        drink.add_flavor("blueberry")

        self.assertEqual(drink.base, "hill fog")
        self.assertEqual(drink.flavors, ["strawberry", "blueberry"])
        self.assertEqual(drink.flavor_count, 2)

    def test_order_add_items(self):
        drink1 = Drink()
        drink1.add_base("water")
        drink1.add_flavor("lemon")

        drink2 = Drink()
        drink2.add_base("sbrite")
        drink2.add_flavor("lime")

        order = Order()
        order.add_item(drink1)
        order.add_item(drink2)

        self.assertEqual(order.drink_total, 2)
        self.assertAlmostEqual(order.drink_cost, 6.00)
        self.assertAlmostEqual(order.total_tax, 0.45)
        self.assertAlmostEqual(order.total_price, 6.45)

    def test_order_remove_item(self):
        drink = Drink()
        drink.add_base("poke cola")
        drink.add_flavor("cherry")

        order = Order()
        order.add_item(drink)
        self.assertEqual(order.drink_total, 1)

        order.remove_item(drink)
        self.assertEqual(order.drink_total, 0)


if __name__ == '__main__':
    unittest.main()