class Polynomial:

    def __init__(self, *coeffient):
        self.list = list(coeffient)



    def __add__(self,other):
        """>>> Polynomial(1, 2)+(Polynomial(2, 3, 4))
[2, 4, 6]"""
        if len(other.list) >= len(self.list):
            new = []
            for i in range(len(self.list), 0, -1):
                b = other.list[len(other.list) + i - len(self.list) - 1] + self.list[i - 1]
                new.append(b)
            new.reverse()
            addtn = other.list[:len(other.list) - len(self.list)] + new
            return addtn
        else:
            print(" Please enter polynomial with smaller degree first !")

    def polyval(self, x):
        n = len(self.list) - 1
        val = 0
        for i in range(len(self.list)):
            val += self.list[i]*(x**(n-i))
        return val

    def differentiate(self, order=1):
       for j in range(order):
            n = len(self.list) - 1
            new = []
            for i in range(len(self.list) - 1):
                d = self.list[i]*(n - i)
                new.append(d)
            self.list = new
       print(new)



print(Polynomial(1, 2, 1) + Polynomial(1, 4, 5, 6))


# D.differentiate(3)
#
# print(C.__add__(D))
#
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)




