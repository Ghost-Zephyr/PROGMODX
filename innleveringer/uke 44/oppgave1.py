from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    if button_b.was_pressed():
        display.show(Image.SAD)
