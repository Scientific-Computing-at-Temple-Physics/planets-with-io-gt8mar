# Marcus Forst
# Weights on Different Planets


# Inputs: planet name, altitude above avg radius, explorer mass
import math as ma
pname=input.('What is the name of the planet?')
alt=input.('What is the altitude above the average radius of the planet?')
mass=input.('What is the mass of the explorer?')
G=6.754*10**-11

# This reads the file f
f=open("planet_data.dat", "r")

# This  
for line in f:
  if line[0]=="#":  continue
  data = line.split(";")

if data[0]==pname:
  then prad=data[1].strip(" km") and den=data[2].strip(" g/cm^3") 

prad_n= eval(prad)
den_n = eval("den")
si_prad=eval(prad_n/1000)
si_den=eval(den_n*1000)

m_planet = eval(si_den*(4/3)*ma.pi*(si_prad**3))
Fg = 

# Outputs: the explorer's weight, the Gravitational acceleration in g's
