"""
Algorytm 13
"""


import pprint
pp = pprint.PrettyPrinter(indent=4)


def stirlinga_2(n, k):
    S = [[1 for x in xrange(n + 1)] for x in xrange(n + 1)]

    for i in (1, n):
        S[i][0] = 0

    for i in range(0, n):
        S[i][i + 1] = 0

    for i in range(1, n):
        for j in range(1, min(i, k)):
            S[i][j] = S[i - 1][j - 1] + j * S[i - 1][j]
    return S


pp.pprint(stirlinga_2(4, 2))
# [   [1, 0, 1, 1, 1],
#     [0, 1, 0, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 2, 1, 1, 0],
#     [0, 1, 1, 1, 1]]
