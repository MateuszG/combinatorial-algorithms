"""
Algorytm 12
Algorytm:
1) Iterujemy za pomocą 'j' do n - 1. Za każdym razem przypisując do 'd' wartość
'r' z reszty dzielenia przez silnia(j + 1), dzieloną przez silnię z 'j'.
2) 'r' zmniejsz o 'd' razy silnia z 'j'.
3) T[n - j] przypisz d + 1
4) Szukaj takiego T[i], które będzie większe od 'd', jeśli znajdziesz to T[i]
zwiększ o jeden (w zakresie od n - j + 1 do 'n')
5) Przejdż do (1) lub wypisz 'T'
"""


def silnia(n):
    return n * silnia(n-1) if n > 1 else 1


def perm_unrank(n, r):
    T = [0 for i in range(n + 1)]
    T[n] = 1
    for j in range(1, n):
        d = (r % silnia(j + 1)) // silnia(j)
        r = r - d * silnia(j)
        T[n - j] = d + 1
        for i in range(n - j + 1, n + 1):
            if T[i] > d:
                T[i] = T[i] + 1
    return T[1:]  # exclude one element at zero index

for rank in range(6):
    print (perm_unrank(3, rank))
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
