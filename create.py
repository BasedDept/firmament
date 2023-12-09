#!/usr/bin/env python3
#from scipy import *
from configparser import Interpolation
from numpy import *
import matplotlib.pyplot as plt
from opensimplex import OpenSimplex
import geojson
import io

seed = 1338

def noise(s, x):
    return OpenSimplex(seed=random.default_rng(s + x).integers(low = 0, high = 2^64 - 1))

def compress(x):
    if x <= -1:
        return -1
    if x < 0:
        return -abs(x**2)
    if x == 0:
        return 0
    if x < 1:
        return x**2
    return 1

base = 1
num = 4
res = 2

def elev(az, alt):
    x = base * sin(pi / 180 * (90 - alt)) * cos(pi / 180 * az)
    y = base * sin(pi / 180 * (90 - alt)) * sin(pi / 180 * az)
    z = base * cos(pi / 180 * (90 - alt))
    h = 0
    m = 0
    for i in arange(0, num - 1, 1):
        m = m + 1/(2**i)
        h = h + 1/(2**i) * noise(seed, i).noise3d(x = 2**i * x, y = 2**i * y, z = 2**i * z)
    return compress(h / m)


el = []
for alt in arange(-90, 90, res):
    tmp = []
    for az in arange(-180, 180, res):
        tmp.append(elev(az, alt))
    el.append(tmp)        


plt.imshow(el, interpolation='none', extent=[-180, 180, -90, 90])
plt.show()
