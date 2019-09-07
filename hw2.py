import doctest
from collections import Counter


class DNA:

    def __init__(self, fasta=None, string=None):
        if fasta != None:
            self.fasta = open(fasta)
            self.sequence = self.fasta.readlines()
            self.sequence.remove(self.sequence[0])
            self.sq = ''.join(self.sequence)
        else:
            self.sq = string

    def get_comple_strand(self):
        """>>> DNA(None, 'TCAATGCATGCGGGTCTATATGCAT').get_comple_strand()
ATGCATATAGACCCGCATGCATTGA"""
        list = []
        x = -1
        while x >= -len(self.sq):
            if self.sq[x] == "A":
                list.append("T")
            elif self.sq[x] == "G":
                list.append("C")
            elif self.sq[x] == "T":
                list.append("A")
            elif self.sq[x] == "C":
                list.append("G")
            x -= 1
        str = ""
        for i in list:
            str += i
        return DNA(None, str)

    def __repr__(self):
        return self.sq

    def get_base_counts(self):
        """>>> DNA(None, "ATGC\n").get_base_counts()== {'G': 1, 'C': 1, 'T': 1, 'A': 1}
True"""
        list = []
        for i in range(len(self.sq)):
            list.append(self.sq[i])
        counter = Counter(list)
        dict = {}
        for k, v in counter.items():
            dict[k] = v
        return dict

    def transcribe(self):
        """>>> DNA(None, "ATGC").transcribe()
'AUGC'"""
        list = []
        for x in range(len(self.sq)):
            list.append(self.sq[x])
            if self.sq[x] == "T":
                list.remove(self.sq[x])
                list.append("U")
        string = ""
        for i in range(len(self.sq)):
            string += list[i]
        return string

    def get_GC (self):
        """>>> DNA(None, "ATGC").get_GC()
50.0"""
        list = []
        for i in range(len(self.sq)):
            list.append(self.sq[i])
        counter = Counter(list)
        dict = {}
        for k, v in counter.items():
            dict[k] = v
        gc_content = ((dict['G'] + dict['C']) / (dict['G'] + dict['C'] + dict['T'] + dict['A'])) * 100
        return gc_content

    def locate_restriction_sites(self):
        """>>> DNA(None, 'TCAATGCATGCGGGTCTATATGCAT').locate_restriction_sites()
[(4, 6), (5, 4), (6, 6), (7, 4), (17, 4), (18, 4), (20, 6), (21, 4)]"""
        result = []
        for i in range(len(self.sq)):
            for j in range(4, 13, 1):
                if i+j > len(self.sq):
                    break
                else:
                    og_sq = self.sq[i: i+j]
                    list = []
                    x = -1
                    while x >= -len(og_sq):
                        if og_sq[x] == "A":
                            list.append("T")
                        elif og_sq[x] == "G":
                            list.append("C")
                        elif og_sq[x] == "T":
                            list.append("A")
                        elif og_sq[x] == "C":
                            list.append("G")
                        x -= 1
                    comple_sq = ""
                    for k in list:

                        comple_sq += k
                    if (og_sq) == (comple_sq):
                        result.append((i+1, j))
        return result




C = DNA('DNA.fasta', None)
print(C.locate_restriction_sites())
print(C.get_GC())
print(C.get_base_counts())
print(C.get_comple_strand())
print(C.transcribe())
if __name__ == '__main__':
    D = DNA('DNA1.fasta', None)
    doctest.testmod(verbose=True)

