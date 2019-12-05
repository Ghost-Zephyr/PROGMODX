# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:53:57 2019

@author: Sivert
"""

from microbit import *
import radio

display.show(Image.DIAMOND_SMALL)
radio.config(channel=11)
radio.on()

while True:
     ay = accelerometer.get_y()
     if ay > 400:
          if button_a.is_pressed() and button_b.is_pressed():
               radio.send("BAB")
               display.show(Image.ARROW_S)
          elif button_a.is_pressed():
               radio.send("BA")
               display.show(Image.ARROW_W)
          elif button_b.is_pressed():
               radio.send("BB")
               display.show(Image.ARROW_E)
          else:
               radio.send("0")
               display.show(Image.DIAMOND)
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
     if accelerometer.is_gesture("face down"):
          if button_a.is_pressed() and button_b.is_pressed():
               radio.send("RB")
               display.show(Image.TARGET)
     if accelerometer.was_gesture("shake"):
          radio.send("PR")
          display.show(Image.UMBRELLA)

