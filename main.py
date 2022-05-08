import numpy as np
import matplotlib.pyplot as plt
x= np.array([1,3,5])
y=[2,4,6]
z=np.exp(x)
w=np.exp(y)
plt.plot(x,z,color="blue",marker='*')
plt.plot(y,w,color="red",marker='o')
plt.xlabel("X Axis--------->")
plt.ylabel("Y Axis--------->")
plt