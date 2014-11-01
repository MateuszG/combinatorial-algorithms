"""
Algorytm 3

Dla zadanej liczby całkowitej r, gdzie 0 ≤ r ≤ 2**n − 1, wyznaczenie podzbioru
T mającego pozycje r w uporządkowaniu leksykograficznym, polega na badaniu
reszt kolejnych wartości r pomniejszanych w każdym kroku o połowę.

Algorytm:
1) W przedziale od 1 do 'n' sprawdzamy kolejne reszty wartości 'r', podzielnych
przez 2, gdy wynik równa się jeden to do zbioru 'T' dodajemy 'i'.
2) W kolejnym korku pomniejszamy 'r' o połowę.
3) Szukamy dalej (1), lub wypisujemy 'T'.
"""


def podzbior_unrank(n, r):
    T = []

    for i in range(n, 0, -1):
        if r % 2 == 1:
            T = T + [i]
        r = r / 2
    print T

for rank in range(10):
    podzbior_unrank(5, rank)
# []
# [5]
# [4]
# [5, 4]
# [3]
# [5, 3]
# [4, 3]
# [5, 4, 3]
# [2]
# [5, 2]
