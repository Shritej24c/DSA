print("Hello World")

a = ('B', 'T', 3, 0, 5, 1)
#print(a[1])
#print(.1 + .2)


def f(x):
    if x % 2 == 0:
        return (x) / 2
    elif x % 2 == 1:
        return 3 * x + 1


#print(f(3))


def haystack(s, t):
    m = len(s)
    n = len(t)
    a = []
    for i in range(m):
        if s[i:i + n] == t:
            a.append(i + 1)
        else:
            pass
    return a


#print(haystack(
 #   'AGAGTTGAGAGTTGAAGAGTTGTAAGAGTTGGAGAGTTGATAGAGTTGAGAGTTGAAGAGTTGAGTAGAGTTGCAGAGTTGTAGAGTTGCAGAGTTGGGGAGAGTTGAGAGTTGGTCTATGAGAGTTGGGAAAGAGTTGAACTAGAGTTGAGAGTTGATTGAACGTTTAGAGTTGAGAGTTGAGAGTTGGCCCCTAGAGTTGAGAGTTGAGAGTTGCCGAGAGTTGTGAGAGTTGAGAGTTGAGAGTTGCAGAGTTGGAGAGTTGAGAGTTGATCAGAGTTGAGAGTTGTAGAGTTGCTCGAGAGTTGCCTTATAAGAGTTGTAGAGTTGTAGAGTTGAACTCAGAGTTGAGCTAAGAGTTGGAGAGTTGCGCCCGAAGAGTTGCAGAGTTGGTAGAGTTGTGGCTAGAGTTGTAGAGTTGACTTAGAGTTGGAGAGTTGTGGAGAGAGTTGGGAGAGTTGAGAGTTGAGAGTTGCTAGAGTTGAGAGTTGGAGAGTTGAGAGTTGACAGAGTTGCAGAGTTGGGCTGGGAGTGCAGAGTTGAGAGTTGACGTAGAGTTGAAACAGAGTTGGCTTAGAGTTGACAGAGTTGCAAGTTAGAGTTGGAGAGTTGAGAGTTGCACTTGCACAAGAGTTGTAGAGTTGAGAGTTGAGAGTTGTATAGAGTTGAGAGTTGCATGAGAGTTGAGAGTTGCATCGAGAGTTGAAGAGTTGAGAGTTGGCAAGACTGAACAGAGTTGACCCAAGAGTTGTAGAGTTGGCTTTAGAGTTGTATTGGAGAGTTGGAGAGTTGAGAGTTGAGAGTTGGCAGAGTTGGAGAGTTGCTAGCACTTGAGAGTTGTTAGAGTTGGATCTAGTGTAGAGTTGGAGAGTTGAGAGTTGAGAGTTGAGAGTTGAGAGTTG',
  #  'AGAGTTGAG'))

def complement(Sq):
    List = []
    str = ""
    x = -1
    while x >= -len(Sq):
        if Sq[x] == "A":
            str += "T"
        elif Sq[x] == "G":
            str
        elif Sq[x] == "T":
            List.append("A")
        elif Sq[x] == "C":
            List.append("G")
        x -= 1

    for i in List:
        str += i
    return str
pos = []
length = []
def palindrome(s):
    for i in range(len(s)):
        for j in range(4, 12):
            a = s[i: i+j]
            b = s[i + j - 1: i-1: -1]
            if complement(a) == b:
                print(a)
                print(b)



ste = "TCAATGCATGCGGGTCTATATGCAT"
print(len(ste))

print(palindrome("TCAATGCATGCGGGTCTATATGCAT"))

protein = open('protein.txt','w')
protein.write('shritej')


















