"""### Zadanie 3.3 | Operacje na listach

Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie
operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```

- `suma(liczby)` - zwraca sumę liczb z listy `liczby`
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby`
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`;
    zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`;
    zwraca `None`, jeśli takiej liczby tam nie ma
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`,
    jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma"""


import pytest


# - `suma(liczby)` - zwraca sumę liczb z listy `liczby`
def suma(liczby: list) -> int:
    """
    Funkcja zwraca sumę liczb z listy liczby
    :param liczby:
    :return:
    """
    if not isinstance(liczby, list):
        raise TypeError("Nie podałeś listy!")
    return sum(liczby)


suma1 = lambda liczby: sum(liczby)


liczby = [50, 40, 30, 10, 60, 50]
print(suma1(liczby))
print("@" * 120)
wynik = suma(liczby)
print(wynik)


def test_lista_dobra():
    assert suma([10, 20]) == 30
    assert suma([-10, 10, -10, 10]) == 0


def test_nie_list():
    with pytest.raises(TypeError):
        suma({'a': 1, 'b': 2, 'c': 3})
        suma((1, 2, (34, 56), 60))
        suma({1, 2, 3, 4, 5})


# - `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
def srednia(liczby: list) -> float:
    """
    Funkcja zwraca średnią z liczb wprowadzonych w liście
    :param liczby:
    :return:
    """
    if not (isinstance(liczby, list)):
        raise TypeError("Nie podałeś listy!")
    return sum(liczby) / len(liczby)


srednia1 = lambda liczby: sum(liczby) / len(liczby)


liczby = [10, 20, 30, 40]


print(srednia1(liczby))
print("@" * 120)
print(srednia(liczby))


def test_liczby_dobre():
    assert srednia([10, 20, 35, 40]) == 26.25
    assert srednia([10, 20, 30, 40]) == 25.0


def test_nie_list1():
    with pytest.raises(TypeError):
        srednia((12, 3, 46, 78))
        srednia({12, 13, 14, 15, 16})
        srednia(('ala', 'kot', 'pat'))


# - `max(liczby)` – zwraca największą wartość z listy `liczby`
def maksymalna(liczby: list) -> int or float:
    """
    Zwraca największą wartość z podanej listy
    :param liczby:
    :return:
    """
    return max(liczby)


liczby = [10, 20, 50, 40]
print(maksymalna(liczby))


# - `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
def roznica_max_min(liczby: list) -> int or float:
    """
    Zwraca rożnicę między największą a najmniejszą liczbą w liście. Jeśli lista jest pusta lub ma tylko jeden element
    to zwraca 0.
    :param liczby:
    :return:
    """
    if not liczby:
        return 0

    return max(liczby) - min(liczby)


liczby = [10, 80, 30, 40]
liczby1 = []
liczby2 = [20]
print(roznica_max_min(liczby))
print(roznica_max_min(liczby1))
print(roznica_max_min(liczby2))


# - `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
def wypisz_wieksze(liczby: list, x: int or float) -> int or float:
    """
    Funkcja wypisuje liczby z listy większe niż liczba podana przes użytkownika.
    :param liczby:
    :param x:
    :return:
    """
    nowa_lista = []
    for i in liczby:
        if i > x:
            nowa_lista.append(i)
    return nowa_lista


liczby = [12, 64, 27, 9656, 345, 133, 11, 9, 6, 2345, 6]
print(wypisz_wieksze(liczby, 25))


# - `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`;
#     zwraca `None`, jeśli takiej liczby tam nie ma
def pierwsza_wieksza(liczby: list, x: int or float) -> int or float:
    for i in liczby:
        if i <= x:
            continue
        return i


liczby = [12, 64, 27, 96, 345, 133, 11, 9, 6, 2345, 6]
print('#' * 60)
print(pierwsza_wieksza(liczby, 200))
print(pierwsza_wieksza(liczby, 2500))asw3222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222q1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`]\







# - `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
# - `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
# - `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
# - `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`;
#     zwraca `None`, jeśli takiej liczby tam nie ma
# - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`,
#     jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
