import numpy as np
N = (np.linspace(1,100,100)**2).reshape((10,10))
x = N%3 == 0
y = N[N%3==0]


