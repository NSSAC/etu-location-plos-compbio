import numpy as np
import matplotlib.pyplot as plt

N = 68



kmed_frac = [6714.431765,
6982.799855,
6889.644021,
8711.587716,
6799.239586,
5537.687551,
5087.364259,
4836.979022]

kmed_int = [6714.431765,
6982.799855,
6889.644021,
8753.097806,
6837.178324,
5548.56659,
5092.091134,
4837.189356]


X = [2,4,6,8,10,12,14,16]

def normalize(a):
    a[:] = [x / 3600.0 for x in a]

normalize(kmed_frac)
normalize(kmed_int)


#plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('weeks')
ax.set_ylabel('average cost (hours)')

plt.plot(X, kmed_frac, 'bs-', label='k-median fractional solution (lower-bound)')
plt.plot(X, kmed_int, 'rs-', label='k-median integral solution ')

#plt.xlim( 0, 15 )
plt.ylim( 0, 4.5 )

plt.legend()

plt.savefig('plot_kmed_cap_rounding_gap')



