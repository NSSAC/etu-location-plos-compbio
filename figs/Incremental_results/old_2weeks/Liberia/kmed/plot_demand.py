import numpy as np
import matplotlib.pyplot as plt

N = 68



demand = [50,
272,
1205.5,
3210.25,
2684,
1712.25,
1046.25,
587.75]


X = [2,4,6,8,10,12,14,16]


#plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('weeks')
ax.set_ylabel('#patients')

plt.plot(X, demand, 'bs-', label='demand')

#plt.xlim( 0, 15 )

plt.legend()

plt.savefig('plot_demand')



