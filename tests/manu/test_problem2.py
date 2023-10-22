from manu.problem2.problem2 import Product, apply_iva, apply_discount



def test_apply_iva():
    products: list[Product] = [Product('manzana', 9, 0)]
    products = apply_iva(products)
    assert products[0].price == 9 * 1.21
    
def test_apply_discount():
    products: list[Product] = [Product('manzana', 10, 50)]
    products = apply_discount(products)
    assert products[0].price == 5

