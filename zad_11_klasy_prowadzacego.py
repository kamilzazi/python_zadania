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
