#BT3051 Assignment 1a
#Roll number: BE14B004
#Collaborators: None
# Time: 2:45



import doctest

def read_fasta(fname):
    sequence_name = ""
    sequence = ""
    fname = open("Fasta.faa", "r")
    list = fname.readlines()
    sequence_name += list[0]
    list.remove(sequence_name)
    for lines in list:
        sequence += lines.strip("\n")
    fname.close()
    return zip([sequence_name], [sequence])


def compute_protein_mass(sequence):
    '''>>> compute_protein_mass('SKADYEK')
839.391924'''

    mol_weight = {}
    data = open("protein.txt", "r")
    for lines in data.readlines():
        line = lines.split()
        mol_weight[line[0]] = line[1]
    protein_weight = 0
    i = 0
    while i < len(sequence):
        if sequence[i] in mol_weight:
            protein_weight += float(mol_weight[sequence[i]])
        i += 1
    data.close()
    return protein_weight + 18


if __name__ == '__main__':
    doctest.testmod(verbose = True)
    for seq_name, seq in read_fasta("Fasta.faa"):
        print(seq_name, compute_protein_mass(seq))
