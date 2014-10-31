"""
Algorytm 19

Standardowe podzialy liczb
Nieuporządkowanym (standardowym) podziałem liczby 'n' na 'k' dodatnich
skladników nazywamy każde przedstawienie liczby 'n' w postaci sumy
n = a[1] + a[2] + ... + a[k] gdzie a[1] ≥ a[2] ≥ ... ≥ a[k] ≥ 1

Konstrukcja algorytmu generującego wszystkie podziały standardowe dla zadanych
parametrów 'n' i 'k'
"""


import pprint
pp = pprint.PrettyPrinter(indent=4)


def liczba_podzial(n, k):
    P = [[0 for _ in range(1, n + 1)] for _ in range(1, n + 2)]
    P[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, min(i, k + 1)):

            if i < 2 * j:
                P[i][j] = P[i-1][j-1]
            else:
                P[i][j] = P[i-1][j-1] + P[i-j][j]

    return P


pp.pprint(liczba_podzial(7, 7))
# [   [0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0],
#     [0, 1, 2, 1, 1, 0, 0],
#     [0, 1, 2, 2, 1, 1, 0],
#     [0, 1, 3, 3, 2, 1, 1]]
