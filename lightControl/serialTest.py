import time
import serial

ser = serial.Serial('/dev/ttyACM0')
if ser.is_open:
    print("The Port is open \n")
else:
    print("The Port is Closed \n")
while True:
    ser.write(b'0')
    time.sleep(5)
    ser.write(b';')
    time.sleep(5)

