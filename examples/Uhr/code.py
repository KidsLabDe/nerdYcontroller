import os
print("hallo!")
print("hallo!")
print("hallo!")
print(os.getenv("test_variable"))



import ipaddress
import wifi
import socketpool


print("Connecting to WiFi")

#  connect to your SSID
wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))

print("Connected to WiFi")

pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))




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



dot_status = True


def bmp_to_screen(img, screen, x0, y0):
    for y in range(img.DIB_h):
        for x in range(img.DIB_w):
            screen.pixel(x + x0, y + y0, img[x, y])

def show_bmp(screen,filename,x0 = 0, y0 = 0):
    bmp = MicroBMP().load(filename)
    bmp_to_screen(bmp,screen, x0, y0)
    screen.display()

def dots(screen):
    global dot_status
    if dot_status:
        screen.pixel(20,2,0x00FF00)
        screen.pixel(20,4,0x00FF00)
    else:
        screen.pixel(20,2,0x00FFFF)
        screen.pixel(20,4,0x00FFFF)
    dot_status = not(dot_status)
    screen.display()

def show_time(screen):
    zeit = rtc.RTC().datetime
    stunde = zeit[3] + os.getenv("TIME_OFFSSET")
    minute = str(zeit[4])
    if len(minute) == 1:
        minute = "0" + minute


    show_bmp(screen,"img/"+str(stunde)[0:1]+".bmp",11,1)
    show_bmp(screen,"img/"+str(stunde)[1:2]+".bmp",16,1)
    show_bmp(screen,"img/"+minute[0:1]+".bmp",22,1)
    show_bmp(screen,"img/"+minute[1:2]+".bmp",27,1)


pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=0)
rtc.RTC().datetime = ntp.datetime




while True:

    show_time(pixel_framebuf)

    show_bmp(pixel_framebuf,"birne1.bmp")
    time.sleep(0.5)
    show_bmp(pixel_framebuf,"birne2.bmp")
    time.sleep(0.5)
    dots(pixel_framebuf)
    show_bmp(pixel_framebuf,"birne3.bmp")
    time.sleep(0.5)
    show_bmp(pixel_framebuf,"birne4.bmp")
    time.sleep(0.5)
    dots(pixel_framebuf)

    # state":{"open":true




