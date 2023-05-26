import pytest
from products import Product


def test_create_normal_prod():
    """
    Test creating a normal product.
    """
    normal_prod = Product("Iphone14", 1300, 200)


def test_create_invalid_prod():
    """
    Test creating an invalid product.
    """
    with pytest.raises(ValueError):
        Product("sadasd", 1300, -200)
        Product("sadasd", -1300, 200)
        Product("", 1300, 200)


def test_prod_becomes_inactive():
    """
    Test if a product becomes inactive when its quantity is set to zero.
    """
    inactive_product = Product("sadasd", 1300, 5)
    inactive_product.set_quantity(0)
    assert not inactive_product.active


def test_buy_modifies_quantity():
    """
    Test if buying a product modifies its quantity.
    """
    product = Product("Example Product", 10, 20)
    purchase_quantity = 5
    expected_quantity = product.quantity - purchase_quantity
    expected_output = f"Total price: {product.price * purchase_quantity}"

    result = product.buy(purchase_quantity)

    assert product.quantity == expected_quantity
    assert result == expected_output


def test_buy_too_much():
    """
    Test buying too much quantity of a product.
    """
    product = Product("Example Product", 10, 20)
    with pytest.raises(ValueError):
        product.buy(250)
