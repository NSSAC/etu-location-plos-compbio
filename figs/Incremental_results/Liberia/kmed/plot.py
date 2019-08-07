import numpy as np
import matplotlib.pyplot as plt

N = 68



kmed_opt = [7183.073547,
7836.366825,
7501.765422,
6697.792153,
6377.634284,
5994.986654,
5437.18557,
5068.544339]

kmed_online = [10618.74528,
8749.384633,
7947.404666,
6991.65811,
6506.301227,
6062.999526,
5581.605056,
5238.396387]


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

plt.plot(X, kmed_opt, 'bs-', label='k-median solution (offline, lower-bound)')
plt.plot(X, kmed_online, 'rs-', label='k-median solution (online)')

#plt.xlim( 0, 15 )
plt.ylim( 0, 3.5 )

plt.legend()

plt.savefig('plot_kmed')



