"""
Algorytm 25
1) Definiujemy p = 1
2) Iterujemy 'i' (n-2...1) za każdym razem zwiększając 'r' o wartość
p*(L[i] - 1).
3) W pętli, 'p' przypisz p * n
"""


def pruffer_rank(L, n):
    r = 0
    p = 1

    for i in reversed(range(1, n - 1)):
        r = r + p * (L[i] - 1)
        p = p * n

    return r

# empty list at zero index
print (pruffer_rank([[]] + [2, 6, 2, 6, 5], 7))
# 4204
