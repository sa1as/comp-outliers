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
import wave
import sys
import glob
import pandas as pd


data2 = scipy.io.wavfile.read('/home/saias/Documents/composition/acoustic data/acoustic 1/180108151705.wav')
data = wave.read('/home/doltsinis/Documents/Composition/acoustic data/acoustic 1/180108151705.wav')
plt.plot(data2[1])

paths = ('/home/saias/Documents/composition/acoustic data/acoustic 1/*.wav', '/home/doltsinis/Documents/Composition/acoustic data/acoustic 1/*.wav')
path = paths[0]
fileNames = sorted(glob.glob(path)) # get the file names from the whole folder in path
data = np.ones([len(scipy.io.wavfile.read(fileNames[0])[1]), len(glob.glob(path))]) # intialize data matrix based on folder size


for i in range(len(glob.glob(path))) :
    print(i)
    tempData = (scipy.io.wavfile.read(fileNames[i])[1])
    data[:,i] = tempData
    
plt.figure(i)
plt.plot(data[:,100])    

# end of loop

    

    np.concatenate(data,tempData)
    tempData.shape
    data.shape    
    data = np.asarray(tempData[i])
    






