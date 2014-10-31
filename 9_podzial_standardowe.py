"""
Algorytm 21

Generowanie wszystkich standardowych podziałów liczby n na k składników.

– a[1] , a[2] , . . . , a[m] są już wybranymi składnikami podziału
– parametr b jest górnym ograniczeniem wartości następnego generowanego
składnika
– a[m+1] może przyjąc wartości od 1 do b

b = k
"""


a = []


def remove():
    koniec = True
    while koniec:
        while 1 in a:
            a.remove(1)
        koniec = False


def add(m):
    while m + 1 >= len(a):
        a.append(0)


def podzial(n, b, m):
    if n == 0:
        print a
        remove()
    else:
        for i in range(1, min(b, n) + 1):
            add(m)
            a[m + 1] = i
            podzial(n - i, i, m + 1)

podzial(6, 6, -1)
# [1, 1, 1, 1, 1, 1]
# [2, 1, 1, 1, 1]
# [2, 2, 1, 1]
# [2, 2, 2]
# [3, 1, 1, 1]
# [3, 2, 1]
# [3, 3]
# [4, 1, 1]
# [4, 2]
# [5, 1]
# [6]
