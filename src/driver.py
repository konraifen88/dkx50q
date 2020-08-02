#!/usr/bin/env python3

import usb1
import usb.core

VENDOR_ID = 0x24f0
PRODUCT_ID = 0x202b

class usbDriver():
    

    def __init__(self):
        # connect
        print('TODO: Initialize.')

    def hotplug_register(self):
        print('FIX: hotplug_register.')
        with usb1.USBContext() as context:
            if not context.hasCapability(usb1.CAP_HAS_HOTPLUG):
                print('Hotplug support is missing. Please update your libusb version.')
                return
            print('Registering hotplug callback...')
            opaque = context.hotplugRegisterCallback(self.hotplug_callback)
            print('Callback registered. Monitoring events, ^C to exit')
            try:
                while True:
                    context.handleEvents()
            except (KeyboardInterrupt, SystemExit):
                print('Exiting')

    def hotplug_callback(self, context, device, event):
        print("Hotplug %s: %s" % ({
            usb1.HOTPLUG_EVENT_DEVICE_ARRIVED: 'arrived', 
            usb1.HOTPLUG_EVENT_DEVICE_LEFT: 'left',}[event],device,))

    def connect(self):
        self.dev = usb.core.find(idVendor=VENDOR_ID,idProduct=PRODUCT_ID)
        self.cfg = self.dev.get_active_configuration()
        print(self.cfg.interfaces())

    def list(self):
        # currently just lists all, will add just kb later
        with usb1.USBContext() as context:
            for device in context.getDeviceIterator(skip_on_error=True):
                print('ID %04x:%04x' % (device.getVendorID(), device.getProductID()), '->'.join(str(x) for x in ['Bus %03i' % (device.getBusNumber(), )] + device.getPortNumberList()), 'Device', device.getDeviceAddress())

    def __del__(self):
        print('TODO: Disconnect.')

if __name__ == '__main__':
    driver = usbDriver()
    # List all usb devices
    # driver.list()
    
    # Register hotplug
    #driver.hotplug_register()
    
    # Connect
    driver.connect()
