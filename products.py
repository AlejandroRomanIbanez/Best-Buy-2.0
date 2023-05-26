class Product:
    """A class representing a product."""
    promotion = None

    def __init__(self, name, price, quantity):
        """
        Initialize a Product object.
        Args:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product.
        Raises:
        ValueError: If the name is empty, or the price or quantity is negative.
        """
        if not name:
            raise ValueError("Invalid name. Name cannot be empty.")
        if price < 0:
            raise ValueError("Invalid price. Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Invalid quantity. Quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def set_promotion(self, promotion):
        """
        Set the promotion for the product.
        This method sets the promotion for the product to the specified promotion object.
        Args:
        promotion (Promotion): The promotion to set for the product.
        """
        self.promotion = promotion

    def get_promotion(self):
        """
        Get the promotion for the product.
        This method returns the promotion object associated with the product.
        Returns:
        Promotion: The promotion object associated with the product, or None if no promotion is set.
        """
        return self.promotion

    def get_quantity(self):
        """
        Get the quantity of the product.
        Returns:
        int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the quantity of the product.
        Args:
        quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False

    def is_active(self):
        """
        Check if the product is active.
        Returns:
        bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activate the product.
        Returns:
        bool: True if the product is activated.
        """
        self.active = True
        return self.active

    def deactivate(self):
        """
        Deactivate the product.
        Returns:
        bool: True if the product is deactivated.
        """
        self.active = False
        return self.active

    def show(self):
        """Print information about the product."""
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}"

    def buy(self, quantity):
        """
        Buy a quantity of the product.
        Args:
        quantity (int): The quantity to buy.
        Returns:
        str: A string indicating the total price of the purchase.
        """
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity available for purchase.")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
            self.quantity -= quantity
            return f"Total price (with promotion): {total_price}"
        else:
            self.quantity -= quantity
            return f"Total price: {self.price * quantity}"


class NonStockedProduct(Product):
    """
    A class representing a non-stocked product.
    This class inherits from the Product class and sets the quantity to infinity,
    making it always available. It overrides the `get_quantity`, `set_quantity`,
    `is_active`, and `buy` methods.
    """

    def __init__(self, name, price):
        super().__init__(name, price, float("inf"))

    def get_quantity(self):
        """Get the quantity of the product."""
        pass

    def set_quantity(self, quantity):
        """Set the quantity of the product."""
        pass

    def is_active(self):
        """Check if the product is active."""
        self.active = True
        return self.active

    def buy(self, quantity):
        """
        Buy a quantity of the product.
        Args:
        quantity (int): The quantity to buy.
        Returns:
        str: A string indicating the total price of the purchase.
        """
        return f"Total price: {self.price * quantity}"


class LimitedProduct(Product):
    """
    A class representing a limited quantity product.
    This class inherits from the Product class and introduces a maximum quantity
    restriction. It overrides the `buy` method to enforce the maximum quantity
    limitation.
    """

    def __init__(self, name, price, quantity, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """
        Buy a quantity of the product.
        Args:
        quantity (int): The quantity to buy.
        Returns:
        str: A string indicating the total price of the purchase.
        Raises:
        ValueError: If the quantity exceeds the maximum limit.
        """
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of {self.name}.")
        return super().buy(quantity)
