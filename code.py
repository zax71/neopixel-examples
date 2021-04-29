"""
NeoPixel & 7 segment display example
code by Zax71
discord: Zax71 | feel free to at me#1557
"""

"""imports"""

#main imports
import time, board, digitalio, neopixel, random

#LED animation imports
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.color import WHITE
from adafruit_led_animation.animation.rainbow import Rainbow

"""neopixel Setup"""

#import neopixels
num_pixels = 4

pixels = neopixel.NeoPixel(board.GP8, num_pixels, auto_write=False)
pixels.brightness = 1

#LED_animation module animations
chase = Chase(pixels, speed=0.1, color=WHITE, size=3, spacing=6)#chase

rainbow = Rainbow(pixels, speed=0.1, period=2)#rainbow


"""buttons"""

# up button
up = digitalio.DigitalInOut(board.GP9)
up.switch_to_input(pull=digitalio.Pull.DOWN)
# down button
down = digitalio.DigitalInOut(board.GP10)
down.switch_to_input(pull=digitalio.Pull.DOWN)

"""7 segment display pins"""

# A-GP0
seg7A = digitalio.DigitalInOut(board.GP0)
seg7A.direction = digitalio.Direction.OUTPUT

# B-GP1
seg7B = digitalio.DigitalInOut(board.GP1)
seg7B.direction = digitalio.Direction.OUTPUT

# C-GP2
seg7C = digitalio.DigitalInOut(board.GP2)
seg7C.direction = digitalio.Direction.OUTPUT

# D-GP3
seg7D = digitalio.DigitalInOut(board.GP3)
seg7D.direction = digitalio.Direction.OUTPUT

# E-GP4
seg7E = digitalio.DigitalInOut(board.GP4)
seg7E.direction = digitalio.Direction.OUTPUT

# F-GP5
seg7F = digitalio.DigitalInOut(board.GP5)
seg7F.direction = digitalio.Direction.OUTPUT

# G-GP6
seg7G = digitalio.DigitalInOut(board.GP6)
seg7G.direction = digitalio.Direction.OUTPUT

"""functions"""


#clear 7seg display
def seg7Clear():
    seg7A.value = False
    seg7B.value = False
    seg7C.value = False
    seg7D.value = False
    seg7E.value = False
    seg7F.value = False
    seg7G.value = False

#main 7seg function
def seg7(number):

    seg7Clear()#clear the display

    if number == 0:
        seg7A.value = True
        seg7B.value = True
        seg7C.value = True
        seg7D.value = True
        seg7E.value = True
        seg7F.value = True
    if number == 1:
        seg7B.value = True
        seg7C.value = True
    if number == 2:
        seg7A.value = True
        seg7B.value = True
        seg7G.value = True
        seg7E.value = True
        seg7D.value = True
    if number == 3:
        seg7A.value = True
        seg7B.value = True
        seg7G.value = True
        seg7C.value = True
        seg7D.value = True
    if number == 4:
        seg7F.value = True
        seg7B.value = True
        seg7G.value = True
        seg7C.value = True
    if number == 5:
        seg7A.value = True
        seg7F.value = True
        seg7G.value = True
        seg7C.value = True
        seg7D.value = True
    if number == 6:
        seg7A.value = True
        seg7F.value = True
        seg7G.value = True
        seg7C.value = True
        seg7D.value = True
        seg7E.value = True
    if number == 7:
        seg7A.value = True
        seg7B.value = True
        seg7C.value = True
    if number == 8:
        seg7A.value = True
        seg7B.value = True
        seg7C.value = True
        seg7D.value = True
        seg7E.value = True
        seg7F.value = True
        seg7G.value = True
    if number == 9:
        seg7A.value = True
        seg7B.value = True
        seg7C.value = True
        seg7D.value = True
        seg7F.value = True
        seg7G.value = True


def mode(mode):

    if mode == 0:
        seg7(0)
        pixels.fill((255, 0, 0))
        pixels.show()
    if mode == 1:
        seg7(1)
        pixels.fill((0, 255, 0))
        pixels.show()
    if mode == 2:
        seg7(2)
        pixels.fill((0, 0, 255))
        pixels.show()
    if mode == 3:
        seg7(3)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pixels.fill((r, g, b))
        pixels.show()
        time.sleep(0.4)
    if mode == 4:
        seg7(4)
        chase.animate()
    if mode == 5:
        seg7(5)
        rainbow.animate()


"""mainloop"""

currentMode = 0
mode(currentMode)
while True:
    #set currentMode to button values
    if up.value:
        currentMode +=1
        time.sleep(0.5)
    elif down.value:
        currentMode -=1
        time.sleep(0.5)


    #conditions to limit currentMode to 0-9
    if currentMode < 0:
        currentMode = 5
    if currentMode > 5:
        currentMode = 0

    mode(currentMode)#set the mode using the function above

