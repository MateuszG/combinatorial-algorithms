"""
Algorytm 23

Aby wyznaczyć kod Prufera dla danego drzewa 'T' na zbiorze wierzchołków
{1, . . . , n}, należy:

Algorytm*:
1. Znaleźć największy wierzchołek o stopniu 1, powiedzmy 'v'. Niech 'w' będzie
wierzchołkiem połączonym z 'v'.

2. Zapisać 'w' oraz usunać wierzchołek 'v' wraz z krawędzia 'vw'.

3. Jeżeli w drzewie pozostała więcej niż jedna krawędź, to przejść do kroku 1;
w przeciwnym razie zakończyć algorytm.

Otrzymany ciąg liczb jest kodem Prufera dla drzewa 'T'.

E - wierzcholki
n - krawedzie
"""


def pruffer(n, E):
    # tworze liste n elementowa wypelniona zerami
    d = [0 for i in range(n)]
    # tworze liste n elementowa wypelniona od 1 do n-2
    L = [i+1 for i in range(n-2)]

    for x, y in E:
        x = x - 1
        y = y - 1

        d[x] = d[x] + 1
        d[y] = d[y] + 1

    for i in range(n-2):
        x = n
        y = n
        while d[x - 1] != 1:
            x = x - 1

        while [x, y] not in E:
            y = y - 1

        L[i] = y

        d[x - 1] = d[x - 1] - 1
        d[y - 1] = d[y - 1] - 1

        # Usuwanie z listy, listy [x,y]
        E.remove([x, y])
    return L

print (pruffer(
    7,
    [
        [1, 5],
        [6, 5],
        [4, 6],
        [2, 6],
        [3, 2],
        [7, 2]
    ]
    )
)
# [2, 6, 2, 6, 5]
