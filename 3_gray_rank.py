"""
Algorytm 5

Iteracyjnie uaktualniamy wartość b mając na uwadzę
– czy a[i] = 1 (zachodzi je ̇zeli n − i in T)
– czy a[i] = 0 (zachodzi je ̇zeli n − i not in T)
Jeżeli b = 1, to dodajemy do r wartość 2^i , gdyż b = b[i] jest
wartością i-tego bitu w binarnej reprezentacji r.
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
