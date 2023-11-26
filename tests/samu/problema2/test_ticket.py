from samu.problema2.ticket import calculate_tax, calculate_discount, add_prices, Product, apply_discount


def test_calculate_tax():
    assert calculate_tax(10.0) == 12.1  # noqa: WPS432, WPS459


def test_calculate_discount_ammount():
    assert calculate_discount(50) == 0.5  # noqa: WPS432, WPS459


def test_apply_discount():
    assert apply_discount(0.5, 10.0) == 5.0  # noqa: WPS432, WPS459


def test_add_prices():
    assert add_prices([Product('pera', 10.0), Product('manzana', 5.0)]) == 15.0  # noqa: WPS432, WPS459
