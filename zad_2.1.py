"""## 2. Pętle i struktury danych
​
### Zadanie 2.1 | Zagadka matematyczna
​
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
"""

##################################ROZWIĄZANIE NR 1, niżej jest kolejne

# import random
# a = random.randint(0, 100)
# b = random.randint(0, 100)
#
# print(f'Pierwsza liczba {a}')
# print(f'Druga liczba {b}')
#
# suma = int(input(f'Podaj sumę liczb {a} i {b}: '))
# if suma == a + b:
#     print("Zgadłeś!")
# else:
#     print('Szukaj dalej.')
# while a + b != suma:
#     suma = int(input(f'Podaj sumę liczb {a} i {b}: '))
#     if a + b == suma:
#         print("Zgadłeś!")
#     else:
#         print('Szukaj dalej.')
#
#
#
#
#############################################ROZWIĄZANIE NR 2
import random
a = random.randint(0, 100)
b = random.randint(0, 100)

print(f'Pierwsza liczba {a}')
print(f'Druga liczba {b}')

while a + b != int(input(f'Podaj sumę liczb {a} i {b}: ')):
    print('Podaj dobry wynik.')
print('Zgadłeś!')