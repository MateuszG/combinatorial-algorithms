"""
Algorytm 25
1) Inicjujemy p = 1
2) Iterujemy po liście 'L', za każdym razem zwiększając 'r' o wartość
p*(L[i] - 1).
3) 'p' przypisz p * n
4) Powtarzaj kroki (2-3) łącznie n-2 razy.
"""


def ranga_pruffera(L, n):
    r = 0
    p = 1

    for i in reversed(range(1, n - 1)):
        r = r + p * (L[i] - 1)
        p = p * n

    return r

# empty list at zero index
print (ranga_pruffera([[]] + [2, 6, 2, 6, 5], 7))
# 4204
