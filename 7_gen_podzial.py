"""
Mateusz Galganek
Algorytm iteracyjny generujacy wszystkie podzialy zbioru
n-elementowego z elementem aktywnym
"""


def algorytm(n):
    # Tworzenie tablic N P B PR
    N = [0 for _ in range(0, n + 1)]
    P = [0 for _ in range(0, n + 1)]
    N[1] = 0
    B = [1 for _ in range(0, n + 1)]
    PR = [True for x in range(0, n + 1)]
    j = n

    # Domyslnie True porusza sie w prawo
    drukuj(B)

    # Przesuwanie elementu aktywanego
    while j > 1:
        k = B[j]
        if PR[j]:
            if N[k] == 0:
                N[k] = j
                N[j] = 0
                P[j] = k
            elif N[k] > j:
                P[j] = k
                N[j] = N[k]
                P[N[j]] = j
                N[k] = j
            B[j] = N[k]
        else:
            B[j] = P[k]
            if k == j:
                if N[k] == 0:
                    N[P[k]] = 0
                else:
                    N[P[k]] = N[k]
                    P[N[k]] = P[k]
        drukuj(B)
        j = n
        while(
            (j > 1) and (PR[j] and B[j] == j)
            or (not PR[j] and B[j] == 1)
        ):
            PR[j] = not(PR[j])
            j = j - 1


def drukuj(B):
    """
    Funkcja wypisujaca elementy w sposob uporzadkowany
    """
    slownik = {}
    for i in range(1, len(B)):
        if (B[i]) in slownik:
            slownik[B[i]] += [i]
        else:
            slownik[i] = [i]
    print slownik

algorytm(4)
# {1: [1, 2, 3, 4]}
# {1: [1, 2, 3], 4: [4]}
# {1: [1, 2], 3: [3], 4: [4]}
# {1: [1, 2], 3: [3, 4]}
# {1: [1, 2, 4], 3: [3]}
# {1: [1, 4], 2: [2], 3: [3]}
# {1: [1], 2: [2, 4], 3: [3]}
# {1: [1], 2: [2], 3: [3, 4]}
# {1: [1], 2: [2], 3: [3], 4: [4]}
# {1: [1], 2: [2, 3], 4: [4]}
# {1: [1], 2: [2, 3, 4]}
# {1: [1, 4], 2: [2, 3]}
# {1: [1, 3, 4], 2: [2]}
# {1: [1, 3], 2: [2, 4]}
# {1: [1, 3], 2: [2], 4: [4]}
