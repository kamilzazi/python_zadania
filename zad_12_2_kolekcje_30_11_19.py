"""Napisz program, który posortuje liczby w liście przy wykorzystaniu
algorytmu "sortowanie przez wybieranie"."""


lista = [1500, 500, 2000, 400, 2100, 300]
posortowane = []

while lista != []:
    index_min = lista.index(min(lista))
    minimalna = lista.pop(index_min)
    posortowane.append(minimalna)

print(posortowane)




