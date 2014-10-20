"""
Standardowe podzialy liczb
"""


import pprint
pp = pprint.PrettyPrinter(indent=4)


def liczba_podzial(n, k):
    P = [[0 for _ in range(1, n + 1)] for _ in range(1, n + 2)]
    P[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):

            if i < 2 * j:
                P[i][j] = P[i-1][j-1]
            else:
                P[i][j] = P[i-1][j-1] + P[i-j][j]

    return P


pp.pprint(liczba_podzial(7, 4))
# [   [1, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0],
#     [0, 1, 2, 1, 1, 0, 0],
#     [0, 1, 2, 2, 1, 0, 0],
#     [0, 1, 3, 3, 2, 0, 0],
#     [0, 1, 3, 4, 3, 0, 0]]


def rekur(n, k):
    if n < k:
        return 0

    if k == 0 and n == 0:
        return 1

    if k == 0 and n > 0:
        return 0

    return rekur(n - 1, k - 1) + rekur(n - k, k)

for num in range(10):
    print rekur(num, 5)
# 0
# 0
# 0
# 0
# 0
# 1
# 1
# 2
# 3
# 5
