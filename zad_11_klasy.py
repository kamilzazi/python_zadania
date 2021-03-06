"""# Zadanie #11
Zaimplementuj klasy odpowiedzialne za tworzenie dokumentów w składni MarkDown.
Stwórz klasę bazową `Element` zawierającą podstawową implementację metody `render()` oraz kilka jej klas pochodnych.
Stwórz klasę `Document` umożliwiającą wyrenderowanie dodanych elementów.
Przykład użycia:
document = Document()
document.add_element(HeaderElement('Header'))
document.add_element(LinkElement('ABC', 'abc.com'))
document.add_element(Element('Simple'))
document.render()
Header
======
[ABC](http://abc.com)
Simple"""

# Prowadzącego:
# class Element:
#     def __init__(self, text):
#         self.text = text
#
#     def render(self):
#         return self.text
#
# class HeaderElement(Element):
#     def render(self):
#         text = super().render()
#         return text + "\n" + "=" * len(text)
#
# e = HeaderElement("Jakis napisadsfiuhdsjghfhdskjfhgkljhdsgjh")
# print(e.render())


# """# Zadanie #11
# Zaimplementuj klasy odpowiedzialne za tworzenie dokumentów w składni MarkDown.
# Stwórz klasę bazową `Element` zawierającą podstawową implementację metody `render()` oraz kilka jej klas pochodnych.
# Stwórz klasę `Document` umożliwiającą wyrenderowanie dodanych elementów.
# Przykład użycia:
# document = Document()
# document.add_element(HeaderElement('Header'))
# document.add_element(LinkElement('ABC', 'abc.com'))
# document.add_element(Element('Simple'))
# document.render()
# Header
# ======
# [ABC](http://abc.com)
# Simple"""


class Element:
    def __init__(self, tekst):
        self.tekst = tekst

    def __str__(self):
        return self.tekst

    def __repr__(self):
        return self.tekst

    def render(self):
        return self.tekst


class HeaderElement(Element):
    def render(self):
        tekst = super().render()
        return tekst + "\n" + "=" * len(tekst)


class LinkElement(Element):
    def render(self):
        tekst = super().render()
        return tekst


class Element(Element):
    pass


class Document:
    def __init__(self):
        self.wynik = ""

    def __str__(self):
        return self.wynik

    def add_element(self, tekst):
        self.wynik += str(tekst) + "\n"

    def rander(self):
        return self.wynik


doc = Document()
x = Element("Kamil")
y = x.render()
print(y)
z = HeaderElement(y)
print(z)
doc.add_element(z)
# doc.add_element(HeaderElement("Kamil Zazula, ul. Zielona 20, 22-680 Lubycza Królewska"))
# doc.add_element(HeaderElement("Kamil Zazula, ul. Popiełuszki 22/12, 35-328 Rzeszów"))
# doc.add_element(LinkElement('ABC'))
print(doc.rander())
