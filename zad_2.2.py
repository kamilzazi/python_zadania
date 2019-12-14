"""### Zadanie 2.2 | Choinka
​
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
Np. dla parametru 3 powinno się wypisać:
```
    *
  * * *
* * * * *
```
"""


# licznik = 0
# x = int(input('Podaj liczbę całkowitą: '))
# gwiazda = '* '
# gwiazdka = '* '
# while licznik != x:
#     wyrownanie = x ** 3
#     print(f'{gwiazdka}'.center(wyrownanie), end='')
#     gwiazdka = gwiazdka + 2 * gwiazda
#     licznik += 1
#     print()





licznik = 0
x = int(input('Podaj liczbę całkowitą: '))
gwiazda = '* '
gwiazdka = '* '
while licznik != x:
    print(f'{gwiazdka:^40}', end='')
    gwiazdka = gwiazdka + 2 * gwiazda
    licznik += 1
    print()
