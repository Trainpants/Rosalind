# SUBS - Finding a Motif in DNA
# find the location of substring in larger string 

with open("rosalind_subs.txt") as datafile:
    data = datafile.read()

data = data.split("\n")
S = data[0]
T = data[1]

#S = "GATATATGCATATACTT"
#T = "ATAT"

subs = ""

for i in range(len(S)-len(T)):
    if S[i:(i+len(T))] == T:
        subs += str(i+1) + " "

print(subs)

