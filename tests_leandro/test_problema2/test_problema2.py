from leandro.problema2.problema2 import sum_prices, apply_iva, apply_discount, Product


def test_sum_prices() -> None:
    lista_productos = [Product("manzana", 5), Product("plátano", 2), Product("pera", 3)]
    assert (sum_prices(lista_productos) == 10)


def test_apply_iva() -> None:
    lista_productos = [Product("manzana", 5), Product("plátano", 2), Product("pera", 3)]
    assert (apply_iva(10, lista_productos) == 12.1)


def test_apply_discount() -> None:
    assert (apply_discount(12.1, 10) == 10.89)
