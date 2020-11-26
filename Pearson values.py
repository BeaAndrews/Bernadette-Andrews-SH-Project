#imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

#pearson correlation order density function
def ordden():
    #creating empty lists
    col_num1 = 14
    col_num2 = 17
    density = []
    order = []
    pearsonod = []
    delimiter = " "
    for i in range(500, 50500, 500):
    #reading in order and density data from each Q tensor file
        with open('Qtensor0.'+str(i) +'.txt') as f:
            for line in f:
                split_string = line.split(delimiter)
                if len(split_string) >= col_num1:
                    #appending data to lists
                    density.append(float(split_string[col_num1]))
                    order.append(float(split_string[col_num2]))
        #finding the pearson correlation between the two variables for each Qtensor file
        a = pearsonr(order, density)
        #appending the pearson coefficients to a list
        pearsonod.append(a[0])
        #emptying the lists
        order = []
        density = []
    return pearsonod

#pearson correlation flow density function
def flowden():
    #creating empty lists
    col_num1 = 14
    col_num2 = 18
    density = []
    flow = []
    pearsonfd = []
    delimiter = " "
    for i in range(500, 50500, 500):
    #reading in flow parameter and density data from each Qtensor file
        with open('Qtensor0.'+str(i) +'.txt') as f:
            for line in f:
                split_string = line.split(delimiter)
                if len(split_string) >= col_num1:
                    #appending data to lists
                    density.append(float(split_string[col_num1]))
                    flow.append(float(split_string[col_num2]))
        #finding the pearson correlation between the two variables for each Qtensor file
        a = pearsonr(density, flow)
        #appending the pearson coefficients to a list
        pearsonfd.append(a[0])
        #emptying the lists
        density = []
        flow = []
    return pearsonfd

#pearson correlation flow order function
def floword():
    #creating empty lists
    col_num1 = 17
    col_num2 = 18
    order = []
    flow = []
    pearsonfo = []
    delimiter = " "
    for i in range(0, 50500, 500):
    #reading in flow parameter and order parameter from each Qtensor file
        with open('Qtensor0.'+str(i) +'.txt') as f:
            for line in f:
                split_string = line.split(delimiter)
                if len(split_string) >= col_num1:
                    #appending data to lists
                    order.append(float(split_string[col_num1]))
                    flow.append(float(split_string[col_num2]))
        #finding pearson correlation between the two variables for each Qtensor file
        a = pearsonr(order, flow)
        #appending the pearson coefficient to a list
        pearsonfo.append(a[0])
        #emptying lists
        order = []
        flow = []
    return pearsonfo

#removing pearson coefficients for the equilbirating period of each Qtensor file so analysis is of flcutuation period
fluc_pearsonod = ordden()[19:]
fluc_pearsonfd = flowden()[19:]
fluc_pearsonfo = floword()[19:]

#writing the final pearson coefficients for each Qtensor file to an output file
f = open('pearsonordden6.txt', 'w')
for i in range(len(fluc_pearsonod)):
    f.write(str(fluc_pearsonod[i])+'\n')
f.close()
f = open('pearsonfloden6.txt', 'w')
for i in range(len(fluc_pearsonfd)):
    f.write(str(fluc_pearsonfd[i])+'\n')
f.close()
f = open('pearsonfloord24.txt', 'w')
for i in range(len(fluc_pearsonfo)):
    f.write(str(fluc_pearsonfo[i])+'\n')
f.close()
