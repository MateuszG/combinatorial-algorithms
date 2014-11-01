"""
Algorytm 7

Algorytm*:
1) Znajdz pierwsza pozycje t[i] od prawej strony nie zawierajaca największego
możliwego elementu
2) Zwiększ t[i] o 1
3) Przypisz elementom leżącym na prawo od t[i] kolejno elementy
(t[i] + 1) + 1, (t[i] + 1) + 2, (t[i] + 1) + 3, . . . (t[i] + 1) + k − i
"""


def podzbior_nast(T, k, n):
    U = T
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
    print podzbior_nast([[]] + unrank, 3, 5)
# [1, 2, 4]
# [1, 2, 5]
# [1, 3, 5]
# [1, 3, 5]
# [1, 4, 6]
# [2, 4, 5]
# [2, 3, 5]
# [2, 4, 6]
# [3, 5, 6]
# None
