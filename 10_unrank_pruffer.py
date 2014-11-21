"""
Algorytm 26
1) Tworzymy liste 'L' wpełnioną 0 (1...n-2).
2) Iterujemy 'i' (n-2...1) przypisujemy L[i], wartość mod(r, n) + 1.
3) W pętli, zmniejszamy wartość rangi o L[i] + 1 i dzielimy rangę przez 'n'.
"""


def unranga_pruffera(r, n):
    L = [0 for _ in range(n - 2)]

    for i in reversed(range(n - 2)):
        L[i] = r % n + 1
        r = (r - L[i] + 1) // n

    return L

print (unranga_pruffera(4204, 7))
# [2, 6, 2, 6, 5]
