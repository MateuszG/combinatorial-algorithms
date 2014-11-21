"""
Algorytm 24 - Rekonstrukcja drzewa z kodu Prufera
1. Rozpoczynamy z pustym zbiorem krawędzi 'E'.
2. Wyznaczamy tablice 'd' stopni wierzchołków (1...n) o wartości 1.
3. Szukamy największego wierzchołka 'x', który nie występuje na liście.
4. Pod 'y' podstaw pierwszy element aktualnego kodu pruffera. Zmniejsz o 1
stopnie wierzchołków 'x' i 'y' i dodaj do zbioru krawędzi krawędź [x, y].
5. Powtarzaj kroki (3-4) stosowną ilość razy.
"""


def inv_pruffer(n, L):
    L.append(1)
    # tworze liste stopni n-elementowa wypelniona jedynkami
    d = [[]] + [1 for i in range(n)]
    E = []

    for i in range(1, n - 1):
        d[L[i]] += 1

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
