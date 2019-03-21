# -*- coding: utf-8 -*-                 #通过声明可以在程序中书写中文
import RPi.GPIO as GPIO  # 引入RPi.GPIO库函数命名为GPIO
import time  # 引入计时time函数


class MotorDriver:
    # 定义电机控制版接口和GPIO口的对应关系，GPIO口采用Board编码，左电机控制板输入端口，右GPIO输出端口
    # A左前轮，B右前轮，C左后轮，D右后轮
    A1 = 7
    A2 = 11
    B1 = 12
    B2 = 13
    C1 = 15
    C2 = 16
    D1 = 18
    D2 = 22

    def __init__(self):
        # BOARD编号方式，基于插座引脚编号
        GPIO.setmode(GPIO.BOARD)  # 将GPIO编程方式设置为BOARD模式
        # 输出模式
        GPIO.setup(MotorDriver.A1, GPIO.OUT)
        GPIO.setup(MotorDriver.A2, GPIO.OUT)
        GPIO.setup(MotorDriver.B2, GPIO.OUT)
        GPIO.setup(MotorDriver.B1, GPIO.OUT)
        GPIO.setup(MotorDriver.C1, GPIO.OUT)
        GPIO.setup(MotorDriver.C2, GPIO.OUT)
        GPIO.setup(MotorDriver.D2, GPIO.OUT)
        GPIO.setup(MotorDriver.D1, GPIO.OUT)

    def run_left_front_wheel(self, direction):
        if direction == 1:
            GPIO.output(MotorDriver.A1, GPIO.HIGH)
            GPIO.output(MotorDriver.A2, GPIO.LOW)

        elif direction == 0:
            GPIO.output(MotorDriver.A1, GPIO.LOW)
            GPIO.output(MotorDriver.A2, GPIO.HIGH)

    def run_right_front_wheel(self, direction):
        if direction == 1:
            GPIO.output(MotorDriver.B1, GPIO.HIGH)
            GPIO.output(MotorDriver.B2, GPIO.LOW)

        elif direction == 0:
            GPIO.output(MotorDriver.B1, GPIO.LOW)
            GPIO.output(MotorDriver.B2, GPIO.HIGH)

    def run_left_rear_wheel(self, direction):
        if direction == 0:
            GPIO.output(MotorDriver.C1, GPIO.HIGH)
            GPIO.output(MotorDriver.C2, GPIO.LOW)

        elif direction == 1:
            GPIO.output(MotorDriver.C1, GPIO.LOW)
            GPIO.output(MotorDriver.C2, GPIO.HIGH)

    def run_right_rear_wheel(self, direction):
        if direction == 0:
            GPIO.output(MotorDriver.D1, GPIO.HIGH)
            GPIO.output(MotorDriver.D2, GPIO.LOW)

        elif direction == 1:
            GPIO.output(MotorDriver.D1, GPIO.LOW)
            GPIO.output(MotorDriver.D2, GPIO.HIGH)

    def go_forward(self, t=0):
        self.run_left_front_wheel(1)
        self.run_right_front_wheel(1)
        self.run_left_rear_wheel(1)
        self.run_right_rear_wheel(1)
        if time != 0:
            time.sleep(t)
            self.stop()
        pass

    def backward(self, t=0):
        self.run_left_front_wheel(0)
        self.run_right_front_wheel(0)
        self.run_left_rear_wheel(0)
        self.run_right_rear_wheel(0)
        if time != 0:
            time.sleep(t)
            self.stop()
        pass

    # 原地左转
    def turn_left(self, t=0):
        self.run_left_front_wheel(0)
        self.run_right_front_wheel(1)
        self.run_left_rear_wheel(0)
        self.run_right_rear_wheel(1)
        if time != 0:
            time.sleep(t)
            self.stop()
        pass

    # 原地右转
    def turn_right(self, t=0):
        self.run_left_front_wheel(1)
        self.run_right_front_wheel(0)
        self.run_left_rear_wheel(1)
        self.run_right_rear_wheel(0)
        if time != 0:
            time.sleep(t)
            self.stop()
        pass

    # 直走并左转
    def walk_left(self):
        pass

    # 直走并右转
    def walk_right(self):
        pass

    # 后退并左转
    def back_left(self):
        pass

    # 后退并右转
    def back_right(self):
        pass

    def stop(self):
        GPIO.output(MotorDriver.A1, GPIO.LOW)
        GPIO.output(MotorDriver.A2, GPIO.LOW)
        GPIO.output(MotorDriver.B1, GPIO.LOW)
        GPIO.output(MotorDriver.B2, GPIO.LOW)
        GPIO.output(MotorDriver.C1, GPIO.LOW)
        GPIO.output(MotorDriver.C2, GPIO.LOW)
        GPIO.output(MotorDriver.D1, GPIO.LOW)
        GPIO.output(MotorDriver.D2, GPIO.LOW)
        pass

    def close(self):
        GPIO.cleanup()
        pass
