#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

arr1 = list(np.random.rand(100))
arr2 = list(np.random.rand(100))

f, axarr = plt.subplots(2,2)

axarr[0].plot(arr1[0:24], arr2[0:24])
plt.show()