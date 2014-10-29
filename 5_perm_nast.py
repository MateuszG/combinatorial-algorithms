
def perm_rank(n, T):
    T[0] = 0
    i = n - 1
    while T[i + 1] < T[i]:
        i = i - 1
    if i == 0:
        return None
    j = n
    while T[j] < T[i]:
        j = j - 1

    p = [1 for _ in range(n + 1)]
    for h in range(i, n + 1):
        p[h] = T[h]

    for h in range(i, n + 1):
        T[h] = p[n + i - h]

    return T[1:]

unranks = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]

for unrank in unranks:
    print perm_rank(3, [[]] + unrank)

# [1, 3, 2]
# [2, 3, 1]
# [2, 3, 1]
# [1, 3, 2]
# [3, 2, 1]
# None
