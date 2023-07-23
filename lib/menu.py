import time
import board
import selector
import buttonBus
import displayio
import terminalio
import adafruit_max1704x
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import bitmap_label,  wrap_text_to_lines

battery = adafruit_max1704x.MAX17048(board.I2C())

def toggleMenu(menuGroup, selectorGroup, label1, method1):
    global battery


    # bselect = selector.selector([[10, 60],[10, 80]])
    # bselect.showSelector(selectorGroup)

    battery.reset()
    time.sleep(0.05)
    timeText = bitmap_label.Label(terminalio.FONT, text="Time: " + str(time.monotonic()), scale=1, color=0x000000, x=25, y=60)
    batText = bitmap_label.Label(terminalio.FONT, text="Battery: " + str(round(battery.cell_percent)) + "%", scale=1, color=0x000000, x=25, y=80)
    menuGroup.append(Rect(10, 10, 115, 220, fill=0xFFFFFF, outline=0x000000, stroke=2))
    menuGroup.append(bitmap_label.Label(terminalio.FONT, text="Menu", scale=2, color=0x000000, x=30, y=30))
    menuGroup.append(timeText)
    menuGroup.append(batText)
