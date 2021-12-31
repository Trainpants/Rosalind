# IPRB
# nine events: DD, DH, DR, HD, HH, HR, RD, RH, RR
# each event has a probability of outcome of offspring with Dom allele

#sampledata = "2 2 2"
data = "24 19 26"
pop = data.split(" ")
D = int(pop[0]) # Dominant homo
H = int(pop[1]) # Hetero
R = int(pop[2]) # Recessive homo
T = D + H + R # Total population

# all events with D individual have outcome with dom allele offspring

# Probabilities of events with possibilities of RR offspring outcomes
PHH = H/T * (H-1)/(T-1) # dom allele offspring outcome with 3/4 probability 
PHR = H/T * R/(T-1) # dom  allele outcome with 1/2 probability // PHR == PRH
PRR = R/T * (R-1)/(T-1) # always RR allele offspring outcome

# total probability of outcome  with D allele
PD = 1 - PRR - PHR - PHH/4 # 2*PHR/2 = PHR
print(PD)
