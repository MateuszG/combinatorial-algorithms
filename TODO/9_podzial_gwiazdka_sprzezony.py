"""
Algorytm 22
Generowanie podziałów liczb n na k składników.
Aby wygenerować wszystkie standardowe podziały liczby 'n' na 'k' składników
wystarczy wygenerować podziały liczby 'n' o największym składniku 'k' i
w każdym przypadku wyznaczyć podział sprzężony.
b = k
"""


def podzial_sprzezony(c):
    b = [1 for _ in range(1, c[1])]
    m = c[1]
    for j in range(2, m):
        for i in range(1, c[j]):
            b[i] = b[i] + 1
    return b


a = []


def podzial_gwiazdka(n, b, m):
    global a

    if a == []:
        a = [0 for _ in range(1, min(b, n))]
        a[1] = b
    if n == 0:
        print podzial_sprzezony(a[1:-1])
    else:
        for i in range(1, min(b, n + 1)):
            a[m + 1] = i
            podzial_gwiazdka(n - i, i, m + 1)

podzial_gwiazdka(6, 6, 0)
# [1]
# [1]
# []