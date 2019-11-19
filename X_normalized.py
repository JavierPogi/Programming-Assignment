import numpy as n
x=n.random.random(5)
for q in range (1,6):
    x = n.vstack((x,n.random.random(5)))
    y = (x-x.mean())/x.std()
    print(y)