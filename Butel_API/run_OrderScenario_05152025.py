from UnifiedOrderSystem_05152025 import Order
from DrinkModule_EnumBased_05052025 import Drink, Base, Flavor, Size
from FoodModule_05092025 import Hotdog, Frenchfries
from IceStormDessertModule_05152025 import IceStorm, IceStormTopping, IceCreamFlavor

# Create an order
order = Order()

# Add a drink with 2 flavors
drink = Drink()
drink.set_size(Size.LARGE)
drink.add_base(Base.MR_SALT)
drink.add_flavor(Flavor.LEMON)
drink.add_flavor(Flavor.LIME)
order.add_item(drink)

# Add a food item with a topping
hotdog = Hotdog()
hotdog.set_topping_from_dict("Chili")
order.add_item(hotdog)

# Add an ice storm dessert with a topping
ice_storm = IceStorm()
ice_storm.set_flavor(IceCreamFlavor.CHOCOLATE)
ice_storm.add_topping(IceStormTopping.COOKIE_DOUGH)
order.add_item(ice_storm)

# Get first receipt
print("\n--- First Receipt ---")
order.get_receipt()

# Remove a flavor from the drink manually (simulate by recreating drink without it)
drink.flavors.pop()  # remove the last flavor (Flavor.LIME)

# Remove the food item
order.remove_item(hotdog)

# Add second flavor to the drink
drink.add_flavor(Flavor.STRAWBERRY)

# Add another food item
fries = Frenchfries()
fries.set_topping_from_dict("Ketchup")
order.add_item(fries)

# Get updated receipt
print("\n--- Updated Receipt ---")
order.get_receipt()
