"""Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
​
1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb,
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr) #podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

"""

import math
import pytest


# # 1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,############################################
# def stopy_na_metry(wartosc_w_stopach: int or float) -> int or float:
#     """Funkcka przelcza odległość wyrażoną w stopach na metry.
#     :param wartosc_w_stopach
#     :return:
#     """
#     if type(wartosc_w_stopach) is not float and type(wartosc_w_stopach) is not int or wartosc_w_stopach < 0:
#         raise ValueError("Wartość musi być większa lub równa 0, oraz musi być intem lub floatem")
#
#     wynik = wartosc_w_stopach * 0.3048
#     print(f'stopy: {wartosc_w_stopach} / metry: {wynik}')
#     return wynik
#
#
# stopy_na_metry(5)
# stopy_na_metry(5.4)
#
#
# def test_inne_typy1():
#     with pytest.raises(ValueError):
#         stopy_na_metry(-4)
#         stopy_na_metry('ania')
#         stopy_na_metry(-1234)
#
#
# def test_liczb_nieujemnych():
#     assert stopy_na_metry(1) == 0.3048
#     assert stopy_na_metry(0) == 0
#
#
# # 2. `max` - zwraca większą z dwóch liczb,###################################################################
# def maks(liczba1: int or float, liczba2: int or float) -> int or float:
#     """Zwraca większą z dwóch liczb
#     :param liczba1
#     :param liczba2
#     :return:
#     """
#     if type(liczba1) is not int and type(liczba1) is not float \
#             or type(liczba2) is not int and type(liczba2) is not float:
#         raise TypeError("Liczby muszą być intem lub floatem")
#     if liczba1 > liczba2:
#         print(f"Liczba {liczba1} jest większa niż liczba {liczba2}.")
#         return liczba1
#     elif liczba1 < liczba2:
#         print(f"Liczba {liczba2} jest większa niż liczba {liczba1}.")
#         return liczba2
#     else:
#         print('Podałeś takie same liczby!')
#
#
# maks(-4, 2)
# maks(5.7, 4)
# maks(76.4, 4.9)
#
#
# def test_inne_typy():
#     with pytest.raises(TypeError):
#         maks('l', 3)
#         maks('ala', 1)
#         maks(1, 'kot')
#
#
# def test_liczb_prawidlowych():
#     assert maks(2, 3) == 3
#     assert maks(-85, -8) == -8
#     assert maks(0, 89) == 89


# # 3. `srednia` - oblicza średnią z dwóch liczb,############################################################
# def srednia(x: int or float, y: int or float):
#     """Funkcja oblicza średnią z dwóch liczb.
#     :param x
#     :param y
#     :return:
#     """
#     if type(x) is not float and type(x) is not int:
#         raise TypeError("Każda z liczb musi być intel albo floatem")
#     wynik = (x + y) / 2
#     print(f'Średnia z wprowadzonych liczb jest równa {wynik}')
#     return wynik
#
#
# srednia(-5, 6.5)
#
#
# def test_nie_intow_nie_floatow():
#     with pytest.raises(TypeError):
#         srednia('ala', 1)
#         srednia(2, "ala")
#
#
# def test_liczb_odpowiednich():
#     assert srednia(3, 3) == 3
#     assert srednia(6, 8) == 7
#     assert srednia(2.5, 6.75) == 4.625


# # 4.`pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)####################################
# def pole_kola(promien: int or float) -> int or float:
#     """Funkcja oblicza pole koła z użyciem podanej wartosci promienia
#     :param promien
#     :return:
#     """
#
#     if type(promien) is not int and type(promien) is not float or promien <= 0:
#         raise ValueError("Wprowadzona wartość musi być dodatnia i być intem lub floatem")
#
#     pole = math.pi * promien ** 2
#     print(f'Pole koła wynosi {pole}')
#     return pole
#
#
# pole_kola(2)
# pole_kola(2.5)
#
# def test_innych_typow_liczb_niedodatnich():
#     with pytest.raises(ValueError):
#         pole_kola(-8)
#
#
# def test_innych_typow():
#     with pytest.raises(ValueError):
#         pole_kola("ala")
#
#
# def test_innych_typow1():
#     with pytest.raises(ValueError):
#         pole_kola("k")


