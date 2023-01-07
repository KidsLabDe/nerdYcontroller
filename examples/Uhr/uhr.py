

import board
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer
import time
from microbmp import MicroBMP
import rtc

import socketpool
import wifi
import adafruit_ntp


pixel_pin = board.GP21
pixel_width = 32
pixel_height = 8

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=0.1,
    auto_write=False,
)

pixel_framebuf = PixelFramebuffer(
    pixels,
    pixel_width,
    pixel_height,
    orientation='VERTICAL',
    alternating=True,
    reverse_x=False,
)



text = "Willkommen im KidsLab! Nächster Kurs: Donnerstag... offener Donnerstag"





def bmp_to_screen(img, screen, x0, y0):
    for y in range(img.DIB_h):
        for x in range(img.DIB_w):
            screen.pixel(x + x0, y + y0, img[x, y])

def show_bmp(screen,filename,x0 = 0, y0 = 0):
    bmp = MicroBMP().load(filename)
    bmp_to_screen(bmp,screen, x0, y0)
    screen.display()


def show_time(screen):
    zeit = rtc.RTC().datetime

    show_bmp(screen,"img/"+str(zeit[3])[0:1]+".bmp",11,1)
    show_bmp(screen,"img/"+str(zeit[3])[1:2]+".bmp",16@,1)
    show_bmp(screen,"img/"+str(zeit[4])[0:1]+".bmp",22,1)
    show_bmp(screen,"img/"+str(zeit[4])[1:2]+".bmp",27,1)





wifi.radio.connect("", "")


pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=0)
rtc.RTC().datetime = ntp.datetime



while True:

    show_time(pixel_framebuf)

    show_bmp(pixel_framebuf,"birne1.bmp")
    time.sleep(1)
    show_bmp(pixel_framebuf,"birne2.bmp")
    time.sleep(1)
    show_bmp(pixel_framebuf,"birne3.bmp")
    time.sleep(1)
    show_bmp(pixel_framebuf,"birne4.bmp")
    time.sleep(1)


    # state":{"open":true



