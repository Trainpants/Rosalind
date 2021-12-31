# FIB - Fibonacci's rabbits
# Given k pairs of rabbits in a litter, what is pop after n months

n = 31
k = 3

pop = [1,1]
for i in range(n-2):
    pop.append(pop[i]*k+pop[-1])

print(pop[-1])
