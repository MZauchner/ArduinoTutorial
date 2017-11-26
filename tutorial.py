import serial #Import Serial Library
 
arduinoSerialData = serial.Serial('com4',9600) #Create Serial port object called arduinoSerialData
 
 
while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        myData = myData.decode("utf-8")
        print(myData)
