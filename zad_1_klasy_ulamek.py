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