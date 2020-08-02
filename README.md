# dkx50q
Collection for the collected information according the Das Keyboard x50q communication

## Perceptions

* There is no difference between changing the color of one, multiple or all key colors in size of dump.
* Each dump contains exactly 100 frames (except the dump of connecting the device)
    * 50 requests against the keyboard
    * 50 responses of the keyboard
* The connecting device dump contains 510 frames
    * The first 410 frames should be setting up the connection
    * The last 100 frames should be the "initial" setting of the profile
* The difference between the dumps is "hidden" in `usb.capdata`
    * Changing the backlight of one button leads to 4 differences in the `usb.capdata` (It seems that each request is done twice, but this has to be verified. 2 `usb.capdata` looks similar on the first look)

## Other Perceptions

| Profile | Bytes 2-5 |
| --- | --- |
| red | 60 2a 80 98 |
| blue | 20 4a ca 97 |
| green | 80 c9 1b 97 |


