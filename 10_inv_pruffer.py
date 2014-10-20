"""
L zbior
n krawedzie
"""


def un_pruffer(n, L):
    # tworze liste n elementowa wypelniona jedynkami
    d = [1 for i in range(n)]
    E = []

    for i in range(n - 2):
        d[L[i-1] - 1] += 1

    L.append(0)
    L[len(L) - 1] = 1

    for i in range(1, n):
        x = n

        while d[x-1] != 1:
            x -= 1

        y = L[i - 1]
        d[x-1] -= 1
        d[y-1] -= 1
        # E krawedzie x,y dodaje do listy
        E.append([x, y])
    return E

print un_pruffer(7, [2, 6, 2, 6, 5])
print un_pruffer(8, [2, 6, 2, 6, 5, 7])
# [[7, 2], [4, 6], [3, 2], [2, 6], [6, 5], [5, 1]]
# [[8, 2], [4, 6], [3, 2], [2, 6], [6, 5], [5, 7], [7, 1]]
