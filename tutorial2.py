import serial
import time


ser = serial.Serial("/dev/cu.usbmodem1421", 9600)
time.sleep(1) #give the connection a second to settle
while True:

    message =input('Enter your message: ')
    message = message.encode("utf-8")
    ser.write(message)
    data = ""
    while len(data)< len(message):
        data += ser.readline().decode("utf-8").replace("\r\n","")
    print(data)
