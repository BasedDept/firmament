#!/usr/bin/env python3

from mpl_toolkits.basemap import Basemap
import scipy as sci
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from opensimplex import OpenSimplex
import geojson
import cartopy
import io
import time

octn = 8
rng = random.default_rng(int(time.time()))
noise = []
for i in range(0, octn - 1):
    noise.append(OpenSimplex(seed=rng.integers(low=0, high=100000)))

nrows, ncols = (90, 180)
lon, lat = meshgrid(linspace(0, 360, ncols), linspace(-90, 90, nrows))
themap = Basemap(projection='ortho', lat_0=45, lon_0=15)
themap.drawmeridians(arange(0, 360, 30))
themap.drawparallels(arange(-90, 90, 30))
Ti = zeros_like(lon)
x, y = themap(lon, lat)
for i in range(0, nrows):
    for j in range(0, ncols):
        xx, yy = themap(lon[j], lat[i])
        Ti[i, j] = noise[0].noise3d(x=xx, y=yy, z=0)
cs = themap.contourf(x, y, Ti, 15)
plt.show()

