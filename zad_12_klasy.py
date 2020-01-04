"""# Zadanie #12
Zaimplementuj klasy odpowiedzialne za różne typy promocji - opartą o stałą wartość i procent od wartości.
Promocje można dodawać do koszyka. Koszyk może mieć aktywnych wiele promocji.
Pamiętaj o obsłużeniu przypadku gdy wartość koszyka spadnie poniżej zera.
Przykład użycia:
basket = Basket()
discount = ValueDiscount(10.0)
basket.add_discount(discount)"""

class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"{self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN")

    def __str__(self):
        return f"Nazwa: {self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN"

    def __repr__(self):
        return f"<Product ID: {self.id}>"

class Basket:
    def __init__(self):
        self.zawartosc = []
        self.suma = 0

    def add_product(self, p: Product, ilosc: int = 1):
        for s in self.zawartosc:
            if s["produkt"].id == p.id:
                s["ilosc"] += ilosc
                return
        # jeśli tu dojdziemy to znaczy, ze na liscie nie ma jeszcze takiego produktu
        slownik = {"produkt": p, "ilosc": ilosc}
        self.zawartosc.append(slownik)


    def add_discount(self, discount):
        if self.suma > 0:
            for slow in self.zawartosc:
                self.suma += slow["produkt"].cena * slow["ilosc"]
            return self.suma - discount


    def count_total_price(self):
        return self.suma


class ValueDiscount:
    def __init__(self, discount):
        self.discount = discount

    def __float__(self):
        return self.discount





p1 = Product(1, "Woda", 3)
p2 = Product(2, "Chleb", 4)
p3 = Product(3, "Banany", 6)
x = Basket()
x.add_product(p1)
x.add_product(p2)
x.add_product(p3)
x.add_product(p1)
print(x.zawartosc)
print(x.count_total_price())
discount = ValueDiscount(10)
x.add_discount(discount)
print(x.count_total_price())