from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image("00000:"*4+"00000"))
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    else:
        display.show(Image("00000:"*4+"00000"))
