"""
Algorytm 6
1) Definiujemy listę 'T' i wartość c = 0
2) Iterujemy 'i' (n-1...0) za każdym razem przypisujemy do 'b' wynik dzielenia
div(r, 2**i).
3) W pętli, jeśli b != c to przypisujemy do zbioru 'T' wartość [n - 1]
4) W pętli, 'c' przypisujemy 'b', a 'r'zmniejszamy o b*(2**i).
"""


def gray_unrank(n, r):
    T = []
    c = 0
    for i in reversed(range(n)):
        b = r // (2 ** i)  # całkowite dzielenie - div
        if b != c:
            T = T + [n - i]
        c = b
        r = r - (b * (2 ** i))
    print (T)

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

"""
Niech c odpowiada b[i+1] a b odpowiada b[i].
Algorytm wyznacza sukcesywnie b[n−1] , . . . , b[0], które są bitami binarnej
reprezentacji liczby r.
"""
