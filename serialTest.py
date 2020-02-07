import time
import serial

while True:

    ser = serial.Serial('/dev/ttyACM0')

    if ser.is_open:
        print("The Port is open \n")
    else:
        print("The Port is Closed \n")

    ser.write(b'hello')
    time.sleep(1)
    response = ser.read(5)
    print(response)
    time.sleep(5)
