"""
Mateusz Galganek
Podzial zbioru na k-bloki wyznaczyc funkcje RGF
"""

def gen(n, k, B):
    F = [0 for _ in range(1, n + 1)]
    j = 1

    for i in range(1, k):
        while F[j] != 0:
            j = j + 1
        h = 1
        print ('j', j)
        while j != B[h]:
            print h
            h = h + 1
        for g in range(len(B)):
            if g == B[h]:
                F[g] = h
    return F

print gen(3, 3, [[], 2,3,3])
