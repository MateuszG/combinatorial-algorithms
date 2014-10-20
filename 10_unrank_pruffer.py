"""
Mateusz Galganek 150803

"""

def unranga_pruffera(ranga, n):
    # tworze liste pruffera
    L = [0 for _ in range(n - 2)]

    # petla dzialajaca na kodzie pruffera
    for i in reversed(range(n - 2)):
        # dziele range i przypisanie do kodu
        L[i] = ranga % n + 1
        roznica = ranga - L[i]

        # dzielenie rangi + 1 przez wierzcholki
        ranga = (roznica + 1) // n

    return L

print unranga_pruffera(4204, 7)
# Wynik [2, 6, 2, 6, 5]
