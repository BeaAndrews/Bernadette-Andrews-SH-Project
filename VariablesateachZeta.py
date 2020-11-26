#imports
import matplotlib.pyplot as plt
import numpy as np

#velocity function
def velocities():
    #creating empty lists for data
    col_num1 = 9
    col_num2 =10
    col_data1 = []
    col_data2 = []
    velocities =[]
    delimiter = " "
    for i in range(0, 50500, 500):
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

#order parameter function
def orders():
    #creating empty lists for data
    col_num = 14
    col_data = []
    orders =[]
    delimiter = " "
    for i in range(0, 50500, 500):
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

#density function
def densities():
    #creating empty lists for data
    col_num = 17
    col_data = []
    densities =[]
    delimiter = " "
    for i in range(0, 50500, 500):
    #reading in the list of densities for each Qtensor file
        with open('Qtensor0.'+str(i)+'.txt') as f:
            for line in f:
                split_string = line.split(delimiter)
                if len(split_string) >= col_num:
                    #appending the data to a list
                    col_data.append(float(split_string[col_num]))
                    #finding the standard deviation of the density at each Qtensor file
        density = np.std(col_data)
        #emptying the list
        col_data = []
        #appending standard deviation of densities to a list
        densities.append(density)
    return densities

#cutting down the data to remove the equilbirating period from the data list for each variable
fluc_velocities = velocities()[19:]
fluc_orders = orders()[19:]
fluc_densities = densities()[19:]
ut file
f = open('finalveloicites2.txt', 'w')
for i in range(len(fluc_velocities)):
    f.write(str(fluc_velocities[i])+'\n')
f.close()
#writing the final fluctuating average orders to an output file
f = open('finalorders2.txt', 'w')
for i in range(len(fluc_orders)):
    f.write(str(fluc_orders[i])+'\n')
f.close()
#writing the final standard deviation of density valuesto an output file
f = open('finaldensities2.txt', 'w')
for i in range(len(fluc_densities)):
    f.write(str(fluc_densities[i])+'\n')
f.close()
#plotting the graphs of each variable against simulation time
plt.plot(range(0,50500, 500), velocities())
plt.title('Plot of the Average Velocity Against Time at Activity coefficient 0.01')
plt.xlabel('Time (Simualtion units)')
plt.ylabel('Average Velocity (Simulation units)')
plt.show()
plt.plot(range(0,50500, 500), orders())
plt.title('Plot of the Average Order Parameter Magnitude Against Time at Activity coefficient 0.01')
plt.xlabel('Time (Simualtion units)')
plt.ylabel('Average Order Parameter (Simulation units)')
plt.show()
plt.plot(range(0,50500, 500), densities())
plt.title('Plot of the Standard Deviation of Density Against Time at Activity coefficcient 0.01')
plt.xlabel('Time (Simualtion units)')
plt.ylabel('Standard Deviation of Density (Simulation units)')
plt.show()
