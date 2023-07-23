from adafruit_display_shapes.circle import Circle

select = Circle(15, 10, 10, outline=0x000000, stroke=2)
spos = -1

class selector:

    def __init__(self, positions):
        global spos
        self.size = len(positions)
        self.positions = positions
        spos = -1

    def showSelector(self, selectorGroup):
        global spos
        if spos == -1:
            selectorGroup.append(select)
            spos += 1

    def hideSelector(self, selectorGroup):
        global spos
        if spos != -1:
            selectorGroup.pop()

    def getSPos(self):
        return spos

    def getSize(self):
        return self.size

    def nextPos(self):
        global spos
        spos = (spos + 1) % self.size
        self.updatePos()

    def lastPos(self):
        global spos
        spos = (spos - 1) % self.size
        self.updatePos()

    def updatePos(self):
        global select
        select.x = self.positions[spos][0]
        select.y = self.positions[spos][1]
