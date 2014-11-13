"""
Algorytm 10
1) Przypisz 'i' wartość n - 1.
2) Dopóki 'i' dla T[i + 1] jest mniejsze od T[i], to zmniejsz 'i' o 1.
3) Jeżeli i == 0, to brak następnika.
4) Jeżeli nie, to przypisz 'j' wartośc 'n'.
5) Dopóki 'j' dla T[j] jest mniejsze od T[i], to zmniejsz 'j' o 1.
6) Zamień T[i] z T[j].
7) Odwróć podlistę przypisując p[h] wartość T[h] (i + 1...n), następnie
przypisz T[h] wartość p[n + i + 1 - h] (i + 1...n), wypisz T.
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
