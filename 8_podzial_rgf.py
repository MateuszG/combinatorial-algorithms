"""
Algorytm 16
1) Dla danego elementu 'j' (zaczynamy od j = 1) szukamy numeru bloku
zawierającego ten element (drugi while).
2) Następnie wszystkim składowym z indeksami równymi elementom należącym do
tego bloku nadajemy numer bloku (instrukcja for each).
3) Czyność tę powtarzamy 'k' razy biorąc pod uwage kolejny element 'j' zbioru,
dla którego składowa f[j] jest jeszcze równa zero.
"""


def not_in(j, h, B):
    b = False

    for i, _ in enumerate(B[h]):
        if B[h][i] == j:
            b = True
    return b


def podzial_rgf(n, B):
    F = [0 for _ in range(n + 1)]
    j = 1
    k = len(B)
    for i in range(1, k):

        while F[j] != 0:
            j = j + 1
        h = 1

        while j not in B[h]:
            h = h + 1

        for g in B[h]:
            F[g] = h

    return F[1:]  # Exclude first element

values = [
    [[1, 2, 3, 4]],
    [[1, 2, 3], [4]],
    [[1, 2, 4], [3]],
    [[1, 2], [3, 4]],
    [[1, 2], [3], [4]],
    [[1, 3, 4], [2]],
    [[1, 3], [2, 4]],
    [[1, 3], [2], [4]],
    [[1, 4], [2, 3]],
    [[1], [2, 3, 4]],
    [[1], [2, 3], [4]],
    [[1, 4], [2], [3]],
    [[1], [2, 4], [3]],
    [[1], [2], [3, 4]],
    [[1], [2], [3], [4]]
]

for val in values:
    val.reverse()
    val.append([])
    val.reverse()
    print (podzial_rgf(4, val), end=' ')
    print (val[1:])
# [1, 1, 1, 1] [[1, 2, 3, 4]]
# [1, 1, 1, 2] [[1, 2, 3], [4]]
# [1, 1, 2, 1] [[1, 2, 4], [3]]
# [1, 1, 2, 2] [[1, 2], [3, 4]]
# [1, 1, 2, 3] [[1, 2], [3], [4]]
# [1, 2, 1, 1] [[1, 3, 4], [2]]
# [1, 2, 1, 2] [[1, 3], [2, 4]]
# [1, 2, 1, 3] [[1, 3], [2], [4]]
# [1, 2, 2, 1] [[1, 4], [2, 3]]
# [1, 2, 2, 2] [[1], [2, 3, 4]]
# [1, 2, 2, 3] [[1], [2, 3], [4]]
# [1, 2, 3, 1] [[1, 4], [2], [3]]
# [1, 2, 3, 2] [[1], [2, 4], [3]]
# [1, 2, 3, 3] [[1], [2], [3, 4]]
# [1, 2, 3, 4] [[1], [2], [3], [4]]

"""
Procedura wyznaczająca z zadanego podzialu zbioru {1, 2, ..., n} na 'k' bloków
{B[1] , ..., B[k]} odpowiadająca mu funkcje (f[1], ..., f[n]) RGF.
"""
