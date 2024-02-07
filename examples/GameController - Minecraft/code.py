import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

# Geht was nicht? Debug an und in der Console nachsehen
debug = False

# Hier sind die einzelnen PINS (Tasten)  definiert und die dazu gehörigen Befehle
buttons = {
    board.GP15: "gamemode 1\n",
    board.GP14: "gamemode 2\n",
    board.GP13: "gamemode 3\n",
    board.GP12: "gamemode 4\n",
}

# Initialisiere die Tasten
for pin in buttons.keys():
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    buttons[pin] = (btn, buttons[pin])

def typeIt(string):
    layout.write(string)

while True:
    for btn, action in buttons.values():
        if btn.value:
            if debug:
                print(f"Button {btn.pin} pressed!")
            # zurest Shift+7 (für /) und dann den Befehl
            keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
            # kurz warten, damit der Befehl auch ankommt
            time.sleep(0.5)
            # Befehl senden
            typeIt(action)
    if debug:
        print(".")
    time.sleep(0.1)