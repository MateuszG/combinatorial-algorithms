def podzbior_unrank(n, r):
    T = []

    for i in range(n, 0, -1):
        if r % 2 == 1:
            T = T + [i]
        r = r / 2
    print T

podzbior_unrank(5, 1)
podzbior_unrank(5, 2)
podzbior_unrank(5, 3)
podzbior_unrank(5, 4)
podzbior_unrank(5, 5)
