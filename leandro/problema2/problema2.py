class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


def ask_product_name() -> str:
    return input("Product's name: ")  # noqa: WPS110, WPS421


def ask_product_price() -> float:
    return float(input("Product's price: "))  # noqa: WPS110, WPS421


def ask_products() -> list[Product]:
    products_list = []
    while input('do you want to add more? ').lower() == 'yes':  # noqa: WPS110, WPS421
        products_list.append(Product(ask_product_name(), ask_product_price()))
    return products_list


def sum_prices(products: list[Product]) -> float:
    return sum([product.price for product in products])


def apply_iva(ticket_price: float, list_products: list[Product]) -> float:
    iva = 1.21
    return sum_prices(list_products) * iva


def ask_discount() -> float:
    return float(input('Discount: '))  # noqa: WPS110, WPS421


def apply_discount(price_with_iva: float, discount: float) -> float:
    descuento = (100 - discount) / 100
    return price_with_iva * descuento


def print_ticket(products_list: list[Product], ticket_price: float, price_with_iva: float, final_price: float) -> None:
    for product in products_list:
        print(product.name, ' : ', product.price)  # noqa: WPS421
    print(f'total price : {ticket_price:.{2}f}€')  # noqa: WPS305, WPS421
    print(f'price with IVA : {price_with_iva:.{2}f}€')  # noqa: WPS305, WPS421
    print(f'price after discount : {final_price:.{2}f}€')  # noqa: WPS305, WPS421


def main() -> None:
    list_products = ask_products()
    ticket_price = sum_prices(list_products)
    price_with_iva = apply_iva(ticket_price, list_products)
    descuento = ask_discount()
    final_price = apply_discount(price_with_iva, descuento)
    print_ticket(list_products, ticket_price, price_with_iva, final_price)
