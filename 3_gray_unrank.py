
def gray_unrank(n, r):
    T = []
    c = 0
    for i in reversed(range(n)):
        b = r / (2 ** i)
        if b != c:
            T = T + [n - i]
        c = b
        r = r - (b * (2 ** i))
    print T

for rank in range(8):
    gray_unrank(3, rank)
# []
# [3]
# [2, 3]
# [2]
# [1, 2]
# [1, 2, 3]
# [1, 3]
# [1]
# [1, 2]
# [1, 2, 3]
