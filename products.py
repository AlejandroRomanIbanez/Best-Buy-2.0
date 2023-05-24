class Product:
  """A class representing a product."""

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
    self.active = True

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
    print(f"{self.name}, Price: {self.price}., Quantity: {self.quantity}")

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
    self.quantity -= quantity
    return f"Total price: {self.price * quantity}"