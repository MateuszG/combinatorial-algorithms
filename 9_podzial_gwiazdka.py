"""
Algorytm 22 - Generowanie podziałów liczb n na k składników.
1) Jeśli 'n' jest równe 0 to wywołaj podzial_sprzezony(a) i wypisz wynik.
2) Jeśli nie, to przypisz a[m + 1] wartość 'i' (1...min(b, n)).
3) Wywołaj rekruncyjnie podzial_gwiazdka(n - i, i, m + 1) i przejdź do (1).
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
    if n == 0:
        print (a[1:], podzial_sprzezony(a[1:]))
        remove()
    else:
        for i in range(1, min(b, n) + 1):
            add(m)
            a[m + 1] = i
            podzial_gwiazdka(n - i, i, m + 1)

podzial_gwiazdka(7, 7, 0)
# [1, 1, 1, 1, 1, 1, 1] [7]
# [2, 1, 1, 1, 1, 1] [6, 1]
# [2, 2, 1, 1, 1] [5, 2]
# [2, 2, 2, 1] [4, 3]
# [3, 1, 1, 1, 1] [5, 1, 1]
# [3, 2, 1, 1] [4, 2, 1]
# [3, 2, 2] [3, 3, 1]
# [3, 3, 1] [3, 2, 2]
# [4, 1, 1, 1] [4, 1, 1, 1]
# [4, 2, 1] [3, 2, 1, 1]
# [4, 3] [2, 2, 2, 1]
# [5, 1, 1] [3, 1, 1, 1, 1]
# [5, 2] [2, 2, 1, 1, 1]
# [6, 1] [2, 1, 1, 1, 1, 1]
# [7] [1, 1, 1, 1, 1, 1, 1]

"""
Trzy podzialy liczby 7, w których największym składnikiem jest 4:
4+1+1+1
4+2+1
4+3
Odpowiadającymi im podziałami sprzężonymi są:
4+1+1+1
3+2+1+1
2+2+2+1
"""
