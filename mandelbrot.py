# Mandelbrot Generator
#
# Based on user input, this script generates a plot of the Mandelbrot set, and
# is optimized to take high resolutions (e.g. 3000 x 3000). The script makes
# use of np.meshgrid, np.where, and np array operations for optimization.

# Import Statements

import numpy as np
import matplotlib.pyplot as plt

# This function generates the Mandelbrot set which is then plotted.
# It makes use of numpy array operations and np.where in order to save time
# when computing high resolutions rather than nested for loops.

def mandelbrot_set_highres(c, n):
    points = np.zeros([r.size, i.size])
    z = c
    for x in range(n):
        z = z**2 + c
        a = np.absolute(z)
        ind = np.where(a > 2)
        points[ind] = x
    return points

# iterations is the max number before we consider the number to diverge

iterations = int(input("Enter max number of iterations: "))
gridsize = int(input("Enter square resolution: "))

# Since the doman and range has length 3, we divide 3 by the resolution for the
# number of points.

length = 3/gridsize
r = np.arange(-2, 1, length)
i = np.arange(-1.5, 1.5, length)

rr, ii = np.meshgrid(r, i)
z = rr + ii*1j

z = mandelbrot_set_highres(z, iterations)

plt.imshow(z, cmap="hot")
plt.savefig("mandelbrot.pdf")
plt.show()

