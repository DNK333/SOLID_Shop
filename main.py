class Product:
    def __init__(self, name, price, quantity):
        if not name.strip():
            raise ValueError("Название товара не может быть пустым")
        if price <= 0:
            raise ValueError("Цена должна быть больше нуля")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.name = name
        self.price = price
        self.quantity = quantity


class ProductDatabase:
    def __init__(self):
        self.products = []

    def save(self, product):
        self.products.append(product)

    def get_all(self):
        return list(self.products)


class ProductInfoPrinter:
    def show(self, product):
        print(f"Товар: {product.name}")
        print(f"Цена: {product.price:.2f} KZT")
        print(f"Количество: {product.quantity}")


class PaymentMethod:
    name = "Способ оплаты"

    def pay(self, amount):
        raise NotImplementedError("Способ оплаты должен реализовать метод pay")

    @staticmethod
    def _validate_amount(amount):
        if amount <= 0:
            raise ValueError("Сумма оплаты должна быть больше нуля")


class KaspiPayment(PaymentMethod):
    name = "Kaspi"

    def pay(self, amount):
        self._validate_amount(amount)
        print(f"Оплата через {self.name}: {amount:.2f} KZT")
        return True


class BankCardPayment(PaymentMethod):
    name = "Банковская карта"

    def pay(self, amount):
        self._validate_amount(amount)
        print(f"Оплата через {self.name}: {amount:.2f} KZT")
        return True


class Checkout:
    def process_payment(self, payment_method, amount):
        return payment_method.pay(amount)


def main():
    product = Product("Наушники", 12990.00, 5)

    database = ProductDatabase()
    database.save(product)

    printer = ProductInfoPrinter()
    printer.show(database.get_all()[0])

    checkout = Checkout()
    checkout.process_payment(KaspiPayment(), product.price)
    checkout.process_payment(BankCardPayment(), product.price)


if __name__ == "__main__":
    main()
