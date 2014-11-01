"""
Algorytm 15

każdy następny podziału powstaje z poprzedniego przez usunięcie pewnego
elementu (zwanego dalej elementem aktywnym) z pewnego bloku (może to spowodować
usunięcie bloku jednoelementowego) i dodanie go do innego bloku lub też
utworzenie z niego bloku jednoelementowego

Wyznaczanie elementu aktywnego:
– dysponujemy tablica boolowska PR określająca kierunek poruszania się danego
elementu
– początkowo mamy jedno-blokowy podzial {1, 2, . . . , n}
– wszystkie warości tablicy PR maja przyporządkowana wartości 'true'
– zasada: po wygenerowaniu (i wypisaniu) kolejnego podzialu wyznaczamy ,,nowy”
element aktywny zawsze poczynając analize od elementu największego
– dany element jest przesuwany (tzn. jest aktywny) tylko wtedy, gdy wszystkie
większe od niego elementy osiągneły swoje skrajne lewe lub prawe polożenie
– element aktywny 'j*' jest najmniejszym elementem, takim że dla każdego
większego elementu 'j' jest spełniony jeden z następujących dwóch warunków:
PR[j] and B[j] = j tzn. element 'j' porusza sie w prawo i osiągnął
swoje skrajne prawe polożenie ('j' nie może być elementem bloku o numerze
większym niż  'j'), lub not PR[j] and B[j] = 1 tzn. element 'j' porusza się w
lewo i osiągnał swoje skrajne lewe położenie, tj. znalazł się w bloku o numerze
1.

Z wykładu:
N[i] - numer nastepnego bloku dla bloku o numerze 'i'
P[i] - numer poprzedniego bloku o numerze podziału 'i'.
B[i] - numer bloku zawierającego element 'i'.
PR[j] - kierunek poruszania się elementu aktywnego.
PR[j] gdy True to 'j' porusza się w prawo, gdy False 'j' porusza się w lewo.

element aktywny - tek który porusza się w prawo lub lewo
numer bloku - bedzie najmnieszym elmentem w tym bloku (numeracja w bloku jest
rosnąca)

Algorytm*:
1) Zdefiniuj tablice
2) Przenieś element aktywny do sąsiedniego bloku:
- następnego, jeżeli 'j' porusza się w prawo, w tym przypadku może zajść
utworzenie nowego bloku.
- poprzedniego jeżeli 'j' porusza się w lewo.
3) Wyznacz element aktwyny w nowym podziale.
"""


def algorytm(n):
    # Tworzenie tablic N P B PR
    N = [0 for _ in range(0, n + 1)]
    P = [0 for _ in range(0, n + 1)]
    N[1] = 0
    B = [1 for _ in range(0, n + 1)]
    PR = [True for x in range(0, n + 1)]
    j = n

    # Domyslnie True porusza sie w prawo
    drukuj(B)

    # Przesuwanie elementu aktywanego
    while j > 1:
        k = B[j]
        if PR[j]:
            if N[k] == 0:
                N[k] = j
                N[j] = 0
                P[j] = k
            elif N[k] > j:
                P[j] = k
                N[j] = N[k]
                P[N[j]] = j
                N[k] = j
            B[j] = N[k]
        else:
            B[j] = P[k]
            if k == j:
                if N[k] == 0:
                    N[P[k]] = 0
                else:
                    N[P[k]] = N[k]
                    P[N[k]] = P[k]
        drukuj(B)
        j = n
        while(
            (j > 1) and (PR[j] and B[j] == j)
            or (not PR[j] and B[j] == 1)
        ):
            PR[j] = not(PR[j])
            j = j - 1


def drukuj(B):
    """
    Funkcja wypisujaca elementy w sposob uporzadkowany
    """
    slownik = {}
    for i in range(1, len(B)):
        if (B[i]) in slownik:
            slownik[B[i]] += [i]
        else:
            slownik[i] = [i]
    print slownik

algorytm(4)
# {1: [1, 2, 3, 4]}
# {1: [1, 2, 3], 4: [4]}
# {1: [1, 2], 3: [3], 4: [4]}
# {1: [1, 2], 3: [3, 4]}
# {1: [1, 2, 4], 3: [3]}
# {1: [1, 4], 2: [2], 3: [3]}
# {1: [1], 2: [2, 4], 3: [3]}
# {1: [1], 2: [2], 3: [3, 4]}
# {1: [1], 2: [2], 3: [3], 4: [4]}
# {1: [1], 2: [2, 3], 4: [4]}
# {1: [1], 2: [2, 3, 4]}
# {1: [1, 4], 2: [2, 3]}
# {1: [1, 3, 4], 2: [2]}
# {1: [1, 3], 2: [2, 4]}
# {1: [1, 3], 2: [2], 4: [4]}
