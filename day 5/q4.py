def process_dataset(dataset):
    d = []
    for item in dataset:
        prod = item[0]
        price = float(item[1].split(":")[1])
        rating = float(item[2].split(":")[1])
        d.append((prod, price, rating))
    filtered = filter(lambda x: x[1] <= 1000.0, d)
    result = map(
        lambda x: {
            "product": x[0],
            "price": x[1],
            "score": x[2]
        },
        filtered
    )
    res = list(result)
    res = sorted(res, key=lambda x: x["score"], reverse=True)
    return res
def main():

    data_input = [
        ("Laptop", "Price: 1200", "Rating: 4.8"),
        ("Phone", "Price: 800", "Rating: 4.5"),
        ("Mouse", "Price: 25", "Rating: 4.7"),
        ("Charger", "Price: 15", "Rating: 4.2")
    ]
    result = process_dataset(data_input)
    print(result)

main()