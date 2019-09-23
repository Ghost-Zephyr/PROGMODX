# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:29:19 2019

@author: siver
"""

from microbit import *

while True:
     display.show(Image.HEART)
     sleep(250)
     display.show(Image("00000:"
                        "00000:"
                        "00000:"
                        "00000:"
                        "00000:"))
     sleep(200)

