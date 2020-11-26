import matplotlib.pyplot as plt
import numpy as np

#pearson coefficient for order density function
def pearson_od():
    #creating empty lists
    avgpearsonod = []
    yerrod = []
    vals = []
    delimiter = "\n"
    for i in range(1, 25, 1):
    #reading in pearson data for each value of zeta
        vals = []
        with open('pearsonordden' +str(i)+'.txt') as f:
            for line in f:
                vals.append(float(line))
            #finding average pearson value at each zeta
            avgval = np.mean(vals)
        #appending values to a list
        avgpearsonod.append(avgval)
        #finding error on these values
        std = np.std(vals)
        yerrod.append(std)
    return avgpearsonod, yerrod

#pearson coefficient for flow density function
def pearson_fd():
    #ceating empty lists
    avgpearsonfd = []
    yerrfd = []
    vals = []
    delimiter = "\n"
    for i in range(1, 25, 1):
    #reading in pearson data for each value of zeta
        vals = []
        with open('pearsonfloden' +str(i)+'.txt') as f:
            for line in f:
                vals.append(float(line))
            #finding average pearson at each zeta
            avgval = np.mean(vals)
        #appending these values to a list
        avgpearsonfd.append(avgval)
        #finding the error on this value using standard deviation of the range of values
        std = np.std(vals)
        yerrfd.append(std)
    return avgpearsonfd, yerrfd

#pearson coefficient for flow order function
def pearson_fo():
    #creating empty lists to put data in
    avgpearsonfo = []
    yerrfo = []
    vals = []
    delimiter = "\n"
    for i in range(1, 25, 1):
    #reading in peatson data for each value of zeta
        vals = []
        with open('pearsonfloord' +str(i)+'.txt') as f:
            for line in f:
                vals.append(float(line))
            #finding avergae of the pearson values at each zeta
            avgval = np.mean(vals)
        #appending these values to a list
        avgpearsonfo.append(avgval)
        #finding error of each value at each value of zeta
        std = np.std(vals)
        yerrfo.append(std)
    return avgpearsonfo, yerrfo

#creating different lists of zeta values as zeta has different intervals
zeta2 = np.arange(0.005, 0.1005, 0.005)
zeta1 = np.arange(0.001, 0.005, 0.001)
#combinging these zeta ranges to create one list of zeta values with different intervals
zeta = np.hstack((zeta1, zeta2)).ravel()

#calling functions
avgpearsonod, yerrod = pearson_od()
avgpearsonfd, yerrfd = pearson_fd()
avgpearsonfo, yerrfo = pearson_fo()
#plotting graphs of variables against zeta with errors on each point 
plt.plot(zeta, avgpearsonod)
plt.title('Pearson Correlation Coefficent for Order Parameter and Density against Activity Coefficient')
plt.xlabel('Activity (simulation units)')
plt.ylabel('Pearson correlation coefficent')
plt.errorbar(zeta, avgpearsonod, yerr=yerrod, fmt = '.k')
plt.show()
plt.plot(zeta, avgpearsonfd)
plt.title('Pearson Correlation Coefficent for Flow Parameter and Density against Activity Coefficient')
plt.xlabel('Activity (simulation units)')
plt.ylabel('Pearson correlation coefficent')
plt.errorbar(zeta, avgpearsonfd, yerr=yerrfd, fmt = '.k')
plt.show()
plt.plot(zeta, avgpearsonfo)
plt.title('Pearson Correlation Coefficent for Flow Parameter and Order Parameter against Activity Coefficient')
plt.xlabel('Activity (simulation units)')
plt.ylabel('Pearson correlation coefficent')
plt.errorbar(zeta, avgpearsonfo, yerr=yerrfo, fmt = '.k')
plt.show()
