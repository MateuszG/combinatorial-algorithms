"""
Algorytm 18

Algorytm*:
1) Idea algorytmu polega na znalezieniu pierwszej pozycji z prawej
strony tablicy f, dla której f[j] != F[j].
2) Wówczas wartość elementu f[j] zostaje zwiększona o 1 a wszystkie elementy
leżące na prawo od niego czynimy równe 1, uaktualniając jednocześnie tablice F.
3) Uaktualnienie to polega na tym, że jeżeli nowa wartość f[j] daje
f[j] == F[j], to wszystkie elementy tablicy F leżące na prawo przyjmują
wartość F[j] + 1, a w przeciwnym razie przyjmują one wartość F[j].
4) Proces ten kontynujemy dopóki nie będzie spełniony warunek f[j] == F[j] dla
wszystkich j.
"""


def generuj_rgf(n):
    f = [1 for _ in range(n)]
    F = [2 for _ in range(n)]
    koniec = False

    while not koniec:
        print f
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
