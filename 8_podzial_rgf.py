# -*- coding: utf-8 -*-
"""
Algorytm 16
Procedura wyznaczająca z zadanego podzialu zbioru {1, 2, . . . , n}
na 'k' bloków {B 1 , . . . , B[k]} odpowiadająca mu funkcje
(f[1], . . . , f[n]) RGF.

Dla danego elementu 'j' (zaczynamy od j = 1) szukamy numeru
bloku zawierającego ten element (drugi while) a następnie wszystkim składowym z
indeksami równymi elementom należącym do tego bloku nadajemy numer bloku
(instrukcja for each).

Czyność tę powtarzamy 'k' razy biorąc pod uwage kolejny element 'j' zbioru,
dla którego składowa f[j] jest jeszcze równa zero. W tym celu przed wejściem
do głównej pętli wszystkie składowe szukanej funkcji RGF muszą zostać
wyzerowane.
"""


def not_in(j, h, B):
    b = True
    for i, _ in enumerate(B[h]):
        if B[h][i] == j:
            b = False
    return b


def podzial_rgf(n, B):
    F = [0 for _ in range(n)]
    j = 1

    while F[j] != 0:
        j = j + 1
    h = 1

    while not_in(j, h, B) and len(B) <= h + 1:
        h = h + 1

    for i, g in enumerate(B[h]):
        F[B[h][i] - 1] = h
    return F

values = [
    [[1, 2, 3, 4]],
    [[1, 2, 3], [4]],
    [[1, 2, 4], [3]],
    [[1, 2], [3, 4]],
    [[1, 3, 4], [2]],
    [[1, 2], [3], [4]],
    [[1], [2], [4], [3]]
]

for val in values:
    val.reverse()
    val.append([])
    val.reverse()
    print (podzial_rgf(4, val), end=' ')
    print (val[1:])
# [1, 1, 1, 1] [[1, 2, 3, 4]]
# [1, 1, 1, 0] [[1, 2, 3], [4]]
# [1, 1, 0, 1] [[1, 2, 4], [3]]
# [1, 1, 0, 0] [[1, 2], [3, 4]]
# [1, 0, 1, 1] [[1, 3, 4], [2]]
# [1, 1, 0, 0] [[1, 2], [3], [4]]
# [1, 0, 0, 0] [[1], [2], [4], [3]]
