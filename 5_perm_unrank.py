"""
Algorytm 12
1) T[n] = 1
2) Iterujemy 'j' (1...n-1) za każdym razem przypisując do 'd' wartość
mod(r, (j + 1)!), dzieloną całkowicie przez silnię z 'j'.
3) 'r' zmniejsz o wartość 'd' razy (j)!.
4) T[n - j] przypisz d + 1.
5) Szukaj takiego T[i] (n - j + 1...n), które będzie większe od 'd', jeśli
znajdziesz to T[i] zwiększ o 1.
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
