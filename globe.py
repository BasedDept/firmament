#!/usr/bin/env python3

import scipy as sci
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from opensimplex import OpenSimplex
import geojson
import cartopy
import io
import time

radi = 1
ratio = 0.00311 /2
res = 4 *(pi/180)
seed = int(time.time())
octn = 8
sea = .1
landc = 0.05
watc = 0.1


rng = random.default_rng(seed)
noise = []
for i in range(0, octn - 1):
    noise.append(OpenSimplex(seed=rng.integers(low=0, high=100000)))

theta = []
phi = []
r = []
x = []
y = []
z = []
h = []

i = 0
hi = 0
lo = 0
for thetai in arange(0, pi, res):
    for phii in arange(-pi, pi, res):
        xx = radi*sin(thetai)*cos(phii)
        yy = radi*sin(thetai)*sin(phii)
        zz = radi*cos(thetai)
        theta.append(thetai)
        phi.append(phii)
        r.append(radi)
        h1 = 0
        for j in range(0, octn - 1):
            h1 = h1 + (1/(j+1) * (noise[j].noise3d(x=j*xx, y=j*yy, z=j*zz)))
        if h1 > hi:
            hi = h1
        if h1 < lo:
            lo = h1
        h.append(h1)
        x.append(xx + xx * 0.05 * h1)
        y.append(yy + yy * 0.05 * h1)
        z.append(zz + zz * 0.05 * h1)
        i = i + 1


sea = sea + ((hi - lo)/2 + lo)
l = []
for hh in h:
    if hh >= sea:
        l.append(landc*hh**3)
    else:
        l.append(watc*hh**3-landc)

plt.figure(1)
m = plt.axes()
m.scatter(phi, z, c = l)
show_globe = False
if show_globe is True:
    plt.figure(2)
    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z, c = l)
    ax.set_xlim([-radi, radi])
    ax.set_ylim([-radi, radi])
    ax.set_zlim(-radi, radi)
plt.show()
