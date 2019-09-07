import matplotlib.pyplot as plt
t = [11, 107, 656, 10190]
sz = [10**i for i in range(5, 9)]


def plot(s, time):
    plt.plot(s, time)
    plt.title("Linear Search Times")
    plt.xlabel("Problem size")
    plt.ylabel("t")
    plt.show()


def subsets(a):
    subset_list = []
    for i in range(len(a)):
        subset_list.append(a[i])


def f(x):
    return (x**x) + (x^x)

print(f(3))
print('Python\nR\nMatlab')
x = 95
a = x == 95
b = x is not None
c = x is 95
d = x == 95.0
e = x is 95.0

