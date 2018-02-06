# Marcus Forst
# Weights on Different Planets


# Inputs: planet name, altitude above avg radius, explorer mass
pname=input.('What is the name of the planet?')
alt=input.('What is the altitude above the average radius of the planet?')
mass=input.('What is the mass of the explorer?')

f=open("planet_data.dat", "r")

for line in f:
  if pname==[0]:
    then r=[1] and den=[2] 
