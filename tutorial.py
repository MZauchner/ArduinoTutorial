import serial #Import Serial Library

ser  = serial.Serial('/dev/cu.usbmodem1421',9600) #Create Serial port object called arduinoSerialData

while (1==1):

#    ser.write("123\n".encode("utf-8"))
    myData = ser.readline()
    myData = myData.decode("utf-8")
    print(myData)

ser.close()
