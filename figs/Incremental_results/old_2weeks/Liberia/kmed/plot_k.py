import numpy as np
import matplotlib.pyplot as plt

N = 68



kmed_k = [5,7,9,11,13,15,17,19]


X = [2,4,6,8,10,12,14,16]

def normalize(a):
    a[:] = [x / 3600.0 for x in a]



#plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('weeks')
ax.set_ylabel('k')

plt.plot(X, kmed_k, 'bs-', label='k')

#plt.xlim( 0, 15 )

plt.legend()

plt.savefig('plot_k')



