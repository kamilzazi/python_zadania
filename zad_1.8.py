"""
### Zadanie 1.8 | Kalkulator lat psich (ok. 0,5 godz.)
​
Zakładamy, że 1 ludzki rok, to 5 lat psich.
​
Za pomocą konsoli wczytaj imię i wiek psa.
​
Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
​
Przykład:
Podaj imię psa - Burek
Podaj wiek psa - 3
​
Gdyby Burek był człowiekiem, miałby 15 lat.
"""

imie = input('Podaj imię psa: ')
wiek = int(input('Podaj wiek psa: '))

print(f'Gdyby {imie} był człowiekiem, miałby {wiek * 5} lat. ')