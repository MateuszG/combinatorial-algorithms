"""
Algorytm 2

Traktując charakterystyczne wektory jako binarną reprezentacje liczb
całkowitych od 0 do 2^n − 1, rozpatrywane uporządkowanie leksykograficzne
odpowiada zwyklemu uporządkowaniu liczb całkowitych. Pozycja podzbioru T jest
liczba całkowitą, której binarna reprezentacja jest X(T).
"""


def podzbior_rank(T, n):
    s = 0
    for i in range(1, n + 1):
        if i in T:
            s = s + 2 ** (n-i)
    return s

list_ciag = [
    [],
    [5],
    [4],
    [5, 4],
    [3],
    [5, 3],
    [4, 3],
    [5, 4, 3],
    [2],
    [5, 2]
]

for ciag in list_ciag:
    print podzbior_rank(ciag, 5), ciag
# 0 []
# 1 [5]
# 2 [4]
# 3 [5, 4]
# 4 [3]
# 5 [5, 3]
# 6 [4, 3]
# 7 [5, 4, 3]
# 8 [2]
# 9 [5, 2]
