def generuj_rgf(n):
    F = [1 for _ in range(n + 1)]
    f = [2 for _ in range(n + 1)]
    koniec = False

    while not koniec:
        print f
        j = n

        while f[j] == F[j]:
            j = j - 1
        if j > 1:
            f[j] = f[j] + 1

            for i in range(j + 1, n + 1):
                f[i] = 1
                if f[j] == F[j]:
                    F[i] = F[j] + 1
                else:
                    F[i] = F[j]

        else:
            koniec = True

print generuj_rgf(4)
# Not valid results
