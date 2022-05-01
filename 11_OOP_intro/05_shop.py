class Product():
    def __init__(self, name, size, cost):
        self.name = name
        self.size = size
        self.cost = cost

    def __repr__(self):
        return f'{self.name} | {self.size} | {self.cost} PLN'

class Shop():
    def __init__(self, products):
        self.products = products

    def show(self):
        print(self.products)

    def __repr__(self):
        shop_to_text = ''

        for prod in self.products:
            prod_to_text = Product.__repr__(prod)
            shop_to_text += '*' + prod_to_text + '\n'

        return shop_to_text

    def try_products(self,index):
        print(f'Przymierzam: {self.products[index]}')

p1 = Product('Spodnie 👖','L',90)
p2 = Product('Koszulka 👕','M',100)
p3 = Product('Buty 👟','38',120)


# zobaczyć, przymierzyć, kupić zwrócić
fashion_shop = Shop([p1,p2,p3])

# fashion_shop.show()
fashion_shop.try_products(2)

print(fashion_shop)