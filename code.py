import time
import alarm
import board
import displayio
import digitalio
import bitmaptools
import adafruit_imageload

import menu
import selector
import buttonBus

#screen /dev/ttyACM0 115200

#setup
board.DISPLAY.root_group.hidden = False
board.DISPLAY.rotation = 90
splash = displayio.Group()
board.DISPLAY.show(splash)

bg, bgPallette = adafruit_imageload.load("/Sprites/Backgrounds/bg1.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
bgTile = displayio.TileGrid(bg, pixel_shader=bgPallette)

tama, tamaPallette = adafruit_imageload.load("/Sprites/Characters/MUSH/ADULT/BODY.BMP", bitmap=displayio.Bitmap, palette=displayio.Palette)
tamaPallette.make_transparent(3)
tamaTile = displayio.TileGrid(tama, pixel_shader=tamaPallette, x=20, y=100)


splash.append(bgTile)
splash.append(tamaTile)

bounce = False
bounceAmount = -10
selector.showSelector(splash)

#Menu Activites
def do(x):
    if x == 0:
        pass
    elif x == 1:
        pass
    elif x == 2:
        pass
    elif x == 3:
        pass
    elif x == 4:
        menu.toggleMenu(splash)
    elif x == 5:
        buttonBus.button1.deinit()
        pin_alarm = alarm.pin.PinAlarm(pin=board.D1, value=True, pull=True)
        time.sleep(0.5)
        alarm.exit_and_deep_sleep_until_alarms(pin_alarm)


#System Loop
while True:

    if(round(time.monotonic()%0.5, 1) == 0.5):
        if bounce == False:
            bounce = True
            bounceAmount = bounceAmount * -1
            tamaTile.y += bounceAmount
    else:
        if bounce == True:
            bounce = False


    if buttonBus.getSelectedButton() == 0:
        selector.lastPos()
        time.sleep(0.2)
    elif buttonBus.getSelectedButton() == 1:
        do(selector.spos)
        time.sleep(0.2)
    elif buttonBus.getSelectedButton() == 2:
        selector.nextPos()
        time.sleep(0.2)
