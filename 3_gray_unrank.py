"""
Algorytm 6
1) Inicjalizujemy listę 'T' i wartość c = 0
2) Itermujemy od 'n-1' do 0 za każdym razem przypisując do 'b' wynik dzielenia
'r' przez 2**i.
3) Jeśli b != c to przypisujemy do zbioru 'T' wartość [n - 1], a wartość 'r'
zmniejszamy o b*(2**i).
"""


def gray_unrank(n, r):
    T = []
    c = 0
    for i in reversed(range(n)):
        b = r / (2 ** i)
        if b != c:
            T = T + [n - i]
        c = b
        r = r - (b * (2 ** i))
    print T

for rank in range(8):
    gray_unrank(3, rank)
# []
# [3]
# [2, 3]
# [2]
# [1, 2]
# [1, 2, 3]
# [1, 3]
# [1]
# [1, 2]
# [1, 2, 3]

"""
Niech c odpowiada b[i+1] a b odpowiada b[i].
Algorytm wyznacza sukcesywnie b[n−1] , . . . , b[0], które są bitami binarnej
reprezentacji liczby r.
"""
