"""
Algorytm ?

Wyznaczenie liczby Bella wykorzystujac zaleznosci
rekurencyjne

Liczba bella - Liczba wszystkich możliwych podziałów zbioru n-elementowego.
"""


def n_po_k(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return n_po_k(n-1, k-1) + n_po_k(n - 1, k)


def liczba_bella(liczba_n):
    if liczba_n < 2:
        return 1
    else:
        suma = 0
        for liczba_k in xrange(liczba_n):
            # Zwykla suma elementow
            suma += n_po_k(liczba_n - 1, liczba_k) * liczba_bella(liczba_k)
        return suma

for i in range(10):
    print i, liczba_bella(i)
# 0 1
# 1 1
# 2 2
# 3 5
# 4 15
# 5 52
# 6 203
# 7 877
# 8 4140
# 9 21147
