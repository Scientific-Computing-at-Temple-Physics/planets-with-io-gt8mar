# Marcus Forst
# Weights on Different Planets


# Inputs: planet name, altitude above avg radius, explorer mass
pname=input.('What is the name of the planet?')
alt=input.('What is the altitude above the average radius of the planet?')
mass=input.('What is the mass of the explorer?')

f=open("planet_data.dat", "r")

for line in f:
  data=line.split(";")

if pname==data[0]:
  then r=data[1] and den=data[2] 
