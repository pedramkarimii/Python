# store customer purchase orders
customer_orders = {}


def add_item(customer: str, product_name: str, price: int, quantity=1):
    # check if the customer already has a purchase order
    if customer in customer_orders:
        # check if the customer wants to save or replace the order
        print("option:\n1.save\n2.replace")

        action = input(
            f" {customer} this order already exists. Do you want to save or replace the order?\n(enter the option number): ")

        if action == '1':
            customer_orders[customer].append((product_name, price, quantity))
            total_price = price * quantity
            print(f"{quantity} {product_name} added to {customer}  cart. Total cost: {total_price}$")
        elif action == '2':
            customer_orders[customer] = [(product_name, price, quantity)]
            total_price = price * quantity
            print(f"{quantity} {product_name} added to {customer}  cart. Total cost: {total_price}$")
        else:
            print("Invalid action!!!. Please enter '1' or '2'.")
    else:
        customer_orders[customer] = [(product_name, price, quantity)]
        total_price = price * quantity
        print(f"{quantity} {product_name} added to {customer}  cart. Total cost: {total_price}$")


# delete a purchase
def remove_item(customer: str, product_name: str):
    if customer in customer_orders:
        for item in customer_orders[customer]:
            if item[0] == product_name:
                customer_orders[customer].remove(item)
                print(f"{product_name} removed from {customer} cart.")
                break
        else:
            print(f"{product_name} not found in {customer} cart.")
    else:
        print(f"{customer} cart is empty.")


# summary of the price of the number of purchases
def calculate_total(customer: str):
    if customer in customer_orders:
        total = sum(price * quantity for _, price, quantity in customer_orders[customer])
        print(f"Total price for {customer} purchase order: {total}$")
    else:
        print(f"{customer}  cart is empty.")


# details of the purchase made
def display_order(customer: str):
    if customer in customer_orders:
        print(f"{customer} Purchase Order:")
        for product, price, quantity in customer_orders[customer]:
            print(f"{quantity} {product} at {price}$ each")
    else:
        print(f"{customer} cart is empty.")


# infinite loop for to rceive and record information
while True:
    try:
        print("Options:\n1.Add\n2.remove\n3.calculate\n4.search\n5.exit")

        order = input("Enter the Options : ")
        # add values
        if order == '1':
            customer = input("Enter customer name: ")
            product_name = input("Enter product name: ")
            price = eval(input("Enter price per item: "))
            quantity = int(input("Enter quantity (default is 1): "))
            add_item(customer, product_name, price, quantity)
        # delete a purchase
        elif order == '2':
            customer = input("Enter customer name: ")
            product_name = input("Enter product name to remove: ")
            remove_item(customer, product_name)

        elif order == '3':
            customer = input("Enter customer name: ")
            calculate_total(customer)
        elif order == '4':
            customer = input("Enter customer name: ")
            display_order(customer)
        elif order == '5':
            print("Have good time, visit our site again to see new products.")
            break
        else:
            print(
                "Invalid order!!! Please enter:\nnumber(1) for the add item.\nnumber(2)for the remove item.\nnumber(3) for the calculate total.\nnumber(4)for the display order.\nnumber(5)for the Exit.")
    except Exception as e:
        print(f"Error!!!An error occurred: {e}")
