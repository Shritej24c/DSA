from collections import Counter


Sq = "TCAATGCATGCGGGTCTATATGCAT"

str = "Sequence\n"

List = []

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

print(str)


def get_GC(sq):
    list = []
    for i in range(len(sq)):
        list.append(sq[i])
    counter = Counter(list)
    dict = {}
    for k, v in counter.items():
        dict[k] = v
    total = 0
    gc_content = ((dict['G'] + dict['C']) / (dict['G'] + dict['C'] + dict['T'] + dict['A'])) * 100
    return gc_content

def get_base_counts(sq):
    list = []
    for i in range(len(sq)):
        list.append(sq[i])
    counter = Counter(list)
    #print(counter.items())
    dict = {}
    for k, v in counter.items():
        dict[k] = v
    return dict

#print(get_base_counts(Sq))
#print(get_GC(Sq))

#print(get_GC("CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"))
#print(get_GC("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"))

f = open("rosalind_gc.txt", 'r')
n_strings = 0
pos_strings = []
name_strings = []
lines = f.readlines()
for l in range(len(lines)):
    if lines[l][0] == ">":
        n_strings += 1
        pos_strings.append(l)
        name_strings.append(lines[l][1:].strip('\n'))

#print(name_strings)
#print(lines)
pos_strings.append(len(lines))
#print(pos_strings)

f.close()
gc_content = []
for i in range(len(pos_strings) - 1):
    string = "".join(lines[pos_strings[i] + 1: pos_strings[i + 1]])
    gc_content.append(get_GC(string))

#print(gc_content)

dna1 = ""
dna2 = ""
hamming = 0

for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
        hamming += 1

print(hamming)




