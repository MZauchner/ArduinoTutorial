import serial #Import Serial Library

ser  = serial.Serial('/dev/cu.usbmodem1421',9600) #Create Serial port object

while (1==1):

    myData = ser.readline()
    myData = myData.decode("utf-8")
    print(myData)

ser.close()
