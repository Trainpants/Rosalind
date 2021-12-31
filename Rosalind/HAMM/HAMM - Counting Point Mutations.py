# HAMM - Counting Point Mutations
# find "Hamming Distance" between two DNA strands
# number of pairs that don't match


with open("rosalind_hamm.txt") as datafile:
    data = datafile.read()

list = data.split("\n")
S = str(list[0])
T = str(list[1])

#S = "GAGCCTACTAACGGGAT"
#T = "CATCGTAATGACGGCCT"
D = 0

for i,e in enumerate(S):
    if e != T[i]:
        D += 1

print(D)



