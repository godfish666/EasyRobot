from til.serial.COM import COM
import serial


class UsbCOM(COM):
    def __init__(self, port, speed):
        self.port = port
        self.speed = speed
        self.ser = serial.Serial(port, speed, timeout=1)

    def send(self):
        try:

            while 1:
                self.ser.write('s')  # writ a string to port

                response = self.ser.readall()  # read a string from port

                print(response)

        except:

            self.ser.close()
