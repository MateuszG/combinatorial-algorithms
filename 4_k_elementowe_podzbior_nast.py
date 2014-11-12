"""
Algorytm 7
1) 'U' przypisz 'T'.
2) Znajdź pierwszą pozycje T[i] od prawej strony nie zawierającą największego
możliwego elementu.
3) Zwiększ T[i] o 1,
4) Przypisz pozycją U[j] z indeksami (i...k) leżącym na prawo od T[i] wartość
(T[i] + 1) + (j − i).
"""


def k_elementowe_podzbiory_nast(T, k, n):
    U = T[:]
    i = k
    while i >= 1 and T[i] == n - k + i:
        i = i - 1
    if i == 0:
        return None
    else:
        for j in range(i, k + 1):
            U[j] = (T[i] + 1) + (j - i)
        return U[1:]

unranks = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 5],
    [1, 3, 4],
    [1, 3, 5],
    [1, 4, 5],
    [2, 3, 4],
    [2, 3, 5],
    [2, 4, 5],
    [3, 4, 5],
]
for unrank in unranks:
    # empty list for zero index
    print (k_elementowe_podzbiory_nast([[]] + unrank, 3, 5))
# [1, 2, 4]
# [1, 2, 5]
# [1, 3, 4]
# [1, 3, 5]
# [1, 4, 5]
# [2, 3, 4]
# [2, 3, 5]
# [2, 4, 5]
# [3, 4, 5]
# None
