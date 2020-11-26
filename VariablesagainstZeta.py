#imports
import matplotlib.pyplot as plt
import numpy as np

#average velocity function
def avgvel():
    #creating empty lists
    avgvel=[]
    yerrv = []
    vals=[]
    delimiter = "\n"
    #reading in average velocity values for each zeta
    for i in range(0, 25, 1):
        vals = []
        with open('finalveloicites'+str(i)+'.txt') as f:
            for line in f:
                vals.append(float(line))
            #finding the average to get a final velocity at each zeta
            avgval = np.mean(vals)
        #appending to list of average velocities
        avgvel.append(avgval)
        #finding error on the average velocity value
        std = np.std(vals)
        yerrv.append(std)
    return avgvel, yerrv

#average order parameter function
def avgord():
    #creating empty lists
    avgord = []
    vals = []
    yerro = []
    delimiter = "\n"
    #reading in average order values for each zeta
    for i in range(0, 25, 1):
        vals = []
        with open ('finalorders'+str(i)+'.txt') as f:
            for line in f:
                vals.append(float(line))
            #finding average to get final order parametr at each zeta
            avgval = np.mean(vals)
        #appending to list of average order parameters
        avgord.append(avgval)
        #finding error on average order parameter magnitude
        err = np.std(avgord)
        yerro.append(err)
    return avgord, yerro

#standard deviation of density function
def stdden():
    #creating empty lists
    stdden = []
    vals = []
    yerrd = []
    delimiter = "\n"
    #reading in standard deviation density values for each zeta
    for i in range(0, 25, 1):
        vals = []
        with open ('finaldensities'+str(i)+'.txt') as f:
            for line in f:
                vals.append(float(line))
                #finding the standard deviation of this list
            stdval = np.std(vals)
        #appending to list of final standard deviation for density at each zeta
        stdden.append(stdval)
        #finding error on each standard deviation density value
        err = np.std(stdden)
        yerrd.append(err)
    return stdden, yerrd

#average veloicty for lower values of zeta
def passivevel():
    #creating empty lists
    avgvelp=[]
    yerrp = []
    vals=[]
    delimiter = "\n"
    #reading in velocity data for the smaller values of activity
    for i in range(0, 11, 1):
        vals = []
        with open('finalveloicitesp'+str(i)+'.txt') as f:
            for line in f:
                vals.append(float(line))
            #finding the average velocity value
            avgval = np.mean(vals)
        #appending these values to a list
        avgvelp.append(avgval)
        #finding the error on the value using the standard deviation of the list of values averages
        std = np.std(vals)
        yerrp.append(std)
    return avgvelp, yerrp


#creating a list of zeta values as zeta values have different intervals
zeta0 = 0
zeta2 = np.arange(0.005, 0.1005, 0.005)
zeta1 = np.arange(0.001, 0.005, 0.001)
zetapassive = np.arange(0, 0.0011, 0.0001)
#combining the individual zeta ranges with each other
zeta = np.hstack((zeta0, zeta1, zeta2)).ravel()
#calling functions
avgvel, yerrv = avgvel()
avgord, yerro = avgord()
stdden, yerrd = stdden()
avgvelp, yerrp = passivevel()

#plotting graphs of variables against zeta with errors on each point
plt.plot(zeta, avgvel)
plt.title('Average velocity against Activity Coefficient')
plt.xlabel('Activity coefficient(simulation units)')
plt.ylabel('Average modulus velocty (Simulation Units)')
plt.errorbar(zeta, avgvel, yerr=yerrv, fmt = '.k')
plt.show()
plt.plot(zeta, avgord)
plt.title('Average Order Parameter Magnitude against Activity Coefficient')
plt.xlabel('Activity coefficient (simulation units)')
plt.ylabel('Average Order Parameter Magnitude (Simulation Units)')
plt.errorbar(zeta, avgord, yerr=yerro, fmt = '.k')
plt.show()
plt.plot(zeta, stdden)
plt.title('Standard Deviation of Density against Activity Coefficient')
plt.xlabel('Activity coefficient (simulation units)')
plt.ylabel('Standard Deviation of Density (Simulation Units)')
plt.errorbar(zeta, stdden, yerr=yerrd, fmt = '.k')
plt.show()
plt.plot(zetapassive, avgvelp)
plt.title('Average Velocity against Activity Coefficient for Lower Values')
plt.xlabel('Activity coefficient (simulation units)')
plt.ylabel('Average modulus velocity (simulation units)')
plt.errorbar(zetapassive, avgvelp, yerr=yerrp, fmt = '.k')
plt.show()
