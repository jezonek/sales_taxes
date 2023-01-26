from sales_taxes.taxes import Collection, Product
from sales_taxes.utils import parse_one_line


def main():
    print("Welcome to Tax calculator!")
    collection = Collection([])
    obj_text = input("> ")
    while obj_text:
        parsed_quantity, parsed_name, parsed_price = parse_one_line(obj_text)
        product = Product(
            quantity=parsed_quantity, name=parsed_name, price_net=parsed_price
        )
        collection.add(product)
        obj_text = input("> ")

    for product in collection.objects:
        print(
            f"{product.quantity} {product.name}: {format(product.price_gross, '.2f')}"
        )
    print(f"Sales Taxes: {format(collection.tax(), '.2f')}")
    print(f"Total: {format(collection.price_gross(),'.2f')}")


if __name__ == "__main__":
    main()
