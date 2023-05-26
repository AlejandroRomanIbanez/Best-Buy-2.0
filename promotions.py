from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    An abstract base class representing a promotion.
    This class defines the structure for promotion classes, which must implement the
    abstract method `apply_promotion`.
    """

    name = ""

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply the promotion to a product with the given quantity.
        Args:
        product (Product): The product to apply the promotion to.
        quantity (int): The quantity of the product.
        Returns:
        float: The total price after applying the promotion.
        """
        pass


class SecondHalfPrice(Promotion):
    """
    A promotion class representing second half price.
    This class implements the `apply_promotion` method to calculate the total price
    after applying the second half price promotion.
    Example:
    promotion = SecondHalfPrice("Half Price")
    """

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        """
        Apply the second half price promotion to a product with the given quantity.
        Args:
        product (Product): The product to apply the promotion to.
        quantity (int): The quantity of the product.
        Returns:
        float: The total price after applying the second half price promotion.
        """
        discounted_quantity = quantity // 2
        remaining_quantity = quantity - discounted_quantity
        return product.price * remaining_quantity


class ThirdOneFree(Promotion):
    """
    A promotion class representing third one free.
    This class implements the `apply_promotion` method to calculate the total price
    after applying the third one free promotion.
    """

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        """
        Apply the third one free promotion to a product with the given quantity.
        Args:
        product (Product): The product to apply the promotion to.
        quantity (int): The quantity of the product.
        Returns:
        float: The total price after applying the third one free promotion.
        """
        free_quantity = quantity // 3
        remaining_quantity = quantity - free_quantity
        return product.price * remaining_quantity


class PercentDiscount(Promotion):
    """
    A promotion class representing a percentage discount.
    This class implements the `apply_promotion` method to calculate the total price
    after applying the percentage discount promotion.
    """

    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply the percentage discount promotion to a product with the given quantity.
        Args:
        product (Product): The product to apply the promotion to.
        quantity (int): The quantity of the product.
        Returns:
        float: The total price after applying the percentage discount promotion.
        Example:
        total_price = promotion.apply_promotion(product, 3)
        """
        discount_percentage = self.percent / 100
        return product.price * quantity * (1 - discount_percentage)
