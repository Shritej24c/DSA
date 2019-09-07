import time

t1 = time.perf_counter()


def binary(k, n, array):
    i = 0
    j = n-1
    while i < j+1:
        mid = (i+j)//2
        print(mid)
        if array[mid] > k:
            j = mid - 1
        elif array[mid] < k:
            i = mid + 1
        elif array[mid] == k:
            return mid+1
        else:
            return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(array)
k = 1
print(binary(k, n, array))
t2 = time.perf_counter()
print(t2-t1)


from Binarysearch import Arraystack


def string_reverser(s):
    S = Arraystack()
    for c in s:
        S.push(c)
    r = []
    while not S.isEmpty():
        r.append(S.pop())
    return ''.join(r)


if __name__ == '__main__':
    print(string_reverser('abcdef'))

s = "Defe,sd"
print(s.strip("De").split(','))

f = ["Crow", "Cartoon", "Chromatin", "Coward"]
l = [2, 2]
p = []
num = 0
for j in range(len(l)):
    num += l[j]
    p.append(num)

print(p)

f[0] += "\n"
print(f)

output = ", ".join(f)
print(output)
lines =  output.split("\n")
print(lines)




