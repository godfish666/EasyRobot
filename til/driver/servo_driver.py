"""
舵机驱动版控制程序
"""
from til.serial.usb2ttl import USB2TTL

class Servo:
    def __init__(self, ID, name):
        self.current_position = 0  # 舵机目前的位置
        self.name = name  # 自定义名
        self.ID = ID  # 驱动板上的接口编号



class Actions:
    def __init__(self, run_time):
        self.run_time = run_time


class ServoDriver:
    def __init__(self, servos):
        self.servos = servos

        self.ttl = USB2TTL("/dev/ttyUSB0", 9600)

    def run_servo(self, servo_id, pos):
        ch = servo_id
        s_ch = hex(ch)
        if len(s_ch) == 3:
            # 一位数转2位数
            s_ch = " 0" + s_ch[2]
        else:
            s_ch = s_ch[2:]

        data = pos
        s_data = hex(data)
        if len(s_data) == 5:
            # 3位数转4位数
            s_data = " " + s_data[3:] + " 0" + s_data[2]
        else:
            s_data = " " + s_data[4:5] + " " + s_data[2:3]

        command = "ff 02 "+s_ch+s_data
        self.ttl.send("str", command)
        pass

    def execute_actions(self, actions):
        pass

