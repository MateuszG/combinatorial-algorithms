a = []


def podzial(n, b, m):
    global a
    if a == []:
        a = [0 for _ in range(1, min(b, n))]
    if n == 0:
        print a[1:-1]
    else:
        for i in range(1, min(b, n + 1)):
            a[m + 1] = i
            podzial(n - i, i, m + 1)

podzial(6, 6, 0)
# [3, 2, 1]
# [4, 2, 1]
# [5, 1, 1]
