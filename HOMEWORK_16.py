class Product:

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}, {self.price}'


class Order:

    def __init__(self):
        self.cart = []
        self.quantity = []

    def __iadd__(self, other: Product | tuple):
        if isinstance(other, Product):
            self.cart.append(other)
            self.quantity.append(1)
        elif isinstance(other, tuple):
            self.cart.append(other[0])
            self.quantity.append(other[1])
        else:
            raise TypeError
        return self

    def __iter__(self):
        return OrderIter(self.cart, self.quantity)

    def __str__(self):
        res = ''
        for item, count in self:
            res += f'{item}: {count} UAH\n'
        return res


class OrderIter:

    def __init__(self, cart, quantity):
        self.cart = cart
        self.quantity = quantity
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.cart):
            self.index += 1
            return self.cart[self.index - 1], self.quantity[self.index - 1]
        raise StopIteration


pr_1 = Product('Banana', 20)
pr_2 = Product('Orange', 25)
pr_3 = Product('Apple', 10)

order = Order()
order += pr_1
order += (pr_2, 2)
order += (pr_3, 0.5)

for item, count in order:
    print(item, count)

print(order)