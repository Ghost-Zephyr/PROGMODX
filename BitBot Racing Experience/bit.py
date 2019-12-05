# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:53:57 2019

@author: siver
"""

from microbit import *
import radio

display.show(Image.DIAMOND_SMALL)
radio.on()

while True:
     if accelerometer.was_gesture("face down"):
          if button_a.is_pressed() and button_b.is_pressed():
               radio.send("RB")
               display.show(Image.TARGET)
     else:
          if button_a.is_pressed() and button_b.is_pressed():
               radio.send("AB")
               display.show(Image.ARROW_N)
          elif button_a.is_pressed():
               radio.send("A")
               display.show(Image.ARROW_W)
          elif button_b.is_pressed():
               radio.send("B")
               display.show(Image.ARROW_E)
          else:
               radio.send("0")
               display.show(Image.DIAMOND)
     if accelerometer.was_gesture("shake"):
          radio.send("PR")
          display.show(Image.UMBRELLA)

