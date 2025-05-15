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
            # For Drinks
            if hasattr(item, "get_size") and hasattr(item, "flavors"):
                print(f"  Size: {item.get_size().name.replace('_', ' ').title()}")
                print(f"  Base: {item.base.name.replace('_', ' ').title() if item.base else 'None'}")
                flavor_list = ", ".join(f.name.title() for f in item.flavors)
                print(f"  Flavors: {flavor_list if item.flavors else 'None'}")
            # For IceStorm
            if hasattr(item, "get_base") and hasattr(item, "toppings") and not hasattr(item, "get_size"):
                print(f"  Flavor: {item.get_base()}")
                print(f"  Toppings: {', '.join(item.toppings) if item.toppings else 'None'}")
            # For Food
            if hasattr(item, "topping") and item.topping:
                print(f"  Topping: {item.topping} (${item.topping_price:.2f})")
            print(f"  Item Total: ${item.get_total():.2f}")
            print("-" * 30)
        print(f"Subtotal: ${self.item_cost:.2f}")
        print(f"Tax (7.25%): ${self.total_tax:.2f}")
        print(f"Total: ${self.total_price:.2f}")
        print("=" * 30)
