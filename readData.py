# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Python program that can be executed to report whether particular
# python packages are available on the system.

import matplotlib.pyplot as plt
import scipy.io.wavfile
import numpy as np
#import sys
import glob
import math

############################################# load data paths
pc = 1 # home pc -> 0, iti pc -> 1 
pathsData1 = ('/home/saias/Documents/composition/acoustic data/acoustic 1/*.wav', '/home/doltsinis/Documents/Composition/acoustic data/acoustic 1/*.wav')
pathdata1 = pathsData1[pc]

pathsData2 = ('/home/saias/Documents/composition/acoustic data/acoustic 2/*.wav', '/home/doltsinis/Documents/Composition/acoustic data/acoustic 2/*.wav')
pathdata2 = pathsData2[pc]

pathsData3 = ('/home/saias/Documents/composition/acoustic data/acoustic 3/*.wav', '/home/doltsinis/Documents/Composition/acoustic data/acoustic 3/*.wav')
pathdata3 = pathsData3[pc]

pathsData4 = ('/home/saias/Documents/composition/acoustic data/acoustic 4/*.wav', '/home/doltsinis/Documents/Composition/acoustic data/acoustic 4/*.wav')
pathdata4 = pathsData4[pc]

pathsData5 = ('/home/saias/Documents/composition/acoustic data/acoustic 5/*.wav', '/home/doltsinis/Documents/Composition/acoustic data/acoustic 5/*.wav')
pathdata5 = pathsData5[pc]
############################################
# outlier detection functions

def calculateModZ(data, MAD):
    Modz = 
    
    return ModZ

def calculateMAD(dataPoints, sampleNum):
    # provide a data vector, columns as new series
    median = np.median(dataPoints)
    absMedian = abs(dataPoints - median)
    MADValue = np.median(absMedian)
    return MADValue

###########################################


###########################################
# initial dat avisualization
dataPartition1 = 20
dataPartition2 = 20  
dataPartition3 = 20  
dataPartition4 = 20  
dataPartition5 = 20  

fileNames1 = sorted(glob.glob(pathdata1)) # get the file names from the whole folder in folder path
dataSensor1 = np.ones([len(scipy.io.wavfile.read(fileNames1[0])[1]), dataPartition1]) # intialize data matrix based on folder size
dataSensor1All = []

fileNames2 = sorted(glob.glob(pathdata2)) # get the file names from the whole folder in folder path
dataSensor2 = np.ones([len(scipy.io.wavfile.read(fileNames2[0])[1]), dataPartition2]) # intialize data matrix based on folder size

fileNames3 = sorted(glob.glob(pathdata3)) # get the file names from the whole folder in folder path
#dataSensor3 = np.ones([len(scipy.io.wavfile.read(fileNames3[0])[1]), dataPartition3]) # intialize data matrix based on folder size

fileNames4 = sorted(glob.glob(pathdata4)) # get the file names from the whole folder in folder path
dataSensor4 = np.ones([len(scipy.io.wavfile.read(fileNames4[0])[1]), dataPartition4]) # intialize data matrix based on folder size

fileNames5 = sorted(glob.glob(pathdata5)) # get the file names from the whole folder in folder path
#dataSensor5 = np.ones([len(scipy.io.wavfile.read(fileNames5[0])[1]), dataPartition5]) # intialize data matrix based on folder size

for i in range(dataPartition1) :

    tempData = (scipy.io.wavfile.read(fileNames1[i])[1])
    dataSensor1[:,i] = tempData
    dataSensor1All.append(tempData)

    tempData = (scipy.io.wavfile.read(fileNames2[i])[1])
    dataSensor2[:,i] = tempData

    #tempData = (scipy.io.wavfile.read(fileNames3[i])[1])
    #dataSensor3[:,i] = tempData

    tempData = (scipy.io.wavfile.read(fileNames4[i])[1])
    dataSensor4[:,i] = tempData

    #tempData = (scipy.io.wavfile.read(fileNames5[i])[1])
    #dataSensor5[:,i] = tempData
   

plt.plot(dataSensor1All[1:2])
##############################################

path = pathdata2 # choose data set to load
dataPartition = math.floor(len(glob.glob(path))/40)
#data = np.ones([len(scipy.io.wavfile.read(fileNames[0])[1]), len(glob.glob(path))]) # intialize data matrix based on folder size
fileNames = sorted(glob.glob(path)) # get the file names from the whole folder in folder path
data = np.ones([len(scipy.io.wavfile.read(fileNames[0])[1])-45001, dataPartition]) # intialize data matrix based on folder size
MADValues =[]

for i in range(dataPartition) :
    #print(i)
    tempData = (scipy.io.wavfile.read(fileNames[i])[1])
    data[:,i] = tempData[45000:-1]
    MADValues.append(calculateMAD(data[:,i],len(data[:,i])) )
    
plt.boxplot(MADValues)
MADValues[-1]
plt.plot(MADValues)   
plt.plot(data[:,5])


