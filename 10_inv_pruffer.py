"""
Algorytm 24 - Rekonstrukcja drzewa z kodu Prufera

Algorytm wyznaczający drzewo na podstawie kodu pruffera stanowiącego n-2
wyrazowy ciąg liczb (a[1] ... a[n−2]) ze zbioru {1, 2, ..., n}, wygeneruje
drzewo 'T' o zbiorze wierzchołków {1, 2, ..., n}.

Algorytm*:
1. Zapisać dwie listy, pierwsza (a[1] ..., a[n−2]) oraz druga {1, 2, ..., n}
i rozpoczać ze zbiorem wierzchołków {1, 2, ..., n} i pustym zbiorem
krawędzi.

2. Wyznaczyć z drugiej listy największą liczbę, powiedzmy 'i', która nie
występuje na pierwszej liście. Usunąć pierwszy element z pierwszej listy,
powiedzmy 'j', usunąć 'i' z drugiej listy oraz dodać do zbioru krawędzi krawędź
'ij'.

3. Jeżeli pierwsza lista zawiera co najmniej jedną liczbę, to przejść
do (2). W przeciwnym razie, jeżeli pierwsza lista jest pusta, to
druga lista będzie składała się z dokładnie dwóch liczb. Dodać
do zbioru krawędzi ostatnia krawędź i zakończć algorytm.

L - zbior
n - krawedzie
"""


def inv_pruffer(n, L):
    # tworze liste n elementowa wypelniona jedynkami
    d = [1 for i in range(n)]
    E = []

    for i in range(n - 2):
        d[L[i-1] - 1] += 1

    L.append(0)
    L[len(L) - 1] = 1

    for i in range(1, n):
        x = n

        while d[x-1] != 1:
            x -= 1

        y = L[i - 1]
        d[x-1] -= 1
        d[y-1] -= 1
        # E krawedzie x,y dodaje do listy
        E.append([x, y])
    return E

print (inv_pruffer(7, [2, 6, 2, 6, 5]))
print (inv_pruffer(8, [2, 6, 2, 6, 5, 7]))
# [[7, 2], [4, 6], [3, 2], [2, 6], [6, 5], [5, 1]]
# [[8, 2], [4, 6], [3, 2], [2, 6], [6, 5], [5, 7], [7, 1]]
