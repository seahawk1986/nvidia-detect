#!/usr/bin/env python3

legacy_304 = False
legacy_173 = False
latest = False

with open('/proc/bus/pci/devices', 'r') as p:
    devices = p.readlines()

with open('nvidia_304.x_device_ids', 'r') as nvidia_304_f:
    product_ids_304 = nvidia_304_f.readlines()

with open('nvidia_173_device_ids', 'r') as nvidia_173_f:
    product_ids_173 = nvidia_173_f.readlines()

for device in devices:
    card = device.split('\t')
    if card[0] == '0100': # type is graphics card
        if card[1][:4].lower() == '10de': # vendor is nVidia (0x10de)
            print("nVidia graphics card found")
            if "0x{0}\n".format(card[1][4:]).upper() in product_ids_304:
                legacy_304 = True
            elif "0x{0}\n".format(card[1][4:]).upper() in product_ids_173:
                legacy_173 = True
            else:
                latest = True

if latest is True:
    print("recommending nvidia-graphics-drivers-331-updates")
elif legacy_304 is True:
    print("recommending nvidia-graphics-drivers-304-updates")
elif legacy_173 is True:
    print("recommending nvidia-graphics-drivers-173")
else:
    print("no nVidia card detected...")
