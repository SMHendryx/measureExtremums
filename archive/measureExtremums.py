#code from http://stackoverflow.com/questions/31667070/max-distance-between-2-points-in-a-data-set-and-identifying-the-points

from itertools import combinations
from numpy import random

from scipy.spatial.distance import pdist
from scipy.spatial.distance import euclidean as dist
import numpy as np
from numpy import random, nanmax, argmax, unravel_index
from scipy.spatial.distance import pdist, squareform

# make test point cloud:
A = random.randint(-5,5, (5,3))
# compute the condensed distance between all combinations of points:
D  = pdist(A)
D = squareform(D);
#from sys import getsizeof
#getsizeof(D)
# to see size of object in bytes
# Get distance and indices of two furthest points:
maxDist, [I_row, I_col] = nanmax(D), unravel_index( argmax(D), D.shape )
# Get two furthest points:
return A[I_row], A[I_col]



def square_distance(x,y): return sum([(xi-yi)**2 for xi, yi in zip(x,y)])

max_square_distance = 0
for pair in combinations(A,2):
    if square_distance(*pair) > max_square_distance:
        max_square_distance = square_distance(*pair)
        max_pair = pair




#compute number of combinations:
import functools
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( functools.reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )