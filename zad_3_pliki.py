"""# Zadanie  3
Napisz program wczytujący listę adresów email z pliku i tworzący nowy plik z odfiltrowaną zawartością.
Wejściowy plik może zawierać duplikaty adresów, ten sam adres pisany różną wielkością liter,
linie zawierające białe znaki oraz błędne adresy email (brak znaku `@` lub występuje on wiele razy).
Wynikowy plik powinien zawierać unikalne, posortowane, poprawne adresy email.
Przykład użycia:
$ python clean_emails.py emails.txt cleaned_emails.txt
"""

# przyda sie
# otworzyc plik, zczytac po nim
# https://docs.python.org/3/library/stdtypes.html
# Text Sequence Type — str
# zapoznac sie: String Methods
# metoda do usuwania bialych znakow z przodu i z tylu
# ile razy wystepuje dana sekwencja


lista = []
lista1 = []
lista2 = []
zbior = set()


with open('emails.txt') as plik:
    for x in plik:
        lista.append((x.lstrip()).rstrip("\n"))
    # print(lista)
    for x in lista:
        lista1.append(x.lower())
    # print(lista1)
    for x in lista1:
        if x.count("@") == 1:
            zbior.add(x)
    # print(zbior)
    for x in sorted(zbior):
        lista2.append(x)
    # print(lista2)

for x in lista2:
    print(x)
