from til.serial.com import COM
import serial



class USB2TTL(COM):
    """
    使用举例
    com = USB2TTL('COM3', 9600)
    com.send("ff 12 0f e7 04")  # 十六进制数据包输出格式'10 11 12 34 3f'
    """
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.ser = serial.Serial(port, baud_rate, timeout=1)

    def send(self, data_type, data):
        try:
            if data_type == "str":
                # data类型为十六进制的字符串，如"ff 12 0f e7 04"
                result = self.ser.write(bytes.fromhex(str))

            if  data_type == "bytes":
                # data类型为字节数组bytes
                result = self.ser.write(data)
            # print("写总字节数:", result)
        except Exception as e:
            print("出现错误"+e)
            self.ser.close()

    def recive(self,style,length):
        # #十六进制接收示例，以后有得用
        # n=s.inwaiting()
        # if n:
        #     data= str(binascii.b2a_hex(s.read(n)))[2:-1]
        #     print(data)
        # print(ser.read().hex())  # 读一个字节
        # response = self.ser.readall()  # read a string from port

        # print(response)
        pass

    def close(self):
        self.ser.close() #关闭后要重新new一个对象
