def podzbior_unrank(n, r):
    T = []

    for i in range(n, 0, -1):
        if r % 2 == 1:
            T = T + [i]
        r = r / 2
    print T

for rank in range(10):
    podzbior_unrank(5, rank)
# []
# [5]
# [4]
# [5, 4]
# [3]
# [5, 3]
# [4, 3]
# [5, 4, 3]
# [2]
# [5, 2]
