import cv2
from keras.models import load_model
import numpy as np
from keras.preprocessing import image
import serial

ser = serial.Serial('/dev/ttyACM0')
if ser.is_open:
    print("The Port is open \n")
else:
    print("The Port is Closed \n")

model = load_model('lilKeith.h5')
i = 0
guess = ''
frame = 0
guess_arr = []
valid = 0
last_gesture = 'Nothing'


def serial_out(gesture):
    if last_gesture == gesture:
        return
    else:
        if gesture == 'Go':
            print('\n Go Transition \n')
            ser.write(b'0')

        elif gesture == 'Stop':
            ser.write(b'2')
            print('\n Stop Transition \n')

        elif gesture == 'Okay':
            ser.write(b'1')
            print('\n Okay Transition \n')

    return


def predict_gesture(pic):
    global guess
    img = pic
    img = cv2.resize(img, (255, 255))
    img_tensor = image.img_to_array(img)  # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    val = model.predict(img_tensor)
    max_index = val.argmax()

    if max_index == 0:
        guess = "Go"
    elif max_index == 1:
        guess = "Nothing"
    elif max_index == 2:
        guess = "Okay"
    elif max_index == 3:
        guess = "Stop"

    return guess


cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)

    if i % 60 == 0:
        pred = predict_gesture(frame)
        guess_arr.append(pred)
        if len(guess_arr) == 5:
            validate = max(set(guess_arr), key=guess_arr.count)
            # print('A$AP Keith Predicts: ', validate)
            serial_out(validate)
            last_gesture = validate
            guess_arr = []

    if key == 27:  # exit on ESC
        break
# elif key == 32:     # Space Bar
cv2.destroyWindow("preview")
