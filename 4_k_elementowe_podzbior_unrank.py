"""
Algorytm 9
Algorytm:
1) x = 1
2) Iterując od 1 do k, zmniejsz wartość 'r' o wartość n_po_k, zwiększ x o 1,
dopóki n_po_k jest mniejsze od 'r'.
3) Następnie T[i] przypisz x, zwiększ x o 1.
4) Szukamy dalej (1), lub wypisujemy 'T'.
"""


def silnia(n):
    return n * silnia(n-1) if n > 1 else 1


def n_po_k(n, k):
    po_n = silnia(n)
    po_k = silnia(k) * silnia(n - k)
    wynik = po_n / po_k
    return wynik


def k_elementowe_podzbiory_unrank(r, k, n):
    x = 1
    T = [0]
    for i in range(1, k + 1):
        T.append(0)
        while n_po_k(n - x, k - i) <= r:
            r = r - n_po_k(n - x, k - i)
            x = x + 1
        T[i] = x
        x = x + 1
    return T[1:]


for rank in range(10):
    # empty list for zero index
    print (k_elementowe_podzbiory_unrank(rank, 3, 5))
# [1, 2, 3]
# [1, 2, 4]
# [1, 2, 5]
# [1, 3, 4]
# [1, 3, 5]
# [1, 4, 5]
# [2, 3, 4]
# [2, 3, 5]
# [2, 4, 5]
# [3, 4, 5]
