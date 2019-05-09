#Import required libraries
import cv2
import numpy as np

#Open the camera:
""""
(0) - Webcam
(1) - External camera
"""
cam = cv2.VideoCapture(0)

if cam.isOpened():
	ret, img = cam.read()
	img = cv2.flip(img, 1)
	cv2.rectangle(img, pt1=(300, 300), pt2=(100, 100), color=(0, 255, 0), thickness=1)
	cv2.imshow("camera", img)
	cv2.waitKey(0)


