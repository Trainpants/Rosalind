# CONS - Consensus and Profile
# find profile matrix and consensus string of given dna strings

with open("rosalind_cons.txt") as datafile:
    data = datafile.read()

fasta = data[1:].split(">")
dna = []
for n in fasta:
    m = n.split("\n",1)
    dna.append(m[1].replace("\n",""))
# This takes the data in fasta format and creates a list just of the dna sequences

dnaflip = []
for i in range(0,len(dna[0])):
    newstr = ""
    for j in range(0,len(dna)):
        newstr += dna[j][i]
    dnaflip.append(newstr)
# This for loop transposes dna into a new matrix dnaflip


A = "A: "
C = "C: "
G = "G: "
T = "T: "
cons = ""

for k in dnaflip:
    max = k.count("A")
    sym = "A"
    if k.count("C") > max:
        max = k.count("C")
        sym = "C"
    if k.count("G") > max:
        max = k.count("G")
        sym = "G"
    if k.count("T") > max:
        max = k.count("T")
        sym = "T"
    cons += sym
    A += str(k.count("A")) + " "
    C += str(k.count("C")) + " "
    G += str(k.count("G")) + " "
    T += str(k.count("T")) + " "

print(cons)
print(A)
print(C)
print(G)
print(T)















