def rgf_podzial(n, F):
    k = 1
    for j in range(1, n):
        if F[j] > k:
            k = F[j]

    B = [[] for _ in range(k + 2)]

    for j in range(1, n + 1):
        B[F[j]] = B[F[j]] + [j]
    return B[1:]  # Removed first dummp element


values = [
    [1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 1, 2, 1],
    [1, 1, 2, 2],
    [1, 1, 2, 3],
    [1, 2, 1, 1],
    [1, 2, 1, 2],
    [1, 2, 1, 3],
    [1, 2, 2, 1],
    [1, 2, 2, 2],
    [1, 2, 2, 3],
    [1, 2, 3, 1],
    [1, 2, 3, 2],
    [1, 2, 3, 3],
    [1, 2, 3, 4],
]

for val in values:
    print val,
    val.reverse()
    val.append([])
    val.reverse()
    print rgf_podzial(4, val)
