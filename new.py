import numpy as np
import matplotlib.pyplot as plt

a = np.linspace (0.001, 3.999, 1000)
x = np.array([0,1])
k  = 1000
x = np.empty(shape=(1,k))

for index, value in  enumerate(a):

    print(value)
    for i in range (1,k):
        x[k] = a * x[k-1] * (1 - x [k-1])
       

    



    