import time
import menu
import alarm
import board
import entity
import animate
import selector
import displayio
import buttonBus
import adafruit_imageload

class home:

    root = displayio.Group()
    entity = entity.entity()
    select = selector.selector([[5,0],[40,0],[70,0],[90,0],[0,220],[110,220]])


    def __init__(self, root, entity):
        self.root = root
        self.entity = entity

        self.entity.show(root[2])

        bg, bgPallette = adafruit_imageload.load("/Sprites/Backgrounds/bg1.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
        bgTile = displayio.TileGrid(bg, pixel_shader=bgPallette)
        self.root[0].append(bgTile)
        self.select.showSelector(self.root[5])

    def do(self, x):
        global wakeTime
        if x == -1:
            pass
        elif x == 0:
            pass
        elif x == 1:
            pass
        elif x == 2:
            pass
        elif x == 3:
            pass
        elif x == 4:
            self.select.hideSelector(self.root[5])
            menu.toggleMenu(self.root[4], self.root[5], "test", "test")
        elif x == 5:
            buttonBus.button1.deinit()
            pin_alarm = alarm.pin.PinAlarm(pin=board.D1, value=True, pull=True)
            time.sleep(0.5)
            alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

    def looper(self):
        animate.doAnimate(self.root[2], 0.5, 10)

        if buttonBus.getSelectedButton() == 0:
            self.select.lastPos()
            time.sleep(0.2)
            return True
        elif buttonBus.getSelectedButton() == 1:
            self.do(self.select.getSPos())
            time.sleep(0.2)
            return True
        elif buttonBus.getSelectedButton() == 2:
            self.select.nextPos()
            time.sleep(0.2)
            return True
