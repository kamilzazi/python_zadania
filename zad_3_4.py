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

def crazy_case(napis: str) ->str:
    """
    Funkcja pobiera napis od użytkownika i zwraca go ze zmianą co drukiej litery na dużą.
    :param napis:
    :return:
    """
    nowy_napis = ''
    for i in range(0, len(napis)):
        if i % 2 == 0:
            litera = napis[i]
            nowy_napis += litera.upper()
        else:
            nowy_napis += napis[i]
    return nowy_napis


def jakis_napis():
    return 'ala ma kota, a kot ma alę'

print(crazy_case(jakis_napis()))