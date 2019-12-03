import json
import cv2
import numpy as np
import os
from shapely.geometry import Polygon,box,mapping
from flask import Flask
from flask import request, jsonify , redirect, url_for
import requests, json

app = Flask(__name__)
app.config["DEBUG"] = True
@app.route('/point', methods=['GET','POST'])
#json_path="C:\\Amrita\\Pythoncodes\\cola\\JSONdata"

def main():
    ##### open jsonfile ,contains both rectangle and polyline coordinates from postman
    data = request.get_json('')
    #print(data)
    #return "jsondata"
    results = data['videolabeling__1.jpg']['regions']
    ###### make the all points into dictionary with keys and values
    shapes = {}

    for each_result in results:
        shapes[each_result['shape_attributes']['name']] = each_result['shape_attributes']['all_points_x'],each_result['shape_attributes']['all_points_y']

    print("shapes=",shapes)
    #print(type(shapes)

    rp=list(shapes.values())[0]
    flat_rplist = [item for sublist in rp for item in sublist]
    pp=list(shapes.values())[1]

    ####### from values store each index in to variable
    rx1=flat_rplist[0]
    rx2=flat_rplist[1]
    ry1=flat_rplist[2]
    ry2=flat_rplist[3]

    ####### to find x,y,h,w of cropping rectangle
    xyhw=rx1,ry1,ry2-ry1,rx2-rx1

    ###### find polygon from  point of intersction of rectangle and polyline
    r1 = box(rx1,ry1,rx2,ry2)
    p1 = Polygon([list(x_y) for x_y in zip(*pp[::1])])
    x = (p1.intersection(r1))
    x = (x.exterior.xy)
    y=np.array(x).astype(int).ravel().tolist()
    y.extend(xyhw)
    print("intersection points =\n",y)
    int_points=jsonify(y)
    print(int_points)
    return int_points

if(__name__ == '__main__'):
    app.run(debug=True)
