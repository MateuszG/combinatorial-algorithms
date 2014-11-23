"""
Algorytm 27
1) Jeśli 'n' jest mniejsze od 2, to wypisz 1.
2) Jeśli nie, to zdefinuj sumę i przypisz 0.
3) Iteruj 'k' (0...n) za każdym razem zwiększając sumę o wartość
n_po_k(n - 1, k) razy wartość wyniku z liczba_bella(k).
"""


def n_po_k(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return n_po_k(n-1, k-1) + n_po_k(n - 1, k)


def liczba_bella(n):
    if n < 2:
        return 1
    else:
        suma = 0
        for k in range(n):
            suma += n_po_k(n - 1, k) * liczba_bella(k)
        return suma

for i in range(10):
    print (i, liczba_bella(i))
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

"""
Liczba Bella - wyznacza wszystkie możliwe podziały zbioru n-elementowego.
(n - 1)
(  k  )
"""
