import cv2
import os

folder = "up"

path = "/home/mark/Documents/Term 8/Image Processing/ImageLable/" + folder + "/"

cv2.namedWindow("preview")

vc = cv2.VideoCapture(0)
im_counter = 0

if vc.isOpened():   # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    elif key == 32:
        img_name = "up_base{}.png".format(im_counter)
        name = path+img_name
        cv2.imwrite(name, frame)
        print("File Written")
        im_counter += 1

cv2.destroyWindow("preview")