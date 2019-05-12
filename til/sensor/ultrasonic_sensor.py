import RPi.GPIO as GPIO
import time

# 设置 GPIO 模式为 BCM
GPIO.setmode(GPIO.BCM)

# 定义 超声波模块的信号接线 引脚
GPIO_TRIGGER = 23
GPIO_ECHO = 24

# 设置 GPIO 的工作方式 (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


class UltrasonicSensor:
    def startup(self):
        pass

    def distance(self):
        # 发送高电平信号到 Trig 引脚
        GPIO.output(GPIO_TRIGGER, True)

        # 持续 10 us
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        start_time = time.time()
        stop_time = time.time()

        # 记录发送超声波的时刻1
        while GPIO.input(GPIO_ECHO) == 0:
            start_time = time.time()

        # 记录接收到返回超声波的时刻2
        while GPIO.input(GPIO_ECHO) == 1:
            stop_time = time.time()

        # 计算超声波的往返时间 = 时刻2 - 时刻1
        time_elapsed = stop_time - start_time
        # 声波的速度为 343m/s， 转化为 34300cm/s。
        d = (time_elapsed * 34300) / 2

        return d

    def close(self):
        pass