import numpy as np


def merge(a, b):
    c = [None] * (len(a) + len(b))
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    if i < len(a):
        c[k:] = a[i:]
    else:
        c[k:] = b[j:]
    return c


d = [2, 6, 4, 9, 1, 5, 10, 56]


def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    else:
        return merge(merge_sort(a[:n // 2]), merge_sort(a[n // 2:]))


# print(merge_sort(d))

def edit_distance(a, b):
    m = len(a)
    n = len(b)
    a = " "+a[:]
    b = " "+b[:]
    e = np.zeros((m + 1, n + 1))
    for y in range(1, n + 1):
        e[0][y] = y
    for z in range(1, m + 1):
        e[z][0] = z
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i] == b[j]:
                cs = 0
            else:
                cs = 1
            e[i][j] = min(e[i - 1][j] + 1, e[i][j - 1] + 1, e[i - 1][j - 1] + cs)
    return e[m][n]


print(edit_distance("logar", "algor"))
print(edit_distance("ATAGAC", "TAACGAC"))
print(edit_distance("TAACGAC", "ATAGAC"))
print(edit_distance("PLEASANTLY", "MEANLY"))

#def shared_motif():
