from time import perf_counter
t1 = perf_counter()
a = [j for j in range(10)]
b = 3





t2 = perf_counter()
print(t2-t1)

array = [8, 5, 9, 3, 6, 2, 1, 7, 4]



def sort(a):
    aa = []
    for i in range(len(a)-4):
        aa.append(a[i])
    return aa

print(sort(array))
