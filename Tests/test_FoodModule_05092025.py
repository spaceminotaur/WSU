import unittest
from FoodModule_05092025 import Hotdog, Frenchfries, Tatertots

class TestFoodAndTopping(unittest.TestCase):
    def test_hotdog_base_price(self):
        dog = Hotdog()
        self.assertEqual(dog.price, 2.30)
        self.assertEqual(dog.get_total(), 2.30)

    def test_topping_assignment(self):
        dog = Hotdog()
        dog.set_topping_from_dict("Chili")
        self.assertEqual(dog.topping, "Chili")
        self.assertAlmostEqual(dog.topping_price, 0.60)
        self.assertAlmostEqual(dog.get_total(), 2.90)

    def test_invalid_topping(self):
        fries = Frenchfries()
        fries.set_topping_from_dict("InvalidSauce")
        self.assertEqual(fries.topping, "")
        self.assertEqual(fries.topping_price, 0.0)
        self.assertEqual(fries.get_total(), 1.50)

    def test_multiple_foods_total(self):
        dog = Hotdog()
        dog.set_topping_from_dict("Bacon Bits")

        tots = Tatertots()
        tots.set_topping_from_dict("Ketchup")

        total = dog.get_total() + tots.get_total()
        self.assertAlmostEqual(total, 2.30 + 0.30 + 1.70 + 0.00)

if __name__ == "__main__":
    unittest.main()
