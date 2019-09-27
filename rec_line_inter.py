import cv2
import numpy as np
from shapely.geometry import Polygon,box,mapping

#plot points on image
img = cv2.imread('cola1.jpg')
A = np.array([[1130,285],[2690,4629]])
img = cv2.rectangle(img, (1130,285),(2690,4629), (0,255,0), 4)
B = np.array([[2280,118],[2339,590],[2437,1248 ],[3007,1779 ],[ 3430,1356 ],[3440,295 ],[2319,108 ]], np.int32)
cv2.polylines(img, [B], True, (0,255,255), 3)
cv2.imwrite('cola1draw.jpg',img)

#find polygon from  point of intersction of rectangle and polyline
r1 = box(1130,285,2690,4629)
p1 = Polygon([(2280,118), (2339,590), (2437,1248),(3007,1779),(3430,1356),(3440,295),(2319,108)])
x = print(p1.intersection(r1))
print(type(x))

img = cv2.imread("cola1.jpg")
height = img.shape[0]
width = img.shape[1]

mask = np.zeros((height, width), dtype=np.uint8)
points = np.array([[[1130,285],[2300,285,],[2437,1248], [ 2690, 1483],[2689,4929],[1130,4929]]])# points from x
cv2.fillPoly(mask, points, (255))
cv2.imwrite("maskk.jpg",mask)
#img2=cv2.imread('maskk.jpg')

res = cv2.bitwise_and(img,img,mask = mask) #to take common region masking
rect = cv2.boundingRect(points) # returns (x,y,w,h) of the rect
cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]] #0,1,2,3 are x,y,w,h
#print(rect[1])
#print(rect[0])
cv2.imwrite("cropped.jpg" , cropped )









#refference site
#https://stackoverflow.com/questions/55212592/how-to-remove-multiple-polygons-using-opencv-python
#https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python
