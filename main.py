import products
import promotions
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)
best_buy = store.Store(product_list)


def show_all_products():
    """
    Print information about all the products in the product_list.
    This function iterates through the product_list and prints information about each product.
    The information includes the name, price, quantity, and promotion (if applicable) of each product.
    The product information is separated by a line of dashes before and after the list of products.
    """
    print("------")
    for product in product_list:
        print(product.show())
    print("------")


def start(store_object):
    """
    Start the store program.
    Args:
    store (Store): The Store object representing the store.
    """
    while True:
        print("Store Menu\n----------")
        user_choice = int(input("""
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: """))
        if user_choice == 1:
            show_all_products()
        elif user_choice == 2:
            print(store_object.get_total_quantity())
        elif user_choice == 3:
            print("------")
            for info_product in store_object.get_all_products():
                print(info_product)
            print("------")
            shopping_list = []
            print("When you want to finish the order, enter an empty text.")
            while True:
                product_choice = input("Which product # do you want?\n")
                if not product_choice:
                    break
                product_index = int(product_choice) - 1
                if product_index < 0 or product_index >= len(product_list):
                    print("Invalid product number. Please try again.")
                    continue
                product = store_object.products[product_index]
                quantity = int(input("What amount do you want?"))
                if isinstance(product, products.LimitedProduct) and quantity > product.maximum:
                    print(f"Cannot purchase more than {product.maximum} of {product.name}. Please try again.")
                    continue
                if quantity > product.quantity:
                    print("Not enough quantity in the store. Please try again.")
                    continue
                shopping_list.append((product, quantity))
                print("Product added to list!\n")
            total_price = store_object.order(shopping_list)
            print(f"Total price: {total_price}")
        elif user_choice == 4:
            break


def main():
    """Entry point of the store program."""
    start(best_buy)


if __name__ == "__main__":
    main()
