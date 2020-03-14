import time
import serial

x = ''
ser = serial.Serial('/dev/ttyACM0')
if ser.is_open:
    print("The Port is open \n")
else:
    print("The Port is Closed \n")
while True:

    x = input('send byte:')
    x = bytes(x.encode('ascii'))
    ser.write(x)
    time.sleep(2)


