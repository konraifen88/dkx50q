#!/usr/bin/env python3
import usb.core

dev = usb.core.find(idVendor=0x24f0,idProduct=0x202b)
cfg = dev.get_active_configuration()

print(cfg.interfaces())
