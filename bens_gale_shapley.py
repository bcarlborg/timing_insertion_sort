#!/usr/bin/env python3

from random import shuffle
import time

# prefsM and prefsW are lists of lists that contain the preference
# orderings for men and women, respoectively
def calcStableMatching( prefsM, prefsW ):
    n = len( prefsM )
    assert n == len( prefsW )
    # list of free men
    freeM = list( range( n ) )
    # A list of indices into the men's preference lists
    nextChoice = [ 0 ] * n
    # partners stores the matches. "-1" means no match
    partners = [ -1 ] * n

    # Does w prefer m1 to m2?
    def prefer( w, m1, m2 ):
        for i in range( n ):
            mi = prefsW[ w ][ i ]
            if mi == m1:
                return True
            elif mi == m2:
                return False
        assert False

    while len( freeM ) > 0:
        mIdx = freeM.pop()
        wIdx = prefsM[ mIdx ][ nextChoice[ mIdx ] ]
        if partners[ wIdx ] < 0:
            partners[ wIdx ] = mIdx
        else:
            mOther = partners[ wIdx ]
            if prefer( wIdx, mIdx, mOther ):
                partners[ wIdx ] = mIdx
                loser = mOther
            else:
                loser = mIdx
            freeM.append( loser )
            nextChoice[ loser ] += 1
        # print( nextChoice )

    # print( partners )
    return partners

# Input generator for Gale-Shapley
def genInOrderPrefs( N ):
    base = list( range( N ) )
    ms = []
    ws = []
    t1 = time.time()
    for i in range( N ):
        m = base[:]
        w = base[:]
        # shuffle( m )
        # shuffle( w )
        ms.append( m )
        ws.append( w )
    t2 = time.time()
    # debugging: print( t2 - t1 )
    return ( ms, ws )

# sanity testing:
# m = calcStableMatching( [ [ 0, 1 ], [ 0, 1 ] ], [ [ 1, 0 ], [ 0, 1 ] ] )
