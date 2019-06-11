# Import required libraries
import cv2
import numpy as np

# Open the camera:
""""
(0) - system inbuilt camera
(1) - External camera
"""
cam = cv2.VideoCapture(0)

if cam.isOpened():
	# read the frames from the Camera
	_, img = cam.read()
	# flip the image for the convenience (optional)
	img = cv2.flip(img, 1)
	# draw a rectangle randomly on the image
	cv2.rectangle(img, pt1=(300, 300), pt2=(0, 0), color=(0, 255, 0), thickness=2)
	# take that rectangle as the region of interest
	roi = img[0:300, 0:300]
	# convert the roi to gray scale for ease of processing
	gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	# get the edges from the gray scale image
	_, edges = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
	# get the contours from the edges
	_, contours, hierarchy = cv2.findContours(edges.copy(),
											  cv2.RETR_TREE,
											  cv2.CHAIN_APPROX_SIMPLE)
	print(contours)
	# cv2.imshow("img", contours)
	# cv2.waitKey(0)
	# find the length of the contours
	cont_len = len(contours)
	print(cont_len)
	# create a matrix of zeros in the shape of cont_len
	area = np.zeros(cont_len)
	for i in range(0, cont_len):
		area[i] = cv2.contourArea(contours[i])
	index = area.argmax()
	hand = contours[index]
	x, y, w, h = cv2.boundingRect(hand)
	cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 0, 255), 0)
	temp = np.zeros(roi.shape, np.uint8)




	# cv2.imshow("camera", gray)
	# cv2.waitKey(0)


