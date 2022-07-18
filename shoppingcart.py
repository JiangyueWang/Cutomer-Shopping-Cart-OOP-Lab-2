from product import Product


class ShoppingCart:
    def __init__(self):
        self.cart_list = []

    def count_total_items(self):
        self.total_items = len(self.cart_list)
        return self.total_items

    def add_item_list(self, item):
        self.cart_list.append(item)

    def empty_cart(self):
        self.cart_list = []
