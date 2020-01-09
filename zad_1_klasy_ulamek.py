"""1. Napisz jak najwygodniejszą w użyciu klasę Ulamek. Z niezbędnych funkcjonalności:
- wypisywanie (print(ulamek))
- stworzenie ułamka z zerowym mianownikiem powinno być niemożliwe (wyjątek przy próbie ustawienia na 0)
- jak najwięcej operatorów arytmetycznych. W szczególności:
        +, -(również __neg__()), *, /, +=, -=, *=, /= działające zarówno
    dla działań z innymi ułamkami jak i z liczbami całkowitymi (int). Gdzie ma to sens operacje powinny działać
    nawet jeżeli po lewej stronie działania jest wartość niebędąca ułamkiem (np. 3 * ulamek)
- operatory logiczne: <, <=, >, >=, ==, != działające dla porówniań ułamka z ułamkiem, ułamka z intem i inta z ułamkiem
- ułamek po każdej operacji powinien być w postaci nieskracalnej
        (tzn. 1/4 + 1/4 powinno dać w wyniku ułamek 1/2 a nie 2/4)
"""

# from fractions import Fraction
# a = Fraction(1, 2)
# print(a)
# print(type(a))

# import fractions
# for n, d in [ (1, 2), (2, 4), (3, 6) ]:
#     f = fractions.Fraction(n, d)
#     print('%s/%s = %s' % (n, d, f))

from fractions import Fraction


class Ulamek(Fraction):
    def __init__(self, licz, mian):
        self.licz = licz
        self.mian = mian

    def ulamek(self):
        return Fraction(self.licz, self.mian)


x = Ulamek(2, 3)
y = Ulamek(1, 4)
z = Ulamek(2, 8)
# y = Ulamek(1, 0) #  nie jest możliwe, bo mianownik = 0
print(x.ulamek())
print(y.ulamek())
a = x + y
print(a)
b = x - y
print(b)
c = x * y
print(c)
d = x / y
print(d)
e = -x
print(e)
f = 3 * x
print(f)
g = x * 3
print(g)

#  <, <=, >, >=, ==, !=
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)
print(y == z)
print(x != y)
