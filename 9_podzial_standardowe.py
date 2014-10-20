a = []


def podzial(n, b, m):
    if n == 0:
        print a[1:-1]
    else:
        for i in range(1, min(b, n + 1)):
            while m + 1 >= len(a):
                a.append(0)
            a[m + 1] = i
            podzial(n - i, i, m + 1)

podzial(6, 6, 0)
# [3, 2]
# [4, 2]
# [5, 1]
