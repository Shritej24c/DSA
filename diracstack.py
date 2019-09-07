from Binarysearch import Arraystack

def domath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "^":
        return pow(op1, op2)
    else:
        return op1 % op2

e = '((1+(4*3)/2)^7)'
operator = Arraystack()
operand = Arraystack()

for i in e:
    if i == ')':
         a = float(operand.pop())
         b = float(operand.pop())
         c = operator.pop()
         d = domath(c, b, a)
         operand.push(d)
    elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^' or i == '%':
        operator.push(i)
    elif i == '(':
        pass
    else:
        operand.push(i)
x = float(operand.pop())
y = float(operand.pop())
z = operator.pop()
#print(domath(z, y, x))

#print(Complex(1,2) + Complex(2,3))


