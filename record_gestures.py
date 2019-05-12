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
	# read the frames for m the camera
	ret, img = cam.read()
	# flip the mage for the convenience (optional)
	img = cv2.flip(img, 1)
	# draw a rectagle randomly on the image
	cv2.rectangle(img, pt1=(300, 300), pt2=(0, 0), color=(0, 255, 0), thickness=1)
	# take that rectangle as the region of interest
	roi = img[0:300, 0:300]
	# convert the roi to gray scale for ease of processing
	gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	# get the edges from the gray scale image
	_, edges = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)






	# cv2.imshow("camera", gray)
	# cv2.waitKey(0)


