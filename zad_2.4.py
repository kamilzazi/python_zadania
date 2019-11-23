"""### Zadanie 2.4 | Zgadnij liczbę z zakresu
​
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
​
Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją i pełni w informatyce bardzo ważną rolę.
Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024)."""

import random
wylosowana = random.randint(0, 1000)
print(wylosowana)
licznik = 0
while True:
    wprowadzona = int(input('Wprowadź liczbę: '))
    licznik += 1
    if wprowadzona != wylosowana:
        if wprowadzona > wylosowana:
            print('Za duża. ')
        else:
            print('Za mała.')
    else:
        print(f"Brawo! Zgadłeś liczbę po {licznik} próbie.")

        break