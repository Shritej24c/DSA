# BT3051 Assignment 0b
# Roll number: BE14B004
# Collaborators: None
# Time: 00:15

from collections import Counter

n = int(input("Enter a number :"))
lines = []
while n != 1:
    if n % 2 == 0:
        n //= 2
        lines.append("*")
    else:
        n = 3*n + 1
        lines.append("#")
    print(n)

print("length of lines = ", len(lines))
print(Counter(lines).items())
