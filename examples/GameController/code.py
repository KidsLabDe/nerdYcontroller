import time
import board
import digitalio


import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)


# workaround: diffirent local keyboard layout...
# import conversion_dvorak


def typeIt(string):
        #string = conversion_dvorak.convert_ascii_dvorak(string)
        #string += "\n"
        layout.write(string)


debug = False

bnt1_pin = board.GP15
bnt2_pin = board.GP14
bnt3_pin = board.GP13
bnt4_pin = board.GP12

btn1 = digitalio.DigitalInOut(bnt1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2= digitalio.DigitalInOut(bnt2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(bnt3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(bnt4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN


while True:
    if btn1.value:
        if debug:
                print("buttn ! 1")
        keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
        time.sleep(0.5)
        typeIt("gamemode 1\n")
        
    elif btn2.value:
        if debug:
                print("buttn! 2!")
        keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
        time.sleep(0.5)
        typeIt("gamemode 2\n")
    elif btn3.value:
        if debug:
                print("buttn! 3!")
        keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
        time.sleep(0.5)
        typeIt("gamemode 3\n")
    elif btn4.value:
        if debug:
                print("buttn! 4!")
        keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
        time.sleep(0.5)
        typeIt("gamemode 4\n")
    else:
        if debug:
                print(".")
    time.sleep(0.1)
