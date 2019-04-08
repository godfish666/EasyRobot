
from til.serial.usb2ttl import USB2TTL


com = USB2TTL('COM3', 9600)
com.send("ff 12 f e7 4")  # 十六进制数据包输出格式'10 11 12 34 3f'
