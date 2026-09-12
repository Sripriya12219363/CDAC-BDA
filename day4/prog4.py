class ProductNotFoundError(Exception):
    pass


class OutOfStockError(Exception):
    pass


def process_order(catalog, order):
    for product_id, quantity in order.items():
        if product_id not in catalog:
            raise ProductNotFoundError(
                f"Product '{product_id}' not found in store catalog."
            )

        available_stock = catalog[product_id]["stock"]

        if quantity > available_stock:
            raise OutOfStockError(
                f"Product '{product_id}' is out of stock. Requested: {quantity}, Available: {available_stock}."
            )

    total = 0.0

    for product_id, quantity in order.items():
        catalog[product_id]["stock"] -= quantity
        total += catalog[product_id]["price"] * quantity

    return total


def main():
    catalog = {
        "P01": {"price": 10.0, "stock": 5},
        "P02": {"price": 20.0, "stock": 10}
    }

    try:
        total = process_order(catalog, {"P01": 2, "P02": 1})
        print("Total:", total)
        print(catalog)

        total = process_order(catalog, {"P01": 2, "P02": 15})
        print("Total:", total)

    except ProductNotFoundError as e:
        print(e)
    except OutOfStockError as e:
        print(e)

    print("P01 stock:", catalog["P01"]["stock"])


main()
