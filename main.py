import products
import store


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]
best_buy = store.Store(product_list)


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
      print("------")
      for info_product in store_object.get_all_products():
        print(info_product)
      print("------")
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

