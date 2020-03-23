# -*- coding: utf-8 -*-
from random import randint
from microbit import *
import neopixel
import radio

# Init
display.show(Image.DIAMOND_SMALL)
np = neopixel.NeoPixel(pin13, 12)

leftSpeed = pin8 #pin16
leftDirection = pin16 #pin8
rightSpeed = pin12 #pin14
rightDirection = pin14 #pin12

# IR sensorene på bunn av BitBoten
leftLineSensor = pin2
rightLineSensor = pin1

# Begge lys sensorene er på samme pin så vi setter også select pin
#lightSensor = pin2
#sensorSelect = pin16

# Neopixel funcs, magi for lysene på bit:boten
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

def venstreLys(Red, Green, Blue):
    for pixel_id in range(0, 6):
        np[pixel_id] = (Red, Green, Blue)
    np.show()


def hoyreLys(Red, Green, Blue):
    for pixel_id in range(6, 12):
        np[pixel_id] = (Red, Green, Blue)
    np.show()

def setLysstyrke(minValue):
    return 1
    '''
    sensorSelect.write_digital(0)
    brightnessLeft = lightSensor.read_analog()
    sensorSelect.write_digital(1)
    brightnessRight = lightSensor.read_analog()

    brightness = int((brightnessLeft + brightnessRight) / 2)
    brightness = int(brightness / 25)
    if(brightness < minValue):
        brightness = minValue
    return brightness'''

# Motor kontroll for å sette motor retning og fart
def move(_leftSpeed, _rightSpeed, _leftDirection, _rightDirection):
    # speed verdier mellom 0 - 1023
    # lavere verder == raskere fart bakover
    # lavere verdier == lavere fart fremover
    # retning 0 == fremover, 1 == bakover
    leftSpeed.write_analog(_leftSpeed)  # Setter farten til venstre motor
    rightSpeed.write_analog(_rightSpeed)  # Setter farten til høyre motor
    if (_leftDirection != 2):
        leftDirection.write_digital(_leftDirection)  # venstre motor retning
        rightDirection.write_digital(_rightDirection)  # høyre motor retning

def drive(speed):
    if (speed > 0):
        move(speed, speed, 0, 0)  # kjør motorene fremover
    else:
        speed = 1023 + speed  # negativ fart
        move(speed, speed, 1, 1)  # kjør motorene bakover

def stop():
    move(0, 0, 0, 0)

# Se funksjonsnavn
def lineDetector(side):  # 0 == venstre, 1 == høyre
    if(side == 0):
        isLine = leftLineSensor.read_digital()
    else:
        isLine = rightLineSensor.read_digital()

    if(isLine == 1): # Sensoren ser linjen
        return True
    else:
        return False

# Mer init stuff
randomNeo()
display.show(Image.DIAMOND)

while True:
    isLeftLine = lineDetector(0)
    isRightLine = lineDetector(1)
    if(isRightLine is True) and (isLeftLine is False):  # en linje sett
        hoyreLys(setLysstyrke(1), 0, 0)
        stop()
        sleep(50)
        move(127, 1023, 0, 1) #skarpHoyre()
        sleep(200)
        stop()
        sleep(50)
        while(lineDetector(1) is True):
            hoyreLys(setLysstyrke(1), 0, 0)
            move(255, 0, 0, 0) #mykHoyre()
    elif(isLeftLine is True) and (isRightLine is False):  # en linje sett
        venstreLys(setLysstyrke(1), 0, 0)
        stop()
        sleep(50)
        move(1023, 127, 1, 0) #skarpVenstre()
        sleep(200)
        stop()
        sleep(50)
        while(lineDetector(0) is True):
            venstreLys(setLysstyrke(1), 0, 0)
            move(0, 255, 0, 0) #mykLeft()
    elif(isRightLine is False) and (isLeftLine is False):  # ingen linje
        venstreLys(0, setLysstyrke(1), 0)
        hoyreLys(0, setLysstyrke(1), 0)
        drive(1023)
    else:
        venstreLys(0, setLysstyrke(1), setLysstyrke(1))  # 2 linjer sett
        hoyreLys(0, setLysstyrke(1), setLysstyrke(1))
        stop()
        sleep(200)
