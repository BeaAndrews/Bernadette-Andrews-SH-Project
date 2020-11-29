import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
from unidip import UniDip
import unidip.dip as dip

def orders():
    col_num = 14
    col_data = []
    orders =[]
    delimiter = " "
    for i in range(0, 236000, 500):
    #reading in the list of order parameter magnitudes for each Qtensor file
        with open('Qtensor0.'+str(i)+'.txt') as f:
            for line in f:
                split_string = line.split(delimiter)
                if len(split_string) >= col_num:
                    #appending the data to a list
                    col_data.append(float(split_string[col_num]))
        #finding the average order parameter for each Qtensor file
        order = np.mean(col_data)
        #emptying the list so the previous value is not overwritten
        col_data = []
        #appending average orders to a list
        orders.append(order)
    return orders

def velocities():
    #creating empty lists for data
    col_num1 = 9
    col_num2 =10
    col_data1 = []
    col_data2 = []
    velocities =[]
    delimiter = " "
    for i in range(0, 236000, 500):
    #reading in the list of velocity y's and z's for Q tensor file
        with open('Qtensor0.'+str(i)+'.txt') as f:
            for line in f:
                split_string = line.split(delimiter)
                if len(split_string) >= col_num1:
                    #appending data to a list
                    col_data1.append(float(split_string[col_num1]))
                    col_data2.append(float(split_string[col_num2]))
        #finding the average velocity of all the particles in that list
        a = [x**2 for x in col_data1]
        b = [x**2 for x in col_data2]
        velocity = []
        for num1, num2 in zip(a, b):
            velocity.append((num1+num2)**(1/2))
        #finding the average velocity
        velocity = np.mean(velocity)
        #emptying the columns so the for loop doesn't override previous values
        col_data1 = []
        col_data2 = []
        #appending the average velocity at each Qtensor file to a list
        velocities.append(velocity)
    return velocities

#defining Gaussian function in order to fit a curve to order param Histogram
def guas(x, mu, sigma, a):
    guas = a*(np.exp(-(x-mu)**2/(2*sigma**2)))
    return guas

#defining double Gaussian function to fit to velocity histogram
def guas2(x, mu1, sigma1, a1, mu2, sigma2, a2):
    guasa = a1*(np.exp(-(x-mu1)**2/(2*sigma1**2)))
    guasb = a2*(np.exp(-(x-mu2)**2/(2*sigma2**2)))
    guas2 = guasa +guasb
    return guas2

orders = orders()
#plotting histrogram of orders
yo, xo, _ = plt.hist(orders, bins = 70)
#placing inital parameters into fit so scipy can estimate
popto, pcovo = curve_fit(guas, xo[:-1], yo, p0=[0.42 ,0.05, np.amax(yo)])
#plotting the optimized curve found by scipy
plt.plot(xo[:-1], guas(xo[:-1], *popto))
#finding errors on the parameters
perro = np.sqrt(np.diag(pcovo))
print('meano = ' +str(popto[0]))
print('sigmao = ' +str(popto[1]))
print('heighto = ' +str(popto[2]))
print(perro)
plt.show()
velocities = velocities()
#plotting historgam of velocities
yv, xv, _ = plt.hist(velocities, bins = 70)
#placing inital parameters into fit so scipy can estimate
poptv, pcovv = curve_fit(guas2, xv[:-1], yv, p0=[0.1 ,0.01, 36, 0.13, 0.01, 27])
#plotting the optimized curve found by scipy
plt.plot(xv[:-1], guas2(xv[:-1], *poptv))
#finding errors on the parameters
perrv = np.sqrt(np.diag(pcovv))
print('meanv1 = ' +str(poptv[0]))
print('sigmav1 = ' +str(poptv[1]))
print('heightv1 = ' +str(poptv[2]))
print('meanv2 = ' +str(poptv[3]))
print('sigmav2 = ' +str(poptv[4]))
print('heightv2 = ' +str(poptv[5]))
print(perrv)
#finding the dip test value for the two seperate Gaussians to test independence 
xv = np.msort(xv)
print(dip.diptst(xv))
plt.show()
