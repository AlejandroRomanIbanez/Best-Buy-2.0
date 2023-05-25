from abc import ABC, abstractmethod

class Promotion(ABC):

    name = ""

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        discounted_quantity = quantity // 2
        remaining_quantity = quantity - discounted_quantity
        return product.price * remaining_quantity


class ThirdOneFree(Promotion):

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        free_quantity = quantity // 3
        remaining_quantity = quantity - free_quantity
        return product.price * remaining_quantity


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount_percentage = self.percent / 100
        return product.price * quantity * (1 - discount_percentage)
