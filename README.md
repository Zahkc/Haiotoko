# Welcome to Haio-Toko 
Haio-Toko (haɪ̯ːoʊtoʊko), an opensource virtual pet for the Adafruit Feather S2 Reverse written in circuit python.
This is being written as a pet project where the objective is an open souce yet simple to make/modify virtual pet.

![](/demo.png)

## Requirements

### Hardware
- [Adafruit S2 Feather Reverse](https://www.adafruit.com/product/5345)
- [PiJuice Zero 800mAh](https://core-electronics.com.au/3-pin-lipo-battery-for-pijuice-zero-800mah.html) or a Lipo with deminsions similar to 7mm x 25mm x 45mm
- 3D Printing Facilities

### Software
No software is necessary but if you wish to modify the code, [MU Code](https://codewith.mu/) is suggested but not necesary.

## Assembly
For the board to mount flush in the case, some slight modifactions will need to be made.

### Cutting
I used some snippers to break down the JST port and the STEMMA QT port. It is important when removing the JST port not to strip the pads, its easier to just cut away at the plastic until the metal prongs are accessable and then cut them at the base. While you have the snippers out you may want to cut the battery leads to size.

### Sticking
You now want to solder the battery to either the now exposed JST pads or the BAT and GND pins.

### Stuffing
Now just kinda stuff that into the 3d printed case.

## Instalation
Installing the code onto the Feather is super easy, just plug in the board into ya computer and drag the contents from the zip onto the root of the circuitpython drive, allowing all over writes. Thats pretty much it.
