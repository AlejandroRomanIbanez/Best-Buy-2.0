class Store:
    """A class representing a store."""

    def __init__(self, products):
        """
        Initialize a Store object.
        Args:
        products (list): A list of products in the store.
        """
        self.products = products

    def add_product(self, product):
        """
        Add a product to the store.
        Args:
        product: The product to add to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store.
        Args:
        product: The product to remove from the store.
        """
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Product {product.name} is not in the store.")

    def get_total_quantity(self):
        """
        Get the total quantity of items in the store.
        Returns:
        str: A string indicating the total quantity of items in the store.
        """
        total = sum(product.quantity for product in self.products if product.quantity != float('inf'))
        return f"Total of {total} items in store"

    def get_all_products(self):
        """
        Get information about all products in the store.
        Returns:
        list: A list of strings representing the information
        of all products in the store.
        """
        product_list = []
        for index, product in enumerate(self.products, start=1):
            promotion_info = product.promotion.name if product.promotion else "No promotion"
            product_info = f"{index}. {product.name}, " \
                           f"Price: ${product.price}, " \
                           f"Quantity: {product.quantity}, " \
                           f"Discount: {promotion_info}"
            product_list.append(product_info)
        return product_list

    def order(self, shopping_list):
        """
        Place an order for the given shopping list.
        Args:
        shopping_list (list): A list of tuples containing the products and quantities to order.
        Returns:
        float: The total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            found_product = None
            for store_product in self.products:
                if store_product.name == product.name:
                    found_product = store_product
                    break
            if found_product is None:
                print(f"Product {product.name} not in the store")
                continue
            if found_product.quantity < quantity:
                print(f"Not enough quantity of {product.name} in the store.")
                continue
            total_price += found_product.price * quantity
            found_product.quantity -= quantity
            if found_product.quantity == 0:
                self.remove_product(found_product)
            if product.promotion is not None:
                if product.promotion.name == "Second Half price!":
                    total_price -= found_product.price * quantity // 2
                    return total_price + found_product.price * (quantity - 1) // 2
                elif product.promotion.name == "Third One Free!":
                    total_price -= found_product.price * (quantity // 3)
                elif product.promotion.name == "30% off!":
                    discount = found_product.price * (product.promotion.percent / 100)
                    total_price -= discount * quantity
        return total_price
