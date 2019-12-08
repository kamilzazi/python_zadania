"""Napisz program, który posortuje liczby w liście przy wykorzystaniu
algorytmu "sortowanie przez wybieranie"."""


# lista = [1500, 500, 2000, 400, 2100, 300]
# posortowane = []
#
# while lista != []:
#     index_min = lista.index(min(lista))
#     minimalna = lista.pop(index_min)
#     posortowane.append(minimalna)
#
# print(posortowane)


lista = [400, 200, 600, 700, 800, 300]
wartosc_min = None
posortowane = []

while lista != []:
    for wartosc in lista:
        if wartosc_min is None or wartosc < wartosc_min:
            wartosc_min = wartosc
    posortowane.append(wartosc_min)
    lista.remove(wartosc_min)
    wartosc_min = None

print(posortowane)





