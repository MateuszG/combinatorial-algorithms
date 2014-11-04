"""
Algorytm 11
Algorytm:
1) Dla każdego j, zwiększamy rangę 'r' o wartość p[j] + 1 pomnożoną przez
silnie(n - j).
2) Następnie iterujemy raz jeszcze za pomocą 'i'.
3) Jeśli p[i] > p[j] to zmniejszamy wartość p[i] o jeden.

"""


def silnia(n):
    return n * silnia(n-1) if n > 1 else 1


def perm_rank(n, T):
    r = 0
    for j in range(1, n):
        r = r + (T[j] - 1) * silnia(n - j)

        for i in range(j + 1, n):
            if T[i] > T[j]:
                T[i] = T[i] - 1
    return r

unranks = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
]

for unrank in unranks:
    print (perm_rank(3, [[]] + unrank))
# 0
# 1
# 2
# 3
# 4
# 5
