
import cv2
import numpy
import pandas as pd

# This function allows us to create a descending sorted list of contour areas.
def contour_area(contours):
     
    # create an empty list
    cnt_area = []
     
    # loop through all the contours
    for i in range(0,len(contours),1):
        # for each contour, use OpenCV to calculate the area of the contour
        cnt_area.append(cv2.contourArea(contours[i]))
 
    # Sort our list of contour areas in descending order
    list.sort(cnt_area, reverse=True)
    return cnt_area

def find_edge(contours, number_of_boxes = 1):
    # Call our function to get the list of contour areas
    cnt_area = contour_area(contours)
    result = []
    # Loop through each contour of our image
    for i in range(0,len(contours),1):
        cnt = contours[i]
 
        # Only draw the the largest number of boxes
        if (cv2.contourArea(cnt) > cnt_area[number_of_boxes]):
             
            # Use OpenCV boundingRect function to get the details of the contour
            x,y,w,h = cv2.boundingRect(cnt)
            result.append([x,y,w,h])

    return result

def count(edge):
    x, y, w, h = edge[0], edge[1], edge[2], edge[3]
    return [x + w/2, y + h/2]

def find_centers(contours, number = 1):
    edges = find_edge(contours, number)
    centers = []
    for edge in edges:
        centers.append(count(edge))
    return centers 

def draw_bounding_box(contours, image, number_of_boxes = 1):
    # draws the top (number of boxes) bounding rectangle

    # note: 0,0 is top right, y-axis goes positive downwards, x axis as usual
    edges = find_edge(contours, number_of_boxes)
    for edge in edges:
        x, y, w, h = edge[0], edge[1], edge[2], edge[3]
        image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

    return image


# read image
img = cv2.imread('battery_detected.jpg')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)[1]

# get contours
result = img.copy()
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
result = draw_bounding_box(contours, result, 2)
edges = find_edge(contours, 2)
print(edges)
centers = find_centers(contours, 2)
print(centers)
cv2.imshow("bounding_box", result)

# save resulting image
cv2.imwrite('box.jpg',result)      

# show thresh and result    
cv2.imshow("bounding_box", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
