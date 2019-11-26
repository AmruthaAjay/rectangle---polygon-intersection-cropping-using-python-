import json
import cv2
import numpy as np
from shapely.geometry import Polygon,box,mapping
from flask import Flask
from flask import request, jsonify
import requests, json

app = Flask(__name__)

@app.route('/')

def intersection_imgplot():
    ##### import jsonfile ,contains both rectangle and polyline coordinates
    with open('C:\\Amrita\\Pythoncodes\\cola\\JSONdata\\cola.json') as f:
        data = json.load(f)

    results = data['videolabeling__1.jpg']['regions']

    ###### make the all points into dictionary with keys and values
    shapes = {}

    for each_result in results:
        shapes[each_result['shape_attributes']['name']] = each_result['shape_attributes']['all_points_x'],each_result['shape_attributes']['all_points_y']

    print("shapes=",shapes)
    #print(type(shapes)

    #for key in shapes:
        #for t in shapes[key]:
            #print(t)
            #for i in t:
                #print(i) #prints all elements in dictionary {shapes}

    ###### extract keys and values from dictionary
    for keys, values in shapes.items():
        print('{}= {}'.format(keys, values))
        #print(keys)
        #print(values)
        #print(type(values))
        #first_key = list(shapes)[0]
        #first_val = list(shapes.values())[0]
        #a = [items for t in values for items in t]
        #print(a)
        #print(type(a))
        #pts = np.asarray(a) # both rectangle and polygon Points
        #print(pts)

    ####### from values store each index in to variable
    rx1=list(shapes.values())[0][0][0]
    rx2=list(shapes.values())[0][0][1]
    ry1=list(shapes.values())[0][1][0]
    ry2=list(shapes.values())[0][1][1]
    px1=list(shapes.values())[1][0][0]
    px2=list(shapes.values())[1][0][1]
    px3=list(shapes.values())[1][0][2]
    px4=list(shapes.values())[1][0][3]
    px5=list(shapes.values())[1][0][4]
    px6=list(shapes.values())[1][0][5]
    px7=list(shapes.values())[1][0][6]
    py1=list(shapes.values())[1][1][0]
    py2=list(shapes.values())[1][1][1]
    py3=list(shapes.values())[1][1][2]
    py4=list(shapes.values())[1][1][3]
    py5=list(shapes.values())[1][1][4]
    py6=list(shapes.values())[1][1][5]
    py7=list(shapes.values())[1][1][6]


    ##### plot points on image , to know if points rect, poly intersects

    img = cv2.imread('C:\\Amrita\\Pythoncodes\\cola\\imgs\\cola1.jpg')
    img = cv2.rectangle(img, (rx1,ry1),(rx2,ry2), (0,255,0), 4)
    P = np.array([[px1,py1],[px2,py2],[px3,py3],[px4,py4],[px5,py5],[px6,py6],[px7,py7]], np.int32)
    img = cv2.polylines(img, [P], True, (0,255,255), 3)
    cv2.imwrite('C:\\Amrita\\Pythoncodes\\cola\\result\\cola1draw.jpg',img)


    ###### find polygon from  point of intersction of rectangle and polyline

    r1 = box(rx1,ry1,rx2,ry2)
    p1 = Polygon([(px1,py1), (px2,py2), (px3,py3),(px4,py4),(px5,py5),(px6,py6),(px7,py7)])
    x = (p1.intersection(r1))
    x = (x.exterior.xy)
    #print(x) # (x) pints are float points
    #print(type(x))#class type 'tuple'
    y=np.asarray(x).astype(int)
    print("intersection points =\n",y)

    ##### from intersection points(y) , store each index value into a variable
    ix1=y[0][0]
    ix2=y[0][1]
    ix3=y[0][2]
    ix4=y[0][3]
    ix5=y[0][4]
    ix6=y[0][5]
    iy1=y[1][0]
    iy2=y[1][1]
    iy3=y[1][2]
    iy4=y[1][3]
    iy5=y[1][4]
    iy6=y[1][5]

    #for elts in y:
    #    for j in elts:
    #        print(j)  # prints all intersection points in y

    ##### read input image here
    img = cv2.imread("C:\\Amrita\\Pythoncodes\\cola\\imgs\\cola1.jpg")
    height = img.shape[0]
    width = img.shape[1]

    ####### to find image masking

    mask = np.zeros((height, width), dtype=np.uint8)
    # points from y(intersection points) and rectangle
    points = np.array([[[rx1,ry1],[ix1,iy1],[ix2,iy2],[ix3,iy3],[ix4,iy4],[rx2,ry2],[rx1,ry2]]])
    # gives white colour to the masked region nd all other region willbe black
    cv2.fillPoly(mask, points, (255,255,255))
    # save img with masked region in white color
    cv2.imwrite("C:\\Amrita\\Pythoncodes\\cola\\result\\maskk.jpg",mask)
    #bitwise_and operation to take common region masking
    res = cv2.bitwise_and(img,img,mask = mask)
    #write and save mask images
    cv2.imwrite("C:\\Amrita\\Pythoncodes\\cola\\result\\ress.jpg" , res )


    ##### to get output image , cropped image
    # returns (x,y,w',h') of the required o/p rect ,  not actual img size
    rect = cv2.boundingRect(points)
    #0,1,2,3 are x,y,w',h' respectively
    cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
    # write and save croped images , final output
    cv2.imwrite("C:\\Amrita\\Pythoncodes\\cola\\result\\final_cropped.jpg" , cropped )

if __name__=='__main__':
    intersection_imgplot()
    app.run(host='localhost',debug= True)
