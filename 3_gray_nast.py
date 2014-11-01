"""
Algorytm 4

Algorytm wyznaczający następnik w kodzie Graya:
– Rozpoczynamy od ciągu zlożonego z samych zer, który odpowiada zbiorowi
pustemu
– Dowolne dwa następujące po sobie podzbiory mają odleglość jeden, tzn. kolejny
podzbiór otrzymujemy z poprzedniego przez usunięcie lub dodanie pojedynczego
elementu (liczba elementów w kolejno generowanych podzbiorach będzie na
przemian parzysta i nieparzysta)

Algorytm:
1) Rozpoczynamy od pustego podzbioru
2) Jeżeli liczba elementów podzbioru 'T' jest parzysta, to bierzemy różnicę
symetryczna podzbioru 'T' i jedoelementowego zbioru złożonego z największego
elementu, tj 'n'.
3) Gdy liczba elementów zbioru 'T' jest nieparzysta,
to jednoelementowym zbiorem jest {j}, gdzie j jest największym elementem
należącym do 'T' pomniejszonym o jeden.
"""


def gray_nast(n, T):
    U = []
    T = set(T)

    if len(T) % 2 == 0:
        U = T.symmetric_difference([n])
    else:
        j = n

        while j not in T:
            j = j - 1
            if j == 1:
                return None
        U = T.symmetric_difference([j - 1])
    return list(U)

lists = [
    [],
    [3],
    [2, 3],
    [2],
    [1, 2],
    [1, 2, 3],
    [1, 3],
    [1]
]
for list_unrank in lists:
    print gray_nast(3, list_unrank)
# [3]
# [2, 3]
# [2]
# [1, 2]
# [1, 2, 3]
# [1, 3]
# [1]
# None
