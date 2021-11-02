#!/bin/python3
import cv2
import os
import datetime
import sys
import time

scale_percent = 70
delay = 1500

headless = input("Start headless? (Default: Yes) ")
while True:
    if headless.lower().strip() in ['y','yes','']:
        headless = True
        break
    elif headless.lower().strip() in ['n','no']:
        headless = False
        break
    else:
        headless = input("Start headless? (Default: Yes)")

start_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
try:
    os.mkdir(start_time)
    os.chdir(start_time)
    print("Captures will be stored at: " + start_time)
except:
    sys.exit(1)

#Camera object
capture = cv2.VideoCapture(0)

if headless:
    print("Press ctrl + c to stop.")
    try:
        while True:
            ret,frame = capture.read()
            height = int(frame.shape[0] * scale_percent / 100)
            width = int(frame.shape[1] * scale_percent / 100)
            dim = (width,height)
            time.sleep(delay / 1000)
            resized = cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
            filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
            cv2.imwrite(filename,resized)
            print("Saved " + filename)
    except KeyboardInterrupt:
        capture.release()
        cv2.destroyAllWindows()
else:
    print("Press 'q' key to stop.")
    while True:
        ret,frame = capture.read()
        height = int(frame.shape[0] * scale_percent / 100)
        width = int(frame.shape[1] * scale_percent / 100)
        dim = (width,height)
        if headless == False:
            cv2.imshow('Camera',frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
        resized = cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
        filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        cv2.imwrite(filename,resized)
        print("Saved " + filename)

    capture.release()
    cv2.destroyAllWindows()