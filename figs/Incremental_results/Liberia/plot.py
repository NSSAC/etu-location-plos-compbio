import numpy as np
import matplotlib.pyplot as plt

N = 68



kmed_opt = []

kmed_online = []


X = [2,4,6,8,10,12,14,16]

def normalize(a):
    a[:] = [x / 3600.0 for x in a]

normalize(kmed_opt)
normalize(kmed_online)


#plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('weeks')
ax.set_ylabel('average cost (hours)')

plt.plot(X, kmed_opt, 'bs-', label='k-median solution (offline, fractional lower-bound)')
plt.plot(X, kmed_online, 'rs-', label='k-median solution (online, integral)')

#plt.xlim( 0, 15 )
plt.ylim( 0, 4.5 )

plt.legend()

plt.savefig('plot_kmed_cap')



