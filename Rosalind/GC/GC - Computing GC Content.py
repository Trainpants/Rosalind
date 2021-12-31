# GC - Computing GC Content
# Percentage of DNA string that is 'C' or 'G'

with open("rosalind_gc.txt") as datafile:
    data = datafile.read()
FASTA = data[1::].split(">")
output = ["",0]

for i in FASTA:
    workvar = i.split("\n",1)
    workvar[1] = workvar[1].replace("\n","")
    GC = (workvar[1].count("C") + workvar[1].count("G")) / len(workvar[1]) * 100
    if GC > output[1]:
        output[0] = workvar[0]
        output[1] = GC

print(output[0])
print(output[1])
