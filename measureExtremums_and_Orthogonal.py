# IN DEVELOPMENT
# Function finds the two furthest points in a set of n-dimensional points and 
# returns the point coordinates and distance between them

# Written by Sean Hendryx adapted from http://stackoverflow.com/questions/31667070/max-distance-between-2-points-in-a-data-set-and-identifying-the-points

from numpy import random, nanmax, argmax, unravel_index
from scipy.spatial.distance import pdist, squareform

def measureExtremums(points, orthogonal = False):
    """
    Takes in a set of n-dimensional points.
    Returns the distance between the two furthest points and the coordinates themselves.
    If orthogonal == True, also returns the orthogonal distance between furthest coordinates
    """
    # compute the condensed distance between all combinations of points:
    D  = pdist(points)
    D = squareform(D);
    #from sys import getsizeof
    #getsizeof(D)
    # to see size of object in bytes
    # Get distance and indices of two furthest points:
    maxDist, [I_row, I_col] = nanmax(D), unravel_index( argmax(D), D.shape )
    if orthogonal == False:
        # Get two furthest points and return them:
        return maxDist, points[I_row], points[I_col]
    else:
        orthDist = 
