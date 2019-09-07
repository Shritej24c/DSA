# BT3051 Assignment 2e
# Roll number: BE14B004
# Collaborators: None
# Time: 00:20


from fractions import _gcd


class Rational:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.d = _gcd(self.n1, self.n2)
        self.dn1 = self.n1 // self.d
        self.dn2 = self.n2 // self.d

    def __add__(self, other):
        return Rational(self.dn1*other.dn2 + other.dn1*self.dn2, self.dn2*other.dn2)

    def __sub__(self, other):
        return Rational(self.dn1*other.dn2 - other.dn1*self.dn2, self.dn2*other.dn2)

    def __mul__(self, other):
        return Rational(self.dn1*other.dn1, self.dn2*other.dn2)

    def __truediv__(self, other):
        return Rational(self.dn1*other.dn2, self.dn2*other.dn1)

    def __repr__(self):
        if self.dn2 != 1:
            return "%d/%d" % (self.dn1, self.dn2)
        else:
            return "%d" % self.dn1

print(Rational(10, 20))
print(Rational(10, 20) + Rational(30, 20))


