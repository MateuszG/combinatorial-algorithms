
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
