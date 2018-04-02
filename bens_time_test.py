#!/usr/bin/env python3

import matplotlib.pyplot as plt
import gale_shapley as gs
import time

ns     = []
times  = []
timesr = []
min_i  = 2
max_i  = 27
n_base = 1.3

for i in range( min_i, max_i ):
    n = int( n_base ** i )
    # generate an input to the algorithm under test
    ( ms, ws ) = gs.genInOrderPrefs( n )
    # run the algorithm
    t1 = time.time()
    gs.calcStableMatching( ms, ws )
    t2 = time.time()
    td = t2 - t1
    print( "%d %d %s" % ( i, n, td ) )
    ns.append( n )
    times.append( td )
    # hoping that when we graph timesr against n, we'll see a line
    timesr.append( 1 * ( td ** 0.3333333 ) )

plt.plot( ns, times )
plt.plot( ns, timesr )

plt.xlabel('input size')
plt.ylabel('time (s)')
plt.title('Algorithm Timing is Fun')
plt.grid(True)
# plt.savefig("test.png")
plt.show()
