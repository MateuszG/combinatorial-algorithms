"""
Algorytm 22 - Podzial gwiazdka - Generowanie podziałów liczb n na k składników.

Algorytm 20 - Podzial sprzężony
Aby wygenerować wszystkie standardowe podziały liczby 'n' na 'k' składników
wystarczy wygenerować podziały liczby 'n' o największym składniku 'k' i
w każdym przypadku wyznaczyć podział sprzężony.

Procedura, któora dla danego podziału (a[1], a[2], . . . , a[m]) wyznacza
podział do niego sprzężony.

b = k
"""


def remove():
    """Usuwanie zbednych elementow (jedynek)"""
    koniec = True
    while koniec:
        while 1 in a:
            a.remove(1)
        koniec = False


def add(m):
    """Dodajemy do listy kolejny element"""
    while m + 1 >= len(a):
        a.append(0)


def podzial_sprzezony(a):
    """Algorytm 20 i część 22"""
    a = [[]] + a
    b = [1 for _ in range(a[1] + 1)]

    for j in range(2, len(a)):
        for i in range(1, a[j] + 1):
            b[i] = b[i] + 1
    return b[1:]


a = []


def podzial_gwiazdka(n, b, m):
    """Algorytm 22"""
    if n == 0:
        print (a[1:], podzial_sprzezony(a[1:]))
        remove()
    else:
        for i in range(1, min(b, n + 1)):
            add(m)
            a[m + 1] = i
            podzial_gwiazdka(n - i, i, m + 1)

podzial_gwiazdka(7, 7, 0)
# Podziały liczby, podziały sprzężone
# [4, 2, 1] [3, 2, 1, 1]
# [4, 3] [2, 2, 2, 1]
# [5, 2] [2, 2, 1, 1, 1]
# [6, 1] [2, 1, 1, 1, 1, 1]
