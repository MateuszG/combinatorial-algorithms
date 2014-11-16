"""
Algorytm 16
1) Tworzymy pustą listę 'F' wypełnioną 0-ami (1...n) i definiujemy j = 1.
2) Jeśli F[j] nie jest równe 0, to zwiększ 'j' o 1.
3) 'h' przypisz 1.
4) Szukamy bloku B[h], który zawiera element 'j', za każdym razem gdy go nie
znajdziemy to zwiększamy wartość 'h' o 1,
5) Dla każdego 'g' ze zbioru B[h], przypisujemy F[g] wartość 'h'.
6) Kroki (2-5) powtarzamy 'k' razy.
"""


def not_in(j, h, B):
    b = False

    for i, _ in enumerate(B[h]):
        if B[h][i] == j:
            b = True
    return b


def podzial_rgf(n, k, B):
    F = [0 for _ in range(n + 1)]
    j = 1
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
    print (podzial_rgf(4, len(val), val), end=' ')
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
