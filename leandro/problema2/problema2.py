class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


def ask_product_name() -> str:
    return input("Product's name: ")


def ask_product_price() -> float:
    return float(input("Product's price: "))


def ask_products() -> list[Product]:
    products_list = []
    while input("do you want to add more? ").lower() == "yes":
        products_list.append(Product(ask_product_name(), ask_product_price()))
    return products_list


def sum_prices(products: list[Product]) -> float:
    ticket_price: float = 0
    for product in products:
        ticket_price += product.price
    return ticket_price


def apply_iva(ticket_price: float, list_products: list[Product]) -> float:
    return sum_prices(list_products) * 1.21


def ask_discount() -> float:
    return float(input('Discount: '))


def apply_discount(price_with_iva: float, discount: float) -> float:
    descuento = (100 - discount) / 100
    return price_with_iva * descuento

def print_ticket(products_list: list[Product], ticket_price, price_with_iva, final_price) -> None:
    for product in products_list:
        print(product.name, " : ", product.price)
    print(f"total price : {ticket_price:.{2}f}€")
    print(f"price with IVA : {price_with_iva:.{2}f}€")
    print(f"price after discount : {final_price:.{2}f}€")

def main():
    list_products = ask_products()
    ticket_price = sum_prices(list_products)
    price_with_iva = apply_iva(ticket_price, list_products)
    descuento = ask_discount()
    final_price = apply_discount(price_with_iva, descuento)
    print_ticket(list_products, ticket_price, price_with_iva, final_price)

main()

