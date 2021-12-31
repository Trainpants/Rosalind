# 01 Counting DNA Nucleotides

with open("rosalind_dna.txt") as datafile:
    DNA = datafile.read()


A = DNA.count("A")
C = DNA.count("C")
G = DNA.count("G")
T = DNA.count("T")

output = str(A) + " " + str(C) + " " + str(G) + " " + str(T)
print(output)

