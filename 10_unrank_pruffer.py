"""
Algorytm 26
1) Tworzymy liste 'L'.
2) Poruszając się od końca, przypisujemy L[i], wartość mod(r, n) + 1.
3) Zmniejszamy wartość rangi o L[i] + 1.
4) Rangę następnie dzielimy przez 'n'.
5) Powtarzaj kroki (2-4) łącznie n-2 razy.
"""


def unranga_pruffera(r, n):
    L = [0 for _ in range(n - 2)]

    for i in reversed(range(n - 2)):
        L[i] = r % n + 1
        r = (r - L[i] + 1) // n

    return L

print (unranga_pruffera(4204, 7))
# [2, 6, 2, 6, 5]
