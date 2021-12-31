# 03 - Complementing a Strand of DNA

with open("rosalind_revc.txt") as datafile:
    DNA = datafile.read()

#DNA = "AAAACCCGGT"

revcomp = ""

revdna = DNA[::-1]

for i in revdna:
    if i == "A":
        revcomp += "T"
    elif i == "T":
        revcomp += "A"
    elif i == "G":
        revcomp += "C"
    elif i == "C":
        revcomp += "G"

print(revcomp)
