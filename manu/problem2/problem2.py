class Product:
    def __init__(self, name: str, price: int, discount: int) -> None:
        self.name: str = name
        self.price: float | int = price
        self.discount: int = discount


def get_products_and_prices() -> list[Product]:
    products_and_prices: list[Product] = []
    name: str = ''
    price: int = 0
    discount: int = 0
    while input('Continue? (yes/no): ') == 'yes':
        name = input('Name: ')
        price = int(input('Price: '))
        ask_discount = input('It have discount? (yes/no): ') == 'yes'
        if ask_discount:
            discount = int(input('What discount?: '))
        products_and_prices.append(Product(name, price, discount))
    return products_and_prices


def apply_iva(products: list[Product]) -> list[Product]:
    iva: float = 1.21
    for product in products:
        product.price *= iva
    return products


def apply_discount(products: list[Product]) -> list[Product]:
    for product in products:
        product.price *= ((100 - product.discount) / 100)
    return products


def print_ticket(products: list[Product]) -> None:
    total_price: float = 0
    for product in products:
        total_price += product.price
        print(f'{product.name}: {product.price}€')
    print(f'Total price: {total_price}')
