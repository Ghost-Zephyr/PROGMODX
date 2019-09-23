# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:04:01 2019

@author: siver
"""

from microbit import *

while compass.is_calibrated() != True:
     compass.calibrate()
     if compass.is_calibrated() != True:
          display.scroll("Could not calirate compass.")

while True:
     needle = ((15 - compass.heading()) // 30) % 12
     display.show(Image.ALL_CLOCKS[needle])
     sleep(50)

