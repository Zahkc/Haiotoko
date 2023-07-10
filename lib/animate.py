import time
import displayio

bounce = False
bounceAmount = 0

def doAnimate(haioGroup: displayio.Group, duration: float, newBounceAmount: int):
    global bounce
    global bounceAmount
    if bounceAmount == 0:
        bounceAmount = newBounceAmount
    if(round(time.monotonic()%duration, 2) == round(duration, 2)):
        if bounce == False:
            bounce = True
            bounceAmount = bounceAmount * -1
            haioGroup.y += bounceAmount
    else:
        if bounce == True:
            bounce = False