# # `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.#####################
# def bmi(wzrost: int or float, waga: int or float) -> float:
#     """Funckaj oblciza współczynnik BMI dl apodanych parametrów:
#      wzrostu w metrach i wagi w kg
#      :param wzrost
#      :param waga
#      :return
#      """
#     if (type(wzrost) is not int and type(wzrost) is not float) or (type(waga) is not int \
#             and type(waga) is not float) or (wzrost <= 0 or waga <= 0):
#         raise ValueError("wzrost i waga muszą być większe od 0 i być intem lub floatem")
#     wynik = round(waga / wzrost ** 2, 1)
#     return wynik
#
#
# print(bmi(2, 3))
# print(bmi(2.3, 3))
# print(bmi(2, 3.4))
# print(bmi(2.8, 3.4))
#
#
# def test_ujemnych1():
#     with pytest.raises(ValueError):
#         bmi(-1, 2)
#         bmi(-5, -8)
#         bmi(5, -9)
#
#
# def test_nieliczb():
#     with pytest.raises(ValueError):
#         bmi(1, 'a')
#         bmi('b', 'a')
#         bmi('c', 6)
#
#
# def test_dobrychliczb():
#     assert bmi(1.9, 90) == 24.9
#     assert bmi(1.75, 84.5) == 27.6


# # 6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.#################
# def pole_trojkata(a: int or float, b: int or float, c: int or float) -> int or float:
#     """Funkcja oblicza pole trójkąta ze wzoru Herona z podanych trzech parametrów
#     :param a
#     :param b
#     :param c
#     :return
#     """
#     if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)) or not \
#             (isinstance(c, int) or isinstance(c, float)):
#         raise TypeError('Liczby muszą być intami lub floatami')
#     for liczba in (a, b, c):
#         if liczba <= 0:
#             raise ValueError('Liczby muszą być większe od 0')
#     if a + b <= c or b + c <= a or c + a <= b:
#         raise ValueError('''Warunek trójkąta nie jest spełniony.
#     Suma długości dwóch dowolnych boków musi być większa od długości trzeciego.''')
#     else:
#         p = 1 / 2 * (a + b + c)
#         pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
#         print(f'Pole trójkąta  wynosi {pole}')
#         return pole
#
#
# pole_trojkata(12, 15, 16)
#
#
# def test_zly_warunek_trojkata():
#     with pytest.raises(ValueError):
#         pole_trojkata(8, 5, 3)
#         pole_trojkata(150, 200, 500)
#
#
# def test_liczb_ujemnych():
#     with pytest.raises(ValueError):
#         pole_trojkata(-2, 3, 4)
#         pole_trojkata(4, -5, 6)
#         pole_trojkata(7, 8, -9)
#
#
# def test_nieliczb6():
#     with pytest.raises(TypeError):
#         pole_trojkata('ala', 1, 3)
#         pole_trojkata(3, 'bela', 5)
#         pole_trojkata('ala', 'bela', 'cela')


# # 7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile #########################################
# def kilometry_na_mile(kilometry: int or float) -> int or float:
#     if not (isinstance(kilometry, int) or isinstance(kilometry, float)):
#         raise TypeError("Wartość kilometrów musi być intem lub loatem.")
#     if kilometry <= 0:
#         raise ValueError("Wartość kilometrów musi być większa od 0")
#     mile = 0.62 * kilometry
#     return mile
#
#
# def test_kilometrow_dobrych():
#     assert kilometry_na_mile(2) == 1.24
#     assert kilometry_na_mile(8) == 4.96
#     assert kilometry_na_mile(0.25) == 0.155
#
#
# def test_kilometrow_nie_int():
#     with pytest.raises(TypeError):
#         kilometry_na_mile('a')
#         kilometry_na_mile((1, 2, 3), 2, 3)
#
#
# def test_kilometry_mniejsze_rowne_zero():
#     with pytest.raises(ValueError):
#         kilometry_na_mile(-8)
#         kilometry_na_mile(0)


# # 8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry #####################################
def mile_na_km(wartosc_mil: int or float) -> int or float:
    if not (isinstance(wartosc_mil, int) or isinstance(wartosc_mil, float)):
        raise TypeError("wartość musi być intem lub floatem")
    if wartosc_mil <= 0:
        raise ValueError("Wartosc musi byc wieksza od 0")
    wartosc_km = 1.61 * wartosc_mil
    return wartosc_km

print(mile_na_km(51))

def test_zwykle_liczby():
    assert mile_na_km(1) == 1.61
    assert mile_na_km(11) == 17.71


def test_liczby_niedodatnie_mile():
    with pytest.raises(ValueError):
        mile_na_km(-8)
        mile_na_km(0)


def test_inne_liczby_mile():
    with pytest.raises(TypeError):
        mile_na_km('a')
        mile_na_km((1, 2, 3), 4, 5)