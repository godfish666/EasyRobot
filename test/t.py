print("ff 02 "+hex(8)+hex(1000 & 0xff)+hex(1000 >> 8))
ch=15
s_ch=hex(ch)
if len(s_ch)==3:
    s_ch=" 0"+s_ch[2]
else :
    s_ch=s_ch[2:]
print(s_ch)

data = 2500
print(hex(data))
s_data=hex(data)
if len(s_data)==5:
    s_data=" "+s_data[3:]+" 0"+s_data[2]
else :
    s_data=" "+s_data[4:5]+" "+s_data[2:3]
print(s_data)