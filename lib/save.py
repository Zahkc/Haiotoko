import storage
import supervisor
import microcontroller

try:
    storage.remount("/", supervisor.runtime.usb_connected)
except RuntimeError as E:
    print("PC Mode")
    microcontroller.reset()
try:
    with open("/Save/current.json", "a") as save:
        save.write("Take 2")
        save.flush()
except OSError as E:
    print("READ ONLY")
    print(E)
