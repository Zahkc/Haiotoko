import json
import time
import storage
import displayio
import supervisor
import microcontroller
import adafruit_imageload

class entity:
    def __init__(self):
        pass

    profile = {
        "spritePath": str(),
        "joyMult": float(),
        "name": str(),
        "respectMult": float(),
        "baseJoy": int(),
        "evolutionInterval": int(),
        "baseRespect": int(),
        "lifespan": int()
    }


    character = {
        "profile": str(), #Profile to load
        "age": int(), #Age in seconds
        "joy": float(), #happy or sad
        "respect": float(), #Good or Evil
        "mistakes": int(), #How many mistakes made
        "money": int(), #MONEY
        "nextEventTime": int(), # seconds till event
        "nextEvloutionTime": int(), # seconds till
        "death": int() # seconds till death
    }

    def importSave(self):
        with open("/Save/current.json", "r") as save:
            self.character = json.loads(save.read())
        with open("/Data/Profiles/" + self.character["profile"] + ".json", "r") as importedProfile:
            self.profile = json.loads(importedProfile.read())


    def exportSave(self):
        with open("/Save/current.json", "w") as save:
            save.write(json.dumps(character))
            save.flush()

    def show(self, haioGroup: displayio.Group):
        haio, haioPalette = adafruit_imageload.load(self.profile["spritePath"], bitmap=displayio.Bitmap, palette=displayio.Palette)
        haioPalette.make_transparent(len(haioPalette)-1)
        haioTile = displayio.TileGrid(haio, pixel_shader=haioPalette, x=20, y=100)
        haioGroup.append(haioTile)
