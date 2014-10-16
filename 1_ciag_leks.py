
def ciag_leks(k, n):
    X = [1 for _ in range(k)]
    print X

    m = (n ** k) - 1

    for _ in range(m):
        s = k - 1

        while X[s] == n:
            s = s - 1

        X[s] = X[s] + 1

        for i in range(s + 1, k):
            X[i] = 1

        print X


ciag_leks(3, 2)
ciag_leks(4, 3)
