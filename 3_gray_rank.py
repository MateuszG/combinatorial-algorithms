"""
Algorytm 5
1) Definiujemy b = 0
2) Szukamy 'i' (n-1...0) o wartości n - i znajdującej się w zbiorze 'T', gdy
znajdziemy to aktualizujemy wartość 'b' przypisując jej wartość 1 - 'b'.
3) Jeżeli b = 1, to zwiększamy 'r' o wartość 2**i.
"""


def gray_rank(n, T):
    r = 0
    b = 0
    for i in reversed(range(n)):
        if (n - i) in T:
            b = 1 - b
        if b == 1:
            r = r + (2 ** i)
    print r

lists = [
    [],
    [3],
    [2, 3],
    [2],
    [1, 2],
    [1, 2, 3],
    [1, 3],
    [1]
]
for list_unrank in lists:
    gray_rank(3, list_unrank)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7

"""
Iteracyjnie uaktualniamy wartość b mając na uwadzę
– czy a[i] = 1 (zachodzi jeżeli n − i in T)
– czy a[i] = 0 (zachodzi jeżeli n − i not in T)
Jeżeli b = 1, to dodajemy do r wartość 2**i , gdyż b = b[i] jest
wartością i-tego bitu w binarnej reprezentacji r.
"""
