#BT3051 Assignment 1a
#Roll number: BE14B004
#Collaborators: None
# Time: 3:15


import doctest
#mrna = "AUGUUUUGCAUUUAA"



def translate_DNA (mrna, translation_table = "RNA_TABLE.txt"):
    """>>> translate_DNA('AUGCUU')
ML"""
    RNA = []
    dict_codon = {}
    sequence = []
    if mrna[:3] != "AUG":
        print("The RNA sequence has to start from Methionine (AUG).")

    elif len(mrna.strip()) % 3 != 0:
        print("The sequence length should be a multiple of 3")

    for codon in range(0, len(mrna), 3):
        RNA.append(mrna[codon:codon+3])

    rna_table = open("RNA_TABLE.txt", "r")
    for line in rna_table.readlines():
        lines = line.split()
        for i in range(len(lines)):
            if i % 2 == 0:
                dict_codon[lines[i]] = lines[i + 1]
    rna_table.close()

    for icodon in range(len(RNA)):
        if dict_codon[RNA[icodon]] == "Stop":
            break
        else:
            sequence.append(dict_codon[RNA[icodon]])

    print("".join(sequence))

print(translate_DNA('AUGCUU'))
if __name__ == "__main__":
    doctest.testmod(verbose=True)








