"""
Algorytm 23 - Wyznaczanie kodu Prufera dla danego drzewa 'T'
1) Znaleźć największy wierzchołek 'x' o stopniu 1.
2) Niech 'x' będzie wierzchołkiem połączonym z 'y'.
3) Zapisać 'y' do listy 'L' oraz usunąć krawędź [x, y] z listy 'E'.
4) Jeżeli w drzewie pozostała więcej niż 1 krawędź, to przejdź do kroku (1), w
przeciwnym razie zakończy algorytm.
"""


def pruffer(n, E):
    # n - krawedzie, E - wierzcholki
    # tworze liste stopni n-elementowa wypelniona zerami
    d = [0 for i in range(n)]
    # tworze liste n-elementowa wypelniona od 1 do n-2
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

"""
Algorytm wyznaczający kod Prufera dla danego drzewa 'T' na zbiorze wierzchołków
opisanym jako {1, 2, ..., n}, który wygeneruje kod Prüfera stanowiący n-2
wyrazowy ciąg liczb ze zbioru {1,2, ..., n}.
1. Stwórz tablice stopni wierzchołków d[1, ..., n].
2. Wyznacz największy wierchołek 'x' stopnia 1.
3. Znajdź wierzchołek 'y' z którym połączony jest wierzchołek 'x'.
4. Wstaw 'y' do tablicy 'L', usuń krawędź [x, y] z 'E' i zmniejsz o 1
stopnie wierzchołków 'x' i 'y' w tablicy 'd'.
5. Powtarzaj kroki (2-4) łącznie n-2 razy.
"""
