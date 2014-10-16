
def gray_rank(n, T):
    r = 0
    b = 0
    for i in reversed(range(n)):
        if (n - i) in T:
            b = 1 - b
        if b == 1:
            r = r + (2 ** i)
    return r

print('wynik', gray_rank(3, [3]))
print('wynik', gray_rank(3, [2, 3]))
print('wynik', gray_rank(3, [2]))
print('wynik', gray_rank(3, [1, 2]))
