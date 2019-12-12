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



def ile_dni_ma_miesiac(jaki_miesiac: str) -> int:
    miesiace = {'styczen': 31, 'luty': 28, 'marzec': 31, 'kwiecien': 30, 'maj': 31, 'czerwiec': 30, 'lipiec': 31,
                'sierpien': 31, 'wrzesien': 30, 'pazdziernik': 31, 'listopad': 30, 'grudzien': 31}
    for miesiac in miesiace:
        if miesiac == jaki_miesiac:
            wynik = miesiace[miesiac]
    return wynik


def opakowywacz_miesiaca(jaki_miesiac, wynik):
    return f'{jaki_miesiac.capitalize()} ma {wynik} dni'

jaki_miesiac = input('Podaj miesiąc: ')
print(opakowywacz_miesiaca(jaki_miesiac, ile_dni_ma_miesiac(jaki_miesiac)))
