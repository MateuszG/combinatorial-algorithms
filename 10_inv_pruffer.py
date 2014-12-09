"""
Algorytm 24 - Rekonstrukcja drzewa z kodu Prufera
1) Rozpoczynamy z pustym zbiorem krawędzi 'E'.
2) Wyznaczamy tablicę 'd' stopni wierzchołków (1...n) z wartościami 1.
3) Dodaj element 1 na końcu zbioru 'L'.
4) Iterujemy 'j' (1...n-1) zwiększając wartośc d[L[j]] o 1.
5) Iterujemy 'i' (1...n) przypisując 'x' wartość 'n'.
6) W pętli, dopóki d[x] != 1 to zmniejsz 'x' o 1.
7) W pętli, pod 'y' podstaw pierwszy element aktualnego kodu pruffera L[i].
Zmniejsz o 1 stopnie wierzchołków d[x] i d[y] i dodaj do zbioru krawędzi 'E'
krawędź [x, y].
"""


def inv_pruffer(n, L):
    L.append(1)
    # tworze liste stopni n-elementowa wypelniona jedynkami
    d = [[]] + [1 for i in range(n)]
    E = []

    for j in range(1, n):
        d[L[j]] += 1

    for i in range(1, n):
        x = n

        while d[x] != 1:
            x -= 1

        y = L[i]
        d[x] -= 1
        d[y] -= 1
        # E krawedzie x,y dodaje do listy
        E.append([x, y])
    return E

print (inv_pruffer(7, [[]] + [2, 6, 2, 6, 5]))
print (inv_pruffer(8, [[]] + [2, 6, 2, 6, 5, 7]))
# [[7, 2], [4, 6], [3, 2], [2, 6], [6, 5], [5, 1]]
# [[8, 2], [4, 6], [3, 2], [2, 6], [6, 5], [5, 7], [7, 1]]

"""
Algorytm wyznaczający drzewo na podstawie kodu pruffera stanowiącego n-2
wyrazowy ciąg liczb (a[1] ... a[n−2]) ze zbioru {1, 2, ..., n}, wygeneruje
drzewo 'T' o zbiorze wierzchołków {1, 2, ..., n}.
"""
