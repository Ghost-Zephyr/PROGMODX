# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 00:49:15 2019

@author: siver
"""

import matplotlib.pyplot as plt
import numpy as np

ABC = ((0, 0), (4, 0), (3, 4))

vec1 = np.array(ABC[1]) - np.array(ABC[0])
vec2 = np.array(ABC[2]) - np.array(ABC[0])

vec1m = np.sqrt(vec1[0]**2 + vec1[1]**2)
vec2m = np.sqrt(vec2[0]**2 + vec2[1]**2)

v = np.degrees(np.arccos(
     (vec1[0]*vec2[0] + vec1[1]*vec2[1]) /
     (vec1m * vec2m)))

a = 1 / 2 * vec1m * vec2m * np.sin(v)

print("Arealet til trekanten er {}".format(a))

