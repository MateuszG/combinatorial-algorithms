def ranga_pruffera(L):
    # dlugosc pruffera
    L_len = len(L) + 2
    licznik = 0
    temp = 1

    # petla dzialajaca na kodzie pruffera
    for i in reversed(range(L_len - 2)):
        war_pruff = L[i] - 1
        licznik = licznik + temp * war_pruff
        temp = temp * L_len

    return licznik

print ranga_pruffera([2, 6, 2, 6, 5])
# 4204
