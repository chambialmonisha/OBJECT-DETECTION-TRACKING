import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")
tracker=cv2.TrackerCSRT_create()
returned,img=video.read()
bbox=cv2.selectROI("Tracking",img,False)
tracker.init(img,bbox)
print(bbox)