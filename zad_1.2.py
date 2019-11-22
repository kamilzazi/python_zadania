"""
### Zadanie 1.2 | Buty do szewca (ok. 1 godz.)
​
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.).
Ma też podać, ile dni będzie trwała naprawa.
​
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci wygodniej, możesz założyć,
że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.
"""

do_szewca = int(input("Kiedy oddałeś buty do szewca? \nWpisz cyfrę odpowiadającą dniowi tygodnia: \n1-poniedziałek, 2-wtorek, 3-środa, 4-czwartek, 5-piątek, 6-sobota, 7-niedziela "))
czas_naprawy = int(input("Ile dni potrwa naprawa? "))
if czas_naprawy > 7:
    print("Naprawa nie może być dłuższa niż 7 dni.")
else:
    if do_szewca + czas_naprawy == 2:
        print("Odbiór we wtorek.")
    elif do_szewca + czas_naprawy == 3:
        print("Odbiór w środę.")
    elif do_szewca + czas_naprawy == 4:
        print("Odbiór w czwarte.k")
    elif do_szewca + czas_naprawy == 5:
        print("Odbiór w piątek.")
    elif do_szewca + czas_naprawy == 6:
        print("Odbiór w sobotę.")
    elif do_szewca + czas_naprawy == 7:
        print("Odbiór w niedzielę.")
    elif do_szewca + czas_naprawy == 8:
        print("Odbiór w poniedziałek.")
    if do_szewca + czas_naprawy == 9:
        print("Odbiór we wtorek.")
    elif do_szewca + czas_naprawy == 10:
        print("Odbiór w środę.")
    elif do_szewca + czas_naprawy == 11:
        print("Odbiór w czwartek.")
    elif do_szewca + czas_naprawy == 12:
        print("Odbiór w piątek.")
    elif do_szewca + czas_naprawy == 13:
        print("Odbiór w sobotę.")
    elif do_szewca + czas_naprawy == 14:
        print("Odbiór w niedzielę.")