import unittest
from drink_order import Drink, Order


class TestDrinkAndOrder(unittest.TestCase):
    # Test that add_base sets a valid base once and prevents it from being overwritten
    def test_add_base_once(self):
        drink = Drink()
        drink.add_base("poke cola")  # Setter method for base
        self.assertEqual(drink.base, "poke cola")  # Getter for base

        drink.add_base("sbrite")  # Should not overwrite existing base
        self.assertEqual(drink.base, "poke cola")  # Getter again

    # Test that an invalid base (not in BASE_OPTIONS) does not set the base
    def test_invalid_base_does_nothing(self):
        drink = Drink()
        drink.add_base("invalid base")  # Setter method (should do nothing)
        self.assertEqual(drink.base, "")  # Getter for base

    # Test that a valid flavor is added successfully
    def test_add_flavor_once(self):
        drink = Drink()
        drink.add_flavor("lemon")  # Setter method for flavors
        self.assertIn("lemon", drink.flavors)  # Getter for flavors
        self.assertEqual(drink.flavor_count, 1)  # Getter for flavor_count

    # Test that duplicate flavors are not added
    def test_add_duplicate_flavor(self):
        drink = Drink()
        drink.add_flavor("lime")
        drink.add_flavor("lime")  # Duplicate, should be ignored
        self.assertEqual(drink.flavor_count, 1)  # Getter for flavor_count

    # Test that invalid flavor names are ignored
    def test_invalid_flavor_does_nothing(self):
        drink = Drink()
        drink.add_flavor("mango")  # Invalid setter call
        self.assertEqual(drink.flavor_count, 0)  # Getter

    # Test all getters together: base, flavors, and flavor_count
    def test_drink_getters(self):
        drink = Drink()
        drink.add_base("hill fog")
        drink.add_flavor("strawberry")
        drink.add_flavor("blueberry")

        self.assertEqual(drink.base, "hill fog")  # Getter
        self.assertEqual(drink.flavors, ["strawberry", "blueberry"])  # Getter
        self.assertEqual(drink.flavor_count, 2)  # Getter

    # Test adding multiple drinks to an order and calculating cost/tax/total
    def test_order_add_items(self):
        drink1 = Drink()
        drink1.add_base("water")
        drink1.add_flavor("lemon")

        drink2 = Drink()
        drink2.add_base("sbrite")
        drink2.add_flavor("lime")

        order = Order()
        order.add_item(drink1)  # Add item to order
        order.add_item(drink2)

        self.assertEqual(order.drink_total, 2)  # Getter for drink_total
        self.assertAlmostEqual(order.drink_cost, 6.00)  # Getter
        self.assertAlmostEqual(order.total_tax, 0.45)  # Getter
        self.assertAlmostEqual(order.total_price, 6.45)  # Getter

    # Test removing an item from the order and checking drink total
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