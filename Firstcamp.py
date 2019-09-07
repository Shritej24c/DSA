import time

t1 = time.perf_counter()
a = list(range(10000))
n = 4712


def linear_search(a, n):

    for i in range(len(a)):
        if a[i] == n:
            print('No is found and its location is', i+1)
            break
        if i == len(a)-1:
            print("Error 404: Not found")

linear_search(a, n)
t2 = time.perf_counter()
print('Time consumed is :', t2-t1)










