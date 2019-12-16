"""### Zadanie 3.4 | Dekorator
​
Napisz dekorator `crazy_case`, który co drugą literę w słowie będzie zamieniał na dużą.
​
```python
@crazy_case
def powiedz_ala():
    return 'Ala ma kota'

print(powiedz_ala()) # aLa mA KoTa
"""


def crazy_case(funkcja_do_udekorowania):
    """
    Funkcja pobiera napis od użytkownika i zwraca go ze zmianą co drukiej litery na dużą.
    :param napis:
    :return:
    """
    def wrapper(*args, **kwargs):
        wynik = funkcja_do_udekorowania(*args, **kwargs)
        nowy_napis = ''
        for i in range(0, len(wynik)):
            if i % 2 == 0:
                litera = wynik[i]
                nowy_napis += litera.upper()
            else:
                nowy_napis += wynik[i]
        return nowy_napis
    return wrapper


@crazy_case
def jakis_napis(arg = 'kota'):
    return f'ala ma {arg}, a kot ma alę'


print(jakis_napis())
# print(crazy_case(jakis_napis()))

