from til.serial.com import COM
import serial

# #十六进制接收示例，以后有得用
# n=s.inwaiting()
# if n:
#     data= str(binascii.b2a_hex(s.read(n)))[2:-1]
#     print(data)

class USB(COM):
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.ser = serial.Serial(port, baud_rate, timeout=1)

    def send(self, str):
        try:
            # 十六进制的发送
            result = self.ser.write(bytes.fromhex(str))  # 写数据
            #print("写总字节数:", result)

            # print(ser.read().hex())  # 读一个字节
            # response = self.ser.readall()  # read a string from port

            # print(response)
            self.ser.close()

        except Exception as e:
            print("出现错误"+e)
            self.ser.close()

