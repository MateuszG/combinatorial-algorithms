"""
Algorytm 20 - Dla podziału wyznacza podział do niego sprzężony.
1) Zainicjalizuj listę 'b' długości a[1] samymi jedynkami.
2) Iteruj 'j' po zadanej liście 'a' od 2 do liczby ilości elementów na liście.
3) Dla każdego elementu z listy 'a' iteruj jako 'i', od 1 do wartości a[j].
4) Zwiększ wartość b[i] o 1.
"""


def podzial_sprzezony(a):
    """Algorytm 20"""
    a = [[]] + a
    b = [1 for _ in range(a[1] + 1)]

    for j in range(2, len(a)):
        for i in range(1, a[j] + 1):
            b[i] = b[i] + 1
    return b[1:]

podzialy = [
    [1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1],
    [2, 2, 1, 1, 1],
    [2, 2, 2, 1],
    [3, 1, 1, 1, 1],
    [3, 2, 1, 1],
    [3, 2, 2],
    [3, 3, 1],
    [4, 1, 1, 1],
    [4, 2, 1],
    [4, 3],
    [5, 1, 1],
    [5, 2],
    [6, 1],
    [7]
]
for podzial in podzialy:
    print (podzial, podzial_sprzezony(podzial))
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
Procedura, która dla danego podziału (a[1], a[2], . . . , a[m]) wyznacza
podział do niego sprzężony.
Podziały sprzeżone:
– liczba skladników w pierwszym podziale odpowiada największemu składnikowi w
drugim podziale.
– największy składnik w pierwszym podziale odpowiada liczbie skladników w
drugim podziale.
– jeżeli k ≤ n jest dodatnia liczba całkowita, to operacja sprzężenia jest
bijekcja ze zbioru podzialów liczby 'n' na 'k' składników na zbiór podzialów
liczby 'n' (na dowolna liczbę skladników), w których największym składnikiem
jest 'k'.
"""
