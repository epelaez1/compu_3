class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


def ask_products() -> list[Product]:
    list_products = []
    while input('Do you want to add another item: Yes or No ') == 'Yes':  # noqa: WPS421
        name_product = input('Write down the name of the product ')  # noqa: WPS421
        price_product = float(input('Write the price of the product with decimals '))  # noqa: WPS421
        product = Product(name_product, price_product)
        list_products.append(product)
    return list_products


def add_prices(list_products: list[Product]) -> float:
    list_prices = 0
    for cosas in list_products:
        list_prices = list_prices + cosas.price
    return list_prices


def ask_discount_ammount(have_discount: bool) -> float:
    if have_discount:
        total_discount = float(input('Write the discount percentaje: '))  # noqa: WPS421
    else:
        total_discount = 0
    return total_discount


def calculate_discount(total_discount: float) -> float:
    return 1 - total_discount / 100


def ask_discount() -> bool:
    have_discounts = input('Are there discounts?: Yes or No ')  # noqa: WPS421
    return have_discounts == 'Yes'


def apply_discount(discount: float, list_prices: float) -> float:
    price = list_prices
    return price * discount


def calculate_tax(price: float) -> float:
    return price * 1.21  # noqa: WPS432


def final_print(price: float, list_products: list[Product], discount: float) -> None:
    for cosas in list_products:
        print(cosas.name, ':', cosas.price)  # noqa: WPS421
    print('Tax : 21%')  # noqa: WPS421
    print('Price =', price, ' €')  # noqa: WPS421


def main() -> None:  # noqa:
    asking = ask_products()
    summatory = add_prices(asking)
    ask = ask_discount()
    amm = ask_discount_ammount(ask)
    calc_disc = calculate_discount(amm)
    apply = apply_discount(summatory, calc_disc)
    tax = calculate_tax(apply)
    final_print(tax, asking, calc_disc)


main()
