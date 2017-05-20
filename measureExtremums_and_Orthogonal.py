# IN DEVELOPMENT
# Function finds the two furthest points in a set of n-dimensional points and 
# returns the point coordinates and distance between them

# Written by Sean Hendryx adapted from http://stackoverflow.com/questions/31667070/max-distance-between-2-points-in-a-data-set-and-identifying-the-points

from numpy import random, nanmax, argmax, unravel_index, absolute
from scipy.spatial.distance import pdist, squareform
import random
import math
import numpy as np

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
        #in dev:
        p1, p2 = points[I_row], points[I_col]
        x1 = p1[0]
        x2 = p2[0]
        y1 = p1[1]
        y2 = p2[1]
        # Make line end-points into vector:
        #http://stackoverflow.com/questions/3838319/how-can-i-check-if-a-point-is-below-a-line-or-not
        v1 = {'x':x2-x1,'y': y2-y1}
        #
        oneHalf = []
        secondHalf = []
        # split the points in half (one set on each side of the major axis):
        #compute cross product to test if a given point is on the same side of the line as the reference point or not:
        referencePoint = points[0]
        #http://stackoverflow.com/questions/13724405/determining-which-side-of-a-line-is-on-given-3rd-point-indicating-desired-side
        for point in points:
            #test = np.dot(np.cross((p1 * p2), (p1 * referencePoint)), np.cross((p1 * p2), (p1 * point)))
            xA = point[0]
            yA = point[1]
            v2 = {'x':x2-xA, 'y':y2-yA}
            test = v1['x']*v2['y'] - v1['y']*v2['x']
            print "test: ", test
            if test > 0.:
                oneHalf.append(point)
            else:
                secondHalf.append(point)
        #
        #compute furthest point in each half from line:
        furthestDist_1 = 0.0
        for point in oneHalf:
            x0 = point[0]
            y0 = point[1]
            dist_i = absolute((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / ((y2 - y1)**2. + (x2 - x1)**2.)**.5
            if dist_i > furthestDist_1:
                furthestDist_1 = dist_i
                furthestOrthoPoint_1 = point
        #
        furthestDist_2 = 0.0
        for point in secondHalf:
            x0 = point[0]
            y0 = point[1]
            dist_i = absolute((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / ((y2 - y1)**2. + (x2 - x1)**2.)**.5
            if dist_i > furthestDist_2:
                furthestDist_2 = dist_i
                furthestOrthoPoint_2 = point
        #
        orthoDist = furthestDist_1 + furthestDist_2
        return maxDist, points[I_row], points[I_col], orthoDist, furthestOrthoPoint_1, furthestOrthoPoint_2



def generateSamplePoints(numPoints, shape = "circle-ish"):
    if shape == "circle-ish":
        # radius of the circle
        circle_r = 10
        # center of the circle (x, y)
        circle_x = 5
        circle_y = 7
        #
        points = []
        for i in range(numPoints):
            # random angle
            alpha = 2 * math.pi * random.random()
            # random radius
            r = circle_r * random.random()
            # calculating coordinates
            x = r * math.cos(alpha) + circle_x
            y = r * math.sin(alpha) + circle_y
            #
            print "Random point ", (x, y)
            point = [x,y]
            points.append(point)
            #
        #
        print "All points:\n", points
        return points


#test:
import matplotlib.pyplot as plt
import numpy as np
points = np.asarray((generateSamplePoints(100)))
distance, p1, p2, orthoDist, furthestOrthoPoint_1, furthestOrthoPoint_2 = measureExtremums(points, orthogonal = True)

plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='red')
plt.scatter(points[:,0], points[:,1])
plt.scatter([furthestOrthoPoint_1[0], furthestOrthoPoint_2[0]], [furthestOrthoPoint_1[1], furthestOrthoPoint_2[1]], s = 40, color='green')
plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], s = 40, color='orange')
#plt.scatter(X,Y1,color='red')
plt.show()

