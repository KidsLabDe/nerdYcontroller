import time
import board
import neopixel


# Wo ist das Datenkabel der NeoPixel angeschlossen? Hinten auf dem Pico stehen die Namen drauf.
pixel_pin = board.GP12


# Wieviele "Pixel" oder Lämpchen hat der Streifen?
num_pixels = 4

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin,  # Wo ist angesteckt
    num_pixels,  # Die Anzahl der Pixel von oben
    brightness=0.2,  # Wie hell - 1 = 100%. Ist super hell... 20% (0.2) reichen meistens...
    auto_write=False,  # Wenn man was ändert, also die Farben setzt, muss man immer noch ein pixels.show() ausführen, damit die Änderungen auch ausgeführt werden. Das ist wichtig, wenn man viele pixel auf einmal ändert, sonst dauert es länger...
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:

    # 10 mal schnell (1ms pro Farbe)
    for i in range(10):
        rainbow_cycle(0.001)  # rainbow cycle with 10ms delay per step

    # einmal normal...
    rainbow_cycle(0.01)  # rainbow cycle with 10ms delay per step

    # und einmal super langsam!
    rainbow_cycle(0.1)  # rainbow cycle with 10ms delay per step

    # Mehr Beispiele gibt es hier: https://learn.adafruit.com/circuitpython-led-animations/overview
