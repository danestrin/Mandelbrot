# Mandelbrot Generator by Dan Estrin
#
# Based on user input, this script generates a plot of the Mandelbrot set, and
# is optimized to take high resolutions (e.g. 3000 x 3000). The script makes
# use of np.meshgrid, np.where, and np array operations for optimization.
# Recommended number of iterations is 100.

import numpy as np
import matplotlib.pyplot as plt
import time

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

# Example plots with different shapes
# Modifiying the iteration number will yield different designs

# Full Mandelbrot
#x_min = -2
#x_max = 1
#y_min = -1.5
#y_max = 1.5
#scale = 1

# Trees
#x_min = -54125
#x_max = -53125
#y_min = -62225
#y_max = -61225
#scale = 100000

# Mini-Mandelbrot - the shape repeats itself when zoomed in 100000x (needs 1000+ iterations)
#x_min = -52787
#x_max = -52777
#y_min = -62612
#y_max = -62602
#scale = 100000

x_min = -2
x_max = 1
y_min = -1.5
y_max = 1.5
scale = 1

r = np.linspace(x_min, x_max, gridsize) / scale
i = np.linspace(y_min, y_max, gridsize) / scale

rr, ii = np.meshgrid(r, i)
z = rr + ii*1j

init_time = time.time()
z = mandelbrot_set_highres(z, iterations)
end_time = time.time()

print("Evaluation time: " + str(end_time - init_time) + " seconds")

plt.axis("off")
# change cmap for different coloring
plt.imshow(z, cmap="magma")
plt.savefig("mandelbrot.png", bbox_inches = "tight", pad_inches = 0, dpi=200)
plt.show()
