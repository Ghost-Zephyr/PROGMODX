# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:49:52 2019

@author: siver
"""

from microbit import *
from random import randint
import neopixel
import radio

display.show(Image.DIAMOND_SMALL)
np = neopixel.NeoPixel(pin13, 12)

def pixelRainbow(i):
     for pixel_id in range(0, len(np)):
          r = i
          g = i + 24
          b = i + 48
          np[pixel_id] = (r, g, b)
     np.show()
     if i + 96 > 255:
          i -= 159
     return i + 48

def pixelReset():
     for pixel_id in range(0, len(np)):
          r = randint(0, 127)
          g = randint(0, 127)
          b = randint(0, 127)
          np[pixel_id] = (r, g, b)
     np.show()

pixelReset()
radio.on()
i = 0

while True:
     msg = radio.receive()
     if msg == "AB":
          display.show(Image.ARROW_N)
          pin0.write_digital(1)
          pin1.write_digital(1)
     if msg == "A":
          display.show(Image.ARROW_W)
          pin0.write_digital(0)
          pin1.write_digital(1)
     if msg == "B":
          display.show(Image.ARROW_E)
          pin0.write_digital(1)
          pin1.write_digital(0)
     if msg == "0":
          display.show(Image.DIAMOND)
          pin0.write_digital(0)
          pin1.write_digital(0)
     if msg == "PR":
          display.show(Image.UMBRELLA)
          pixelReset()
     if msg == "RB":
          display.show(Image.TARGET)
          i = pixelRainbow(i)
          sleep(20)

