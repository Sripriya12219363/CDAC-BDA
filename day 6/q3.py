class PriceAmount:
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency.upper()
    def __str__(self):
        return f"{self.currency} {self.value:.2f}"
    def __repr__(self):
        return f"PriceAmount(value={self.value:.2f}, currency='{self.currency}')"
    def __add__(self, other):
        if not isinstance(other, PriceAmount):
            raise TypeError("Can only add PriceAmount objects.")
        if self.currency != other.currency:
            raise ValueError(
                f"Cannot add price amounts with different currencies: "
                f"'{self.currency}' and '{other.currency}'."
            )
        return PriceAmount(self.value + other.value, self.currency)
    def __eq__(self, other):
        if not isinstance(other, PriceAmount):
            return False
        return self.currency == other.currency and self.value == other.value
def main():
    p1 = PriceAmount(19.99, "usd")
    p2 = PriceAmount(10.01, "USD")
    p3 = PriceAmount(15.00, "EUR")
    print(str(p1))
    print(repr(p1))
    total = p1 + p2
    print(str(total))
    print(p1 == PriceAmount(19.99, "USD"))
    try:
        bad_addition = p1 + p3
    except ValueError as e:
        print(e)

main()