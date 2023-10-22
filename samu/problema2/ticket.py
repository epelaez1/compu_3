class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


def print_ticket() -> None:
    ...
    return None


def ask_products() -> list[Product]:
    list_products = []
    while input('Do you want to add another item: Yes or No ') == 'Yes':
        name_product = input('Write down the name of the product ')
        price_product = float(input('Write the price of the product with decimals '))
        product = Product(name_product, price_product)
        list_products.append(product)
    return list_products


def add_prices(list_products: list[Product]) -> float:
    list_prices = 0.0
    for item in list_products:
        list_prices = list_prices + item.price
    return list_prices


def calculate_discount(have_discount: bool) -> float:
    if have_discount:
        total_discount = float(input('Write the discount percentaje: '))
        discount = 1 - total_discount / 100
    else:
        discount = 1
    return discount


def ask_discount() -> bool:
    are_discounts = input('Are there discounts?: Yes or No ')
    return are_discounts == 'Yes'


def apply_discount(discount: float, list_prices: float) -> float:
    price = list_prices
    price = price * discount
    return price


def calculate_tax(price: float) -> float:
    price = price * 1.21
    return price


def final_print(price: float, list_products: list[Product], discount: float) -> None:
    for item in list_products:
        print(item.name, ':', item.price)
    print('Tax : 21%')
    print('Price =', price, ' €')
    return None


def main() -> None:
    asking = ask_products()
    sum = add_prices(asking)
    ask = ask_discount()
    calc_disc = calculate_discount(ask)
    apply = apply_discount(sum, calc_disc)
    tax = calculate_tax(apply)
    receipt = final_print(tax, asking, calc_disc)
    return None


run = main()
