"""
Algorytm 20 - Podzial sprzężony
Aby wygenerować wszystkie standardowe podziały liczby 'n' na 'k' składników
wystarczy wygenerować podziały liczby 'n' o największym składniku 'k' i
w każdym przypadku wyznaczyć podział sprzężony.

Procedura, któora dla danego podziału (a[1], a[2], . . . , a[m]) wyznacza
podział do niego sprzężony.

b = k
"""


def podzial_sprzezony(a):
    """Algorytm 20"""
    a = [[]] + a
    b = [1 for _ in range(a[1] + 1)]

    for j in range(2, len(a)):
        for i in range(1, a[j] + 1):
            b[i] = b[i] + 1
    return b[1:]

podzialy = [
    [1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1],
    [2, 2, 1, 1, 1],
    [2, 2, 2, 1],
    [3, 1, 1, 1, 1],
    [3, 2, 1, 1],
    [3, 2, 2],
    [3, 3, 1],
    [4, 1, 1, 1],
    [4, 2, 1],
    [4, 3],
    [5, 1, 1],
    [5, 2],
    [6, 1],
    [7]
]
for podzial in podzialy:
    print (podzial_sprzezony(podzial))
# [7]
# [6, 1]
# [5, 2]
# [4, 3]
# [5, 1, 1]
# [4, 2, 1]
# [3, 3, 1]
# [3, 2, 2]
# [4, 1, 1, 1]
# [3, 2, 1, 1]
# [2, 2, 2, 1]
# [3, 1, 1, 1, 1]
# [2, 2, 1, 1, 1]
# [2, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 1]
