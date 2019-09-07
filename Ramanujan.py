
def ramanujan_num(n):
    for a in range(0, n):
        for b in range(0, n):
            for c in range(0, n):
                for d in range(0, n):
                    if a**3 + b**3 == c**3 + d**3 and a != b and a != c and a != d:
                        ramanujan_num = a**3 + b**3
                        return ramanujan_num

print(ramanujan_num(15))

