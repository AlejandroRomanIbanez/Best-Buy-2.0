import pytest
import products
import promotions


def test_create_normal_prod():
    """
    Test creating a normal product.
    """
    normal_prod = products.Product("Iphone14", 1300, 200)


def test_create_invalid_prod():
    """
    Test creating an invalid product.
    """
    with pytest.raises(ValueError):
        products.Product("sadasd", 1300, -200)
        products.Product("sadasd", -1300, 200)
        products.Product("", 1300, 200)


def test_prod_becomes_inactive():
    """
    Test if a product becomes inactive when its quantity is set to zero.
    """
    inactive_product = products.Product("sadasd", 1300, 5)
    inactive_product.set_quantity(0)
    assert not inactive_product.active


def test_buy_modifies_quantity():
    """
    Test if buying a product modifies its quantity.
    """
    product = products.Product("Example Product", 10, 20)
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
    product = products.Product("Example Product", 10, 20)
    with pytest.raises(ValueError):
        product.buy(250)


def test_pass_the_limit():
    """
    Test buying more than the max limit
    """
    product = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError):
        product.buy(2)


def test_all_promotions():
    """
    Test that all promotions works as it should be
    """
    product = products.Product("Example Product", 10, 5)
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    percent_discount = promotions.PercentDiscount("30% off!", percent=30)

    total_price = second_half_price.apply_promotion(product, 4)
    assert total_price == 20
    total_price = third_one_free.apply_promotion(product, 6)
    assert total_price == 40
    total_price = percent_discount.apply_promotion(product, 3)
    assert total_price == 21


