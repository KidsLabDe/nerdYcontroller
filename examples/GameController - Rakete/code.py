import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

debug = False
sleep_time = 0.01
timer_sec = time.monotonic()

# Liste der Tasten und ihre zugehörigen Pins und Keycodes
buttons = [
    {"pin": board.GP15, "keycode": Keycode.V, "state": False},
    {"pin": board.GP17, "keycode": Keycode.B, "state": False},
    {"pin": board.GP14, "keycode": Keycode.N, "state": False},
    {"pin": board.GP16, "keycode": Keycode.M, "state": False},
    {"pin": board.GP18, "keycode": Keycode.C, "state": False},
]

# Initialisierung der Tasten
for button in buttons:
    button["pin"] = digitalio.DigitalInOut(button["pin"])
    button["pin"].direction = digitalio.Direction.INPUT
    button["pin"].pull = digitalio.Pull.UP

# Timeout Funktion - wenn das Spiel 90 Sekunden nicht benutzt wurde, wird mit Enter das Spiel wieder aktiviert
def timeout():
    global timer_sec
    if (time.monotonic() - timer_sec) > 90:
        keyboard.release_all()
        keyboard.press(Keycode.ENTER)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(1)
        keyboard.press(Keycode.ENTER)
        time.sleep(0.05)
        keyboard.release_all()
        time.sleep(1)
    timer_sec = time.monotonic()

while True:
    for button in buttons:
        if not(button["pin"].value) and not(button["state"]):
            timeout()
            button["state"] = True
            keyboard.press(button["keycode"])
            if debug:
                print(f'{button["keycode"]} an')
            time.sleep(sleep_time)
        if (button["pin"].value) and (button["state"]):
            timeout()
            button["state"] = False
            keyboard.release(button["keycode"])
            if debug:
                print(f'{button["keycode"]} aus')
            time.sleep(sleep_time)