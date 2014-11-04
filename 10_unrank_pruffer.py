"""
Algorytm 26
Algorytm:
1) Tworzymy liste 'L' od końca, przypisując do niej wartość mod(r,n) + 1.
2) Zmieniejszamy wartość rangi o L[i] + 1.
3) Rangę następnie dzielimy przez 'n'.
"""


def unranga_pruffera(r, n):
    L = [0 for _ in range(n - 2)]

    for i in reversed(range(n - 2)):
        L[i] = r % n + 1
        r = (r - L[i] + 1) // n

    return L

print (unranga_pruffera(4204, 7))
# [2, 6, 2, 6, 5]
