import heapq
array = [10, 9, 8,7]

print(heapq.nsmallest(1, array))

def selection_sort(a):
    for i in range(len(a) - 1):
        minm = i
        for j in range(i, len(a)):
            if a[minm] > a[j]:
                a[minm], a[j] = a[j], a[minm]
    print(a)


print(selection_sort(array))
