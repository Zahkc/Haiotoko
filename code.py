import os
import sys
import time
import json
import alarm
import board
import storage
import displayio
import supervisor
import bitmaptools
import microcontroller
import adafruit_imageload

import menu
import entity
import animate
import selector
import buttonBus


def importer(path):
    sys.path.append(path)
    for entry in os.listdir(path):
        if entry[-3:] == ".py":
            string = f'import {entry}'[:-3]
            exec (string)
        elif "." not in entry:
            importer(path+'/'+entry)

importer("/Activities")
sam = "xyz"
test.printit()

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

root.insert(0, bgGroup)
root.insert(1, bgItemGroup)
root.insert(2, haioGroup)
root.insert(3, fgItemGroup)
root.insert(4, menuGroup)
root.insert(5, selectorGroup)

wakeTime = time.monotonic()


entity = entity.entity()
entity.importSave()

#Load Settings
with open("/Save/settings.json", "r") as reader:
    settings = json.loads(reader.read())

timeoutAmount = settings["timeout"]
timeout = round(time.monotonic() + timeoutAmount, 1)
nextWake = max(entity.character["nextEventTime"], entity.character["nextEvloutionTime"], entity.character["death"]) - entity.character["age"]


def checkTimeout():
    # print("Time: " + str(round(time.monotonic(), 1)) + " Timeout: " + str(timeout))
    if round(time.monotonic(), 1) == timeout:
        entity.character["age"] +=  int(time.monotonic() - wakeTime)
        # entity.update()
        buttonBus.button1.deinit()
        pin_alarm = alarm.pin.PinAlarm(pin=board.D1, value=True, pull=True)
        time.sleep(0.5)
        alarm.exit_and_deep_sleep_until_alarms(pin_alarm)


home = home.home(root, entity)

#System Loop
while True:
    checkTimeout()
    if home.looper():
        timeout = round(time.monotonic() + timeoutAmount, 1)
