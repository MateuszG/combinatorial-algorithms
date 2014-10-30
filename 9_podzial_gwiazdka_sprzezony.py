"""
Algorytm 22
Generowanie podziałów liczb n na k składników.
Aby wygenerować wszystkie standardowe podziały liczby 'n' na 'k' składników
wystarczy wygenerować podziały liczby 'n' o największym składniku 'k' i
w każdym przypadku wyznaczyć podział sprzężony.
b = k
"""


def remove():
    """  """
    koniec = True
    while koniec:
        while 1 in a:
            a.remove(1)
        koniec = False


def add(m):
    """Dodajemy do listy kolejny element"""
    while m + 1 >= len(a):
        a.append(0)


def podzial_sprzezony(c):
    b = [1 for _ in range(1, c[1])]
    m = c[1]
    for j in range(2, m):
        for i in range(1, c[j]):
            b[i] = b[i] + 1
    return b


a = []


def podzial_gwiazdka(n, b, m):
    if n == 0:
        print (a[1:])
        remove()
    else:
        for i in range(1, min(b, n + 1)):
            add(m)
            a[m + 1] = i
            podzial_gwiazdka(n - i, i, m + 1)

podzial_gwiazdka(6, 6, 0)
# [3, 2, 1]
# [4, 2]
# [5, 1]
