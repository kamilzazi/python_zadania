"""### Zadanie 2.3
​
Napisz program, który odczytuje od użytkownika wiele liczb.
​
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
​
- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum
"""


liczby = []
print('Wpisz liczby. Jeśli chcesz zakończyć wpisywanie naciśnij dowolny przycisk różny niż cyfra.')
while True :
    x = input('Podaj liczbę: ')
    if x.isdigit() == True:
        liczby.append(int(x))
    else:
        print(f'Wprowadziłeś liczby: {liczby}')
        break
ilosc = len(liczby)
suma = sum(liczby)
print(f'Liczba podanych liczby wynosi {ilosc}.')
print(f'Suma wprowadzonych liczb wynosi {suma}.')
print(f'Średnia wprowadzonych liczb wynosi {suma / ilosc}.')
index_min = None
index_max = None
for index in liczby:
    if index_min is None or index_min > index:
        index_min = index
    elif index_max is None or index_max < index:
        index_max = index
print(f'Minimalna wprowadzona liczba to: {index_min}.')
print(f'Maksymalna wprowadzona liczba to: {index_max}.')

