# TODO make work :)

import usb1
import usb.core
import usb.util
import os
import sys
import libusb
from usb import util
import math

PRODUCT_ID = 0x24f0
VENDOR_ID = '202b'

dev = usb.core.find(idVendor=VENDOR_ID,idProduct=PRODUCT_ID)

print(dev)

with usb1.USBContext() as context:
    handle=context.openByVendorIDAndProductID(
        VENDOR_ID,PRODUCT_ID,)
    handle.claimInterface(0)
    handle.setInterface(0)


