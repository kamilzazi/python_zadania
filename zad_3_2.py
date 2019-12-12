"""Zadanie 3.2 | Miesiące
​
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
​
Logikę obliczania liczby dni wydziel do osobnej funkcji.
​
**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
​
**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie. """


# **Wersja A**
# def ile_dni_ma_miesiac(jaki_miesiac: str) -> int:
#     miesiace = {'styczen': 31, 'luty': 28, 'marzec': 31, 'kwiecien': 30, 'maj': 31, 'czerwiec': 30, 'lipiec': 31,
#                 'sierpien': 31, 'wrzesien': 30, 'pazdziernik': 31, 'listopad': 30, 'grudzien': 31}
#     for miesiac in miesiace:
#         if miesiac == jaki_miesiac:
#             wynik = miesiace[miesiac]
#     return wynik
#
#
# def opakowywacz_miesiaca(jaki_miesiac, wynik):
#     return f'{jaki_miesiac.capitalize()} ma {wynik} dni'
#
#
# miesiac_uzytkownika = input('Podaj miesiąc: ')
# print(opakowywacz_miesiaca(miesiac_uzytkownika, ile_dni_ma_miesiac(miesiac_uzytkownika)))


# **Wersja B (trudniejsza)**
# Jeżeli użytkownik poda luty-zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie. """


def ile_dni(miesiac_uzytkownika: str) -> int:
    miesiace = {'styczen': 31, 'marzec': 31, 'kwiecien': 30, 'maj': 31, 'czerwiec': 30, 'lipiec': 31,
                     'sierpien': 31, 'wrzesien': 30, 'pazdziernik': 31, 'listopad': 30, 'grudzien': 31}
    if miesiac_uzytkownika == 'luty':
        ktory_rok = int(input('O luty w którym roku Ci chodzi?: '))
        if ktory_rok % 4 == 0 and ktory_rok % 100 != 0 or ktory_rok % 400 == 0:
            # https://pl.wikipedia.org/wiki/Rok_przest%C4%99pny
            slownik_miesiac = {'miesiac1': 'luty', 'dni': 29, 'w_ktorym_roku': ktory_rok}
            return slownik_miesiac
        else:
            slownik_miesiac = {'miesiac1': 'luty', 'dni': 28, 'w_ktorym_roku': ktory_rok}
            return slownik_miesiac
    else:
        for miesiac in miesiace:
            if miesiac == miesiac_uzytkownika:
                slownik_miesiac = {'miesiac1': miesiac, 'dni': miesiace[miesiac] }
                return slownik_miesiac


def wrapper(mies):
    if mies['miesiac1'] != 'luty':
        print(f"{mies['miesiac1']} ma {mies['dni']} dni.")
    else:
        print(f'{mies["miesiac1"]} w {mies["w_ktorym_roku"]} roku ma {mies["dni"]} dni.')


miesiac_uzytkownika = input("Podaj miesiac: ")
wrapper(ile_dni(miesiac_uzytkownika))
