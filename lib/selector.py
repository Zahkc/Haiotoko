from adafruit_display_shapes.circle import Circle

spos = -1
select = Circle(15, 10, 10, outline=0x000000, stroke=2)

def showSelector(splash):
    global spos
    if spos == -1:
        splash.append(select)
        spos += 1
        print("added")

def hideSelector(splash):
    global spos
    if spos != -1:
        splash.pop()

def nextPos():
    global spos
    spos = (spos + 1) % 6
    updatePos()

def lastPos():
    global spos
    spos = (spos - 1) % 6
    updatePos()

def updatePos():
    global select
    if spos == 0:
        select.x = 5
        select.y = 0
    elif spos == 1:
        select.x = 40
        select.y = 0
    elif spos == 2:
        select.x = 70
        select.y = 0
    elif spos == 3:
        select.x = 90
        select.y = 0
    elif spos == 4:
        select.x = 0
        select.y = 220
    elif spos == 5:
        select.x = 110
        select.y = 220
