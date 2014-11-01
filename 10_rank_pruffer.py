"""
Algorytm 25

Algorytm:
1) Inicjujemy r = 0 i p = 1
2) Iterujemy od prawej (n - 2) do lewej (1) po liście 'L'. Za każdym razem
zwiększając 'r' o wartość L[i] - 1.
3) 'p' przypisz p*n
4) Iterujemy dalej (1), lub wypisujemy 'r'.
"""


def ranga_pruffera(L, n):
    r = 0
    p = 1

    for i in reversed(range(1, n - 1)):
        r = r + p*(L[i] - 1)
        p = p*n

    return r

# empty list at zero index
print (ranga_pruffera([[]] + [2, 6, 2, 6, 5], 7))
# 4204
