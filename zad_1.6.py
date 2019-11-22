"""### Zadanie 1.6 | Bilety (ok. 1 godz.)
​
Założenia:
	- 0-6   - wiek przedszkolny - cena biletu: 0
	- 7-17  - wiek szkolny      - cena biletu: 2.28
	- 18-64 - wiek dorosły      - cena biletu: 3.80
	- +65   - wiek emerytalny   - cena biletu: 1.90
​
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
​
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli."""

wiek = int(input('Ile masz lat? '))

if 0 <= wiek <= 6:
    print('Bilety są darmowe.')
else:
    ile_biletow = float(input('Ile biletów chcesz kupić? '))
    if 7 <= wiek <= 17:
        print(f'Za bilety musisz zapłacić {ile_biletow * 2.28} zł. ')
    elif 18 <= wiek <= 64:
        print(f'Za bilety musisz zapłacić {ile_biletow * 3.80} zł. ')
    else:
        print(f'Za bilety musisz zapłacić {ile_biletow * 1.90} zł. ')