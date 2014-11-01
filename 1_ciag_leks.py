"""
Algorytm 1

Generuj w porządku leksykograficznym wszystkie ciągi długości 'k' zbudowane
z liczb od 1 do n.
Pierwszym ciągiem jest (1, 1, . . . , 1) a ostatnim (n, n, . . . , n).
Wektor X[1..k] zawiera ostatni wygenerowany ciąg.
Inicjujemy wektor 'X' samymi jedynkami.

Algorytm:
1) szukamy w tablicy 'X', poruszając się od końca (tj. od strony prawej do
lewej) wyrazu stojącego najbardziej na prawo, który jest mniejszy od 'n'
2) zwiększamy go o jeden
3) wszystkie wyrazy na prawo od niego czynimy równe jeden
"""


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
# [1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [1, 2, 2]
# [2, 1, 1]
# [2, 1, 2]
# [2, 2, 1]
# [2, 2, 2]
