import cv2 as cv
import numpy as np

'''
image = cv2.imread("../data/random_items.jpeg") # Insert the name of the file here

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 0, 0], dtype="uint8") #Determine the lower HSV value of the color green, and insert them as your array values [h, s, v]
upper_green = np.array([90, 255, 255], dtype="uint8") #Determine the upper HSV value of the color green, and insert them as your array values [h, s, v]

mask = cv2.inRange(hsv, lower_green, upper_green)

detected_green = cv2.bitwise_and(hsv, hsv, mask = mask)

edited_image = cv2.cvtColor(detected_green, cv2.COLOR_HSV2BGR)

cv2.imwrite("battery_detected.jpg", edited_image)

cv2.imshow("Original Image", image)

cv2.imshow("Battery Detected", edited_image)    

cv2.waitKey(0) #press any key to close the window
'''

# FINDING CENTROID
image = cv.imread("battery_detected.jpg")

imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(image, contours, -1, (0,255,0), 3)

cv.waitKey(0) 






