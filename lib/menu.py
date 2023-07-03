import board
import adafruit_max1704x
import time
import terminalio
import displayio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import bitmap_label,  wrap_text_to_lines

menuToggle = True
battery = adafruit_max1704x.MAX17048(board.I2C())

def toggleMenu(splash):
    global menuToggle
    global battery
    if menuToggle:
        battery.reset()
        time.sleep(0.05)
        timeText = bitmap_label.Label(terminalio.FONT, text="Time: " + str(time.time() - 946684800), scale=1, color=0x000000, x=25, y=60)
        batText = bitmap_label.Label(terminalio.FONT, text="Battery: " + str(round(battery.cell_percent)) + "%", scale=1, color=0x000000, x=25, y=80)
        menuGroup = displayio.Group()
        menuGroup.append(Rect(10, 10, 115, 220, fill=0xFFFFFF, outline=0x000000, stroke=2))
        menuGroup.append(bitmap_label.Label(terminalio.FONT, text="Menu", scale=2, color=0x000000, x=30, y=30))
        menuGroup.append(timeText)
        menuGroup.append(batText)
        splash.append(menuGroup)
    else:
        splash.pop()
    menuToggle ^= True
