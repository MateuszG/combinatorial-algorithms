"""
Algorytm 10
1) Wyznacz indeks 'i'.
2) Jeżeli i == 0, to brak następnika.
3) Jeżeli nie, to wyznacz indeks 'j' najmiejszego elementu, który jest większy
od T[i].
4) Zamień T[i] z T[j].
5) Odwróć podlistę i wypisz T
"""


def perm_nastepnik(n, T):
    T[0] = 0
    i = n - 1
    while T[i + 1] < T[i]:
        i = i - 1
    if i == 0:
        return None
    j = n
    while T[j] < T[i]:
        j = j - 1
    T[i], T[j] = T[j], T[i]

    p = [1 for _ in range(n + 2)]
    for h in range(i + 1, n + 1):
        p[h] = T[h]

    for h in range(i + 1, n + 1):
        T[h] = p[n + i + 1 - h]

    return T[1:]

unranks = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]

for unrank in unranks:
    print (perm_nastepnik(3, [[]] + unrank))

# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
# None

"""
Dla zadanej permutacji algorytm wyznacza jej bezpośredniego "następnika" w
uporządkowaniu leksykograficznym.
"""
