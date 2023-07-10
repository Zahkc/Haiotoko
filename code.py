import time
import json
import alarm
import board
import displayio
import bitmaptools
import adafruit_imageload
import storage
import supervisor
import microcontroller

import menu
import entity
import animate
import selector
import buttonBus

#screen /dev/ttyACM0 115200

#setup
board.DISPLAY.root_group.hidden = False
board.DISPLAY.rotation = 90

try:
    storage.remount("/", False)
except RuntimeError as E:
    print("Failed Mount")

root = displayio.Group()

bgGroup = displayio.Group()
bgItemGroup = displayio.Group()
haioGroup = displayio.Group()
fgItemGroup = displayio.Group()
menuGroup = displayio.Group()
selectorGroup = displayio.Group()

board.DISPLAY.show(root)

entity = entity.entity()
entity.importSave()
entity.show(haioGroup)


bg, bgPallette = adafruit_imageload.load("/Sprites/Backgrounds/bg1.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
bgTile = displayio.TileGrid(bg, pixel_shader=bgPallette)
bgGroup.append(bgTile)

root.append(bgGroup)
root.append(bgItemGroup)
root.append(haioGroup)
root.append(fgItemGroup)
root.append(menuGroup)
root.append(selectorGroup)

select = selector.selector([[5,0],[40,0],[70,0],[90,0],[0,220],[110,220]])
select.showSelector(selectorGroup)
wakeTime = time.monotonic()


#Load Settings
with open("/Save/settings.json", "r") as reader:
    settings = json.loads(reader.read())
timeoutAmount = settings["timeout"]
timeout = round(time.monotonic() + timeoutAmount, 1)

nextWake = max(entity.character["nextEventTime"], entity.character["nextEvloutionTime"], entity.character["death"]) - entity.character["age"]

#Menu Activites
def do(x):
    global wakeTime
    if x == 0:
        entity.character["age"] +=  int(time.monotonic() - wakeTime)
        wakeTime = time.monotonic()
        print(entity.character["age"])
        pass
    elif x == 1:
        pass
    elif x == 2:
        pass
    elif x == 3:
        pass
    elif x == 4:
        menu.toggleMenu(root)
    elif x == 5:
        buttonBus.button1.deinit()
        pin_alarm = alarm.pin.PinAlarm(pin=board.D1, value=True, pull=True)
        time.sleep(0.5)
        alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

def checkTimeout():
    # print("Time: " + str(round(time.monotonic(), 1)) + " Timeout: " + str(timeout))
    if round(time.monotonic(), 1) == timeout:
        entity.character["age"] +=  int(time.monotonic() - wakeTime)
        # entity.update()
        buttonBus.button1.deinit()
        pin_alarm = alarm.pin.PinAlarm(pin=board.D1, value=True, pull=True)
        time.sleep(0.5)
        alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

#System Loop
while True:
    checkTimeout()
    animate.doAnimate(haioGroup, 0.5, 10)

    if buttonBus.getSelectedButton() == 0:
        select.lastPos()
        time.sleep(0.2)
        timeout = round(time.monotonic() + timeoutAmount, 1)
    elif buttonBus.getSelectedButton() == 1:
        do(select.getSPos())
        time.sleep(0.2)
        timeout = round(time.monotonic() + timeoutAmount, 1)
    elif buttonBus.getSelectedButton() == 2:
        select.nextPos()
        time.sleep(0.2)
        timeout = round(time.monotonic() + timeoutAmount, 1)
