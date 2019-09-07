str = "ACGTTACG"


List = []

for x in range(len(str)):
    List.append(str[x])
    if str[x] == "T":
        List.remove(str[x])
        List.append("U")

string = ""

for i in range(len(str)):
    string += List[i]

a = []


def fibo(n):
    a.append('*')



    if n == 1:
        return n
    elif n == 2 or n==3:
        return n-1
    else:
        return fibo(n-1) + fibo(n-2)

def testfib(n):
    print('fib of ', n, '=', fibo(n))


#testfib(7) == testfib(8)

class Arraystack:
    def __init__(self):
        # create a stack
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def __len__(self):
        return len(self.stack)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return len(self.stack) == 0

    def __print__(self):
        print(self.stack)


s = Arraystack()
s.__print__()
print(s.isEmpty())
s.push("YBCBINDIOND")
s.push("fdfd")
s.push("renn")
s.push("revv")
s.push("ninon")
s.pop()
s.__print__()
print (s.top()) 