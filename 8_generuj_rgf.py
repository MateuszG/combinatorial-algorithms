def generuj_rgf(n):
    f = [1 for _ in range(n)]
    F = [2 for _ in range(n)]
    koniec = False

    while not koniec:
        print f
        j = n

        while True:
            j = j - 1

            if f[j] != F[j]:
                break

        if j > 0:
            f[j] = f[j] + 1

            for i in range(j + 1, n):
                f[i] = 1

                if f[j] == F[j]:
                    F[i] = F[j] + 1
                else:
                    F[i] = F[j]

        else:
            koniec = True

generuj_rgf(4)
# [1, 1, 1, 1]
# [1, 1, 1, 2]
# [1, 1, 2, 1]
# [1, 1, 2, 2]
# [1, 1, 2, 3]
# [1, 2, 1, 1]
# [1, 2, 1, 2]
# [1, 2, 1, 3]
# [1, 2, 2, 1]
# [1, 2, 2, 2]
# [1, 2, 2, 3]
# [1, 2, 3, 1]
# [1, 2, 3, 2]
# [1, 2, 3, 3]
# [1, 2, 3, 4]
