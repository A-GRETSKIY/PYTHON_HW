class Product:

    def __init__(self, title, price: int | float):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title} - {self.price}'


class Customer:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.name} - {self.phone}'


class Order:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.cart = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float):
        self.cart.append(product)
        self.quantities.append(quantity)

    def total_price(self):
        total = 0
        for i, item in enumerate(self.cart):
            total += item.price * self.quantities[i]
        return total

    def __str__(self):
        res = f'{self.customer}\n'

        for i, item in enumerate(self.cart):
            tmp = f'\t{item} UAH x {self.quantities[i]} = {self.quantities[i] * item.price}\n'
            res += tmp

        res += f'Total: {self.total_price()} UAH'

        return res


if __name__ == '__main__':  # if __name__ == '__main__': - стандартная точка входа в программу, отсюда начинает рабрту скрипт
    pr_1 = Product('apple', 20)
    pr_2 = Product('banana', 30)

    cust_1 = Customer('Oleh', '+380931111111')
    cust_2 = Customer('Ivan', '+380932222222')

    order_1 = Order(cust_1)
    order_2 = Order(cust_2)

    order_1.add_product(pr_1, 2)
    order_1.add_product(pr_2, 2)
    order_1.add_product(pr_1, 1)

    order_2.add_product(pr_1, 3)

    print(order_1)