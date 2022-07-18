from product import Product
from shoppingcart import ShoppingCart
from customer import Customer

product_one = Product("apple", 4.5, "fruit")
product_two = Product("pear", 3.4, "fruit")
product_three = Product("orange", 3.4, "fruit")


customer_one = Customer("J")
print(f'customer name is {customer_one.customer_name}')

customer_one.add_item_list(product_one)
customer_one.add_item_list(product_two)
customer_one.add_item_list(product_three)
customer_one.display_items()

total_item_in_customer_shopping_cart = customer_one.customer_shopping_cart.count_total_items()
print(
    f'total items in the current customer shopping cart is {total_item_in_customer_shopping_cart}')

print('----empty current shopping cart---')
customer_one.customer_shopping_cart.empty_cart()
print(customer_one.display_items())
