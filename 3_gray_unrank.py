
def gray_unrank(n, r):
    T = []
    c = 0
    for i in reversed(range(n)):
        b = r / (2 ** i)
        if b != c:
            T = T + [n - i]
        c = b
        r = r - (b * (2 ** i))
    return T

print gray_unrank(3, 6)
