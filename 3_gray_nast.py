
def gray_nast(n, T):
    U = []
    T = set(T)

    if len(T) % 2 == 0:
        U = T.symmetric_difference(set([n]))
    else:
        j = n
        while j not in T:
            j = j - 1
            if j == 1:
                return
            U = T.symmetric_difference(set([j - 1]))
    return U

print gray_nast(3, [1, 2])
