
from til.serial.usb import USB


com = USB('COM3', 9600)
com.send("10 11 12 34 3f")  # 十六进制数据包输出格式'10 11 12 34 3f'
