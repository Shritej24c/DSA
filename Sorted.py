import heapq
array = [8, 5, 9, 3, 6, 2, 1, 7, 4]


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i + 1] = key
    print(a)

insertion_sort(array)


def selection_sort(a):
    for i in range(len(a)):
        key = a[i]
        a[i] = heapq.nsmallest(1, a[i:])[0]
    print(a)


def mselection_sort(a):
    for i in range(len(a)-1):
        minm = i
        for j in range(i, len(a)-1):
            if a[minm] > a[j]:
                minm = j
        if i != minm:
            a[i], a[minm] = a[minm], a[i]
    print(a)
#selection_sort(array)
mselection_sort(array)


def bubble_sort(a):
    for j in range(len(a)):
        for i in range(len(a)-j-1):
            if a[i+1] < a[i]:
                a[i], a[i+1] = a[i+1], a[i]
            else:
                pass
    print(a)

#bubble_sort(array)