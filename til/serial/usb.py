from til.serial.com import COM
import serial


class UsbCOM(COM):
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.ser = serial.Serial(port, baud_rate, timeout=1)

    def send(self, str):
        # try:

            # while 1:
        self.ser.write(bytes(str, "UTF-8"))  # writ a string to port

        # response = self.ser.readall()  # read a string from port

        # print(response)

        # except  :

        self.ser.close()
