"""Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
​
1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb,
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
"""

import math
import pytest


# 1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
def stopy_na_metry(wartosc_w_stopach: int or float) -> int or float:
    """Funkcka przelcza odległość wyrażoną w stopach na metry.
    :param wartosc_w_stopach
    :return:
    """
    if wartosc_w_stopach < 0 or type(wartosc_w_stopach) is not float and type(wartosc_w_stopach) is not int:
        raise ValueError("Wartość musi być większa lub równa 0, oraz musi być intem lub floatem")

    wynik = wartosc_w_stopach * 0.3048
    print(f'stopy: {wartosc_w_stopach} / metry: {wynik}')
    return wynik


stopy_na_metry(5)
stopy_na_metry(5.4)


def test_inne_typy1():
    with pytest.raises(ValueError):
        stopy_na_metry(-4)
        stopy_na_metry('ania')
        stopy_na_metry(-1234)


def test_liczb_nieujemnych():
    assert stopy_na_metry(1) == 0.3048
    assert stopy_na_metry(0) == 0


# 2. `max` - zwraca większą z dwóch liczb,
def maks(liczba1: int or float, liczba2: int or float) -> int or float:
    """Zwraca większą z dwóch liczb
    :param liczba1
    :param liczba2
    :return:
    """
    if type(liczba1 or liczba2) is str:
        raise TypeError("Żadna z liczb nie może być stringiem")
    if liczba1 > liczba2:
        print(f"Liczba {liczba1} jest większa niż liczba {liczba2}.")
        return liczba1
    elif liczba1 < liczba2:
        print(f"Liczba {liczba2} jest większa niż liczba {liczba1}.")
        return liczba2
    else:
        print('Podałeś takie same liczby!')


maks(-4, 2)
maks(5.7, 4)
maks(76.4, 4.9)


def test_inne_typy():
    with pytest.raises(TypeError):
        maks('ala', 1)
        maks(1, 'kot')
        maks(1.554, 123)


def test_liczb_prawidlowych():
    assert maks(2, 3) == 3
    assert maks(-85, -8) == -8
    assert maks(0, 89) == 89


# ##3. `srednia` - oblicza średnią z dwóch liczb,
def srednia(x: int or float, y: int or float):
    """Funkcja oblicza średnią z dwóch liczb.
    :param x
    :param y
    :return:
    """
    if type(x) is not float and type(x) is not int:
        raise TypeError("Każda z liczb musi być intel albo floatem")
    wynik = (x + y) / 2
    print(f'Średnia z wprowadzonych liczb jest równa {wynik}')
    return wynik


srednia(-5, 6.5)


def test_nie_intow_nie_floatow():
    with pytest.raises(TypeError):
        srednia('ala', 1)
        srednia(2, "ala")


def test_liczb_odpowiednich():
    assert srednia(3, 3) == 3
    assert srednia(6, 8) == 7
    assert srednia(2.5, 6.75) == 4.625


# `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)

def pole_kola(promien: int or float):
    """Funkcja oblicza pole koła z użyciem podanej wartosci promienia
    :param promien
    :return:
    """

    if promien < 0 or type(promien) is not int and type(promien) is not float:
        raise ValueError("Wprowadzona wartość musi być dodatnia i być intem lub floatem")
    pole = math.pi * promien ** 2
    print(f'Pole koła wynosi {pole}')
    return pole


pole_kola(2)
pole_kola(2.5)


def test_innych_typow_liczb_niedodatnich():
    with pytest.raises(ValueError):
        pole_kola(-8)
        pole_kola('ala')
