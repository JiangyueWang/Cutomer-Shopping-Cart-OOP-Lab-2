from shoppingcart import ShoppingCart


class Customer:
    def __init__(self, name):
        self.customer_name = name
        self.customer_shopping_cart = ShoppingCart()

    def add_item_list(self, item):
        self.customer_shopping_cart.add_item_list(item)

    def display_items(self):
        for item in self.customer_shopping_cart.cart_list:
            print(
                f'Name: {item.product_name} Price: {item.product_price} Category: {item.product_category}')
