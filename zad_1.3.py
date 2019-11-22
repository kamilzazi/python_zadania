"""
### Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)
​
Napisz trzy programy, które dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypiszą współczynnik BMI,
oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
Programy mają różnić się sposobem interakcji z użytkownikiem.
"""

# PROGRAM 1
wzrost = float(input('Podaj swój wzrost w cm: '))
waga = float(input('Podaj swoją wagę w kg: '))

BMI = waga / (wzrost/100) ** 2
print(f"Twoje BMI wynosi {BMI}.")

if BMI < 18.5:
    print("Masz niedowagę.")
elif 18.5 <= BMI < 25:
    print("Twoja waga jest prawidłowa.")
elif 25 <= BMI < 30:
    print("Masz nadwagę.")
else:
    print("Twój wskaźnik BMI wskazuje otyłość.")

# PROGRAM 2