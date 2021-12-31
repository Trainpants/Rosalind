# PROT - Translating RNA into Protein
# given a mRNA string, return the protein string encoded by into

with open("RNA_codon_table.txt") as datafile:
    table = datafile.read()

table = table.split("\n")
D = []
for j in table:
    D.append(j.split(" "))
codons = dict(D)

with open("rosalind_prot.txt") as datafile:
    RNA = datafile.read()

#RNA = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
PROT = ""

for i in range(3,len(RNA),3):
    P = codons[RNA[i-3:i]]
    if P != "Stop":
        PROT += P
    else:
        break

print(PROT)