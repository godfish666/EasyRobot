from til.serial.com import COM
from til.serial.usb import UsbCOM


com = UsbCOM('COM3', 9600)
com.send("asndsadnoisand")
