# -*- coding: utf-8 -*-
from random import randint
from microbit import *
import neopixel
import radio

display.show(Image.DIAMOND_SMALL)
np = neopixel.NeoPixel(pin13, 12)

leftSpeed = pin0
leftDirection = pin8
rightSpeed = pin1
rightDirection = pin12

def randomNeo():
    for pixel_id in range(0, len(np)):
        r = randint(0, 127)
        g = randint(0, 127)
        b = randint(0, 127)
        np[pixel_id] = (r,g,b)
    np.show()

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

def move(_leftSpeed, _rightSpeed, _leftDirection, _rightDirection):
    leftSpeed.write_analog(_leftSpeed)
    rightSpeed.write_analog(_rightSpeed)
    if (_leftDirection != 2):
        leftDirection.write_digital(_leftDirection)
        rightDirection.write_digital(_rightDirection)

def drive(speed):
    if (speed > 0):
        move(speed, speed, 0, 0)
    else:
        speed = 1023 + speed
        move(speed, speed, 1, 1)

def stop():
    move(0, 0, 0, 0)

randomNeo()
radio.config(channel=11)
radio.on()
display.show(Image.DIAMOND)

while True:
     msg = radio.receive()
     if msg == "AB":
          display.show(Image.ARROW_N)
          drive(1023)
     if msg == "A":
          display.show(Image.ARROW_W)
          move(127, 1023, 0, 0) #(255, 1023, 0, 0)
     if msg == "B":
          display.show(Image.ARROW_E)
          move(1023, 127, 0, 0) #(1023, 255, 0, 0)
     if msg == "BAB":
          display.show(Image.ARROW_S)
          drive(-1023)
     if msg == "BA":
          display.show(Image.ARROW_W)
          move(1023, 127, 1, 1)
     if msg == "BB":
          display.show(Image.ARROW_E)
          move(127, 1023, 1, 1)
     if msg == "0":
          stop()
          display.show(Image.TARGET)
     if msg == "PR":
          display.show(Image.UMBRELLA)
          randomNeo()
     if msg == "RB":
          display.show(Image.DIAMOND)
          i = pixelRainbow(i)
          sleep(20)

