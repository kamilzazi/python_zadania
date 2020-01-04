"""# Zadanie #12
Zaimplementuj klasy odpowiedzialne za różne typy promocji - opartą o stałą wartość i procent od wartości.
Promocje można dodawać do koszyka. Koszyk może mieć aktywnych wiele promocji.
Pamiętaj o obsłużeniu przypadku gdy wartość koszyka spadnie poniżej zera.
Przykład użycia:
basket = Basket()
discount = ValueDiscount(10.0)
basket.add_discount(discount)"""


class Product:
    def __init__(self, id, produkt, cena):
        self.id = id
        self.produkt = produkt
        self.cena = cena

    def __str__(self):
        return (f"B) ID: {self.id}, produkt: {self.produkt}, cena: {self.cena}")


class Basket:
    def __init__(self):
        self.koszyk = []

    def add_product(self, produkt: Product, liczba=1):
        for s in self.koszyk:
            if s["produkt"].id == produkt.id:
                s["liczba"] += liczba
                return
        slownik = {"produkt": produkt, "liczba": liczba}
        self.koszyk.append(slownik)

    def count_total_price(self):
        self.total_price = 0
        for s in self.koszyk:
            self.total_price += (s["produkt"].cena * s["liczba"])
        return self.total_price - self.discount

    def add_discount(self, discount1=0):
        self.discount = discount1
        return self.discount


class ValueDiscount:
    def __init__(self, discount1):
        self.discount = int(discount1)

    def return_discount(self):
        return self.discount


p1 = Product(1, "Woda", 3)
p2 = Product(2, "Chleb", 4)
p3 = Product(3, "Banany", 6)
x = Basket()
x.add_product(p1)
x.add_product(p2)
x.add_product(p3)
x.add_product(p1)
print(x.koszyk)
print(x.count_total_price())
discount = ValueDiscount(10).return_discount()
z = x.add_discount(discount)
print("X")
print(z)
# print(x.count_total_price())
# x.add_discount(dis)
