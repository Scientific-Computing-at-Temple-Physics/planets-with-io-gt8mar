# Marcus Forst
# Weights on Different Planets


# Inputs: planet name, altitude above avg radius, explorer mass
import math as ma
pname= input("What is the name of the planet?")
alt=float(input('What is the altitude above the average radius of the planet?'))
mass=float(input('What is the mass of the explorer?'))
G=6.674*(10**(-11))

# This reads the data file
f=open("planet_data.dat", "r")

# Ignores the first line
for line in f:
	if line[0]=="#":  continue
	data = line.split(";")	#splits the line into lists using the delimeter ;

	if data[0].upper() == pname.upper(): #selects the correct line of data for the given planet
		prad = data[1].split() #selects the numerical value for the radius
		den = data[2].split()  #selects the numerical value for the density
		break #stops the program from running needlessly past the selected planet

prad_n = float(prad[0])#makes the numerical values floats
den_n = float(den[0])
si_prad = prad_n*1000 #converts to SI
si_den = den_n*1000

m_planet = float(si_den*(4.0/3.0)*ma.pi*(si_prad**3)) #computes the mass of the planet
Fg = round((G*m_planet*mass)/((si_prad+alt)**2),3) #computes the force due to gravity (weight)
grav = round((G*m_planet)/((si_prad+alt)**2),3) #computes the acceleration due to gravity

print ("The weight of the explorer is", Fg, "N")
print ("The acceleration due to gravity is", grav, "g's")
# Outputs: the explorer's weight, the Gravitational acceleration in g's

f.close()
