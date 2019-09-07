class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b

    def abslt(self):
        return pow(self.real ** 2 + self.imaginary ** 2, 0.5)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary, self.imaginary * other.real + self.real * other.imaginary)

    def __print__(self):
        print(self.real, self.imaginary)


C = Complex(10, 8)
D = Complex(-2, -1)
E = Complex(0.5, 0)
S = C + D*E




