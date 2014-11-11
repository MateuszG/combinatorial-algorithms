"""
Algorytm 8
1) T[1] = 0
2) Iterujemy od 1 do 'k'. Jeśli element leżący na lewo od t[i] - 1 jest
mniejszy lub równy t[i - 1] + 1, to iteruj 'j' od wartości T[i - 1] + 1 do
wartości T[i] - 1.
3) Następne zwiększ range o wartość n_po_k
"""


def silnia(n):
    return n * silnia(n-1) if n > 1 else 1


def n_po_k(n, k):
    po_n = silnia(n)
    po_k = silnia(k) * silnia(n - k)
    wynik = po_n // po_k
    return wynik


def k_elementowe_podzbiory_rank(T, k, n):
    r = 0
    T[0] = 0
    for i in range(1, k + 1):
        if T[i-1] + 1 <= T[i] - 1:
            for j in range(T[i-1] + 1, T[i]):
                r = r + n_po_k(n - j, k - i)
    return r


unranks = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 5],
    [1, 3, 4],
    [1, 3, 5],
    [1, 4, 5],
    [2, 3, 4],
    [2, 3, 5],
    [2, 4, 5],
    [3, 4, 5],
]
for unrank in unranks:
    # empty list for zero index
    print (k_elementowe_podzbiory_rank([[]] + unrank, 3, 5))
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

"""
Wyznacza liczbę k-elementowych podzbiorów poprzdzających zadany zbiór T w
uporządkowaniu leksykograficznym.
"""
