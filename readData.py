# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Python program that can be executed to report whether particular
# python packages are available on the system.

import matplotlib.pyplot as plt
import scipy
import numpy as np
import wave
import sys
import glob
import pandas as pd


data2 = scipy.io.wavfile.read('/home/doltsinis/Documents/Composition/acoustic data/acoustic 1/180108151705.wav')
data = wave.read('/home/doltsinis/Documents/Composition/acoustic data/acoustic 1/180108151705.wav')

plt.plot(data2[1])

print(glob.glob('/home/doltsinis/Documents/Composition/acoustic data/acoustic 1/*.wav'))
fileNames = sorted(glob.glob('/home/doltsinis/Documents/Composition/acoustic data/acoustic 1/*.wav'))

data = np.ones(len(scipy.io.wavfile.read(fileNames[1])), len(glob.glob('/home/doltsinis/Documents/Composition/acoustic data/acoustic 1/*.wav')))

for i in range(3):
    print(i)
    tempData = (scipy.io.wavfile.read(fileNames[i]))
    test = tempData[1]
    data = np.concatenate(data,test)
    
    data = np.asarray(tempData[i])
    
    plt.figure
    plt.plot(data[1])
    plt.legend







