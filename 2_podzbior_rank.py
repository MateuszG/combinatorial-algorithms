def podzbior_rank(T, n):
    s = 0
    for i in range(n):
        if i in T:
            s = s + 2 ** (n-i)
    print s

list_ciag = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 5],
    [1, 3, 4],
    [1, 3, 5],
    [1, 4, 5],
    [2, 3, 4],
    [2, 3, 5],
    [2, 4, 5],
    [3, 4, 5]
]

for ciag in list_ciag:
    podzbior_rank(ciag, 5)
