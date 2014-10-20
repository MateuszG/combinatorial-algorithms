"""
Mateusz Galganek
Podzial zbioru na k-bloki wyznaczyc funkcje RGF
"""


def not_in(j, h, B):
    b = True
    for i, _ in enumerate(B[h]):
        if B[h][i] == j:
            b = False
    return b


def gen(n, B):
    F = [0 for _ in range(n)]
    j = 1

    while F[j] != 0:
        j = j + 1
    h = 1

    while not_in(j, h, B) and len(B) <= h + 1:
        h = h + 1

    for i, g in enumerate(B[h]):
        F[B[h][i] - 1] = h
    return F

values = [
    [[1, 2, 3, 4]],
    [[1, 2, 3], [4]],
    [[1, 2, 4], [3]],
    [[1, 2], [3, 4]],
    [[1, 3, 4], [2]],
    [[1, 2], [3], [4]],
    [[1], [2], [4], [3]]
]

for val in values:
    val.reverse()
    val.append([])
    val.reverse()
    print gen(4, val),
    print val[1:]

# [1, 1, 1, 1] [[1, 2, 3, 4]]
# [1, 1, 1, 0] [[1, 2, 3], [4]]
# [1, 1, 0, 1] [[1, 2, 4], [3]]
# [1, 1, 0, 0] [[1, 2], [3, 4]]
# [1, 0, 0, 0] [[1], [2], [4], [3]]
