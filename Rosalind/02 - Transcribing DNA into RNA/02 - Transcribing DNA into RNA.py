# 02 - Transcribing DNA into RNA

with open("rosalind_rna.txt") as datafile:
    DNA = datafile.read()

#DNA = "GATGGAACTTGACTACGTAAATT"

RNA = ""

for i in DNA:
    if i == "T":
        RNA += "U"
    else:
        RNA += i

print(RNA)





