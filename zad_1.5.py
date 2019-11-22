"""### Zadanie 1.5 | Pole trójkąta (ok. 1 godz.)
​
Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
​
Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
​
Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
​
```
import math
​
x = math.sqrt(10)
```
"""

import math

a = int(input('Podaj pierwszy bok trójkąta a= '))
b = int(input('Podaj drugi bok trójkąta b= '))
c = int(input('Podaj trzeci bok trójkąta c= '))
p = (a + b + c) / 2

if a < b < c and a + b > c:
    print(f'Pole powierzchni trójkąta wynosi {math.sqrt(p * (p - a) * (p - b) * (p - c))}')
elif b < c < a and b + c > a:
    print(f'Pole powierzchni trójkąta wynosi {math.sqrt(p * (p - a) * (p - b) * (p - c))}')
elif c < a < b and c + a > b:
    print(f'Pole powierzchni trójkąta wynosi {math.sqrt(p * (p - a) * (p - b) * (p - c))}')
elif a < c < b and c + a > b:
    print(f'Pole powierzchni trójkąta wynosi {math.sqrt(p * (p - a) * (p - b) * (p - c))}')
elif b < a < c and c + a > b:
    print(f'Pole powierzchni trójkąta wynosi {math.sqrt(p * (p - a) * (p - b) * (p - c))}')
elif c < b < a and c + a > b:
    print(f'Pole powierzchni trójkąta wynosi {math.sqrt(p * (p - a) * (p - b) * (p - c))}')
else:
    print('Nieprawidłowe długości boków trójkąta.')
