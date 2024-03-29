"""
Algorytm 17
1) k = 1
2) Szukamy największego F[j] (1...n) porównując go z wartością 'k', jeśli
znajdziemy większą wartość to przypisujemy 'k' tą wartość F[j].
3) Tworzymy pustą listę 'B' z podlistami (1...k).
4) Iterując 'j' (1...n) wartości F[j] potraktuj jako indeksy listy B,
dodając do podzbioru B[F[j]] wartość [j].
"""


def rgf_podzial(n, F):
    k = 1
    for j in range(1, n):
        if F[j] > k:
            k = F[j]

    B = [[] for _ in range(k + 2)]

    for j in range(1, n + 1):
        B[F[j]] = B[F[j]] + [j]

    B = [x for x in B if x != []]  # Remove empty lists in list B
    return B


values = [
    [1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 1, 2, 1],
    [1, 1, 2, 2],
    [1, 1, 2, 3],
    [1, 2, 1, 1],
    [1, 2, 1, 2],
    [1, 2, 1, 3],
    [1, 2, 2, 1],
    [1, 2, 2, 2],
    [1, 2, 2, 3],
    [1, 2, 3, 1],
    [1, 2, 3, 2],
    [1, 2, 3, 3],
    [1, 2, 3, 4],
]

for val in values:
    print (val, end=' ')
    val.reverse()
    val.append([])
    val.reverse()
    print (rgf_podzial(4, val))
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
Procedura wyznaczająca z zadanej funkcji RGF(f[1] , . . . , f[n])
odpowiadający jej podział zbioru {1, 2, . . . , n} na stosowna liczbe bloków.
1) Pierwszy 'for' wyznacza, na podstawie zadanej funkcji RGF, liczbe bloków w
podziale odpowiadającym tej funkcji. Sprowadza się to do wyznaczenia
największej składowej.
2) W ostatniej pętli 'for' wstawiane są do kolejnych bloków podziału stosowne
elementy.
"""
