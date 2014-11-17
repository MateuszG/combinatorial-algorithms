"""
Algorytm 18
1) Stwórz listę 'f' wypełnioną 1 i listę 'F' wypełnioną 2 (1...n).
2) Zdefiniuj zmienną boolowską 'koniec' i przypisz jej False.
3) Dopóki 'koniec' nie jest True, to wypisuj tablicę 'f'.
4) Przypisz 'j' wartośc 'n', jeśli f[j] jest równe F[j] to zmniejszaj 'j' o 1.
5) Gdy wartość 'j' jest większa od 1 to wartość elementu f[j] zostaje
zwiększona o 1, a wszystkie elementy leżące na prawo przypisujemy 1,
uaktualniając jednocześnie tablice F.
6) Uaktualnienie to polega na tym, że jeżeli nowa wartość f[j] daje
f[j] == F[j], to wszystkie elementy tablicy F leżące na prawo przyjmują
wartość F[j] + 1, a w przeciwnym razie przyjmują one wartość F[j].
7) Proces (3-6) kończymy gdy koniec = True ('j' jest mniejsze lub równe 1).
"""


def generuj_rgf(n):
    f = [1 for _ in range(n)]
    F = [2 for _ in range(n)]
    koniec = False
    while not koniec:
        print (f)
        j = n
        while True:
            j = j - 1
            if f[j] != F[j]:
                break
        if j > 0:
            f[j] = f[j] + 1
            for i in range(j + 1, n):
                f[i] = 1
                if f[j] == F[j]:
                    F[i] = F[j] + 1
                else:
                    F[i] = F[j]
        else:
            koniec = True

generuj_rgf(4)
# [1, 1, 1, 1]
# [1, 1, 1, 2]
# [1, 1, 2, 1]
# [1, 1, 2, 2]
# [1, 1, 2, 3]
# [1, 2, 1, 1]
# [1, 2, 1, 2]
# [1, 2, 1, 3]
# [1, 2, 2, 1]
# [1, 2, 2, 2]
# [1, 2, 2, 3]
# [1, 2, 3, 1]
# [1, 2, 3, 2]
# [1, 2, 3, 3]
# [1, 2, 3, 4]
"""
1) Idea algorytmu polega na znalezieniu pierwszej pozycji z prawej
strony tablicy f, dla której f[j] != F[j].
"""
