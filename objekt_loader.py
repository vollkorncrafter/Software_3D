import numpy as np

def OBJ():
    obj = open("suzanne.txt", "r")
    obj_list = obj.readlines()
    points = []
    for l in obj_list:
        n_V = l.replace("v","")
        split = n_V.split()
        X = float(split[0]) / 15
        Y = float(split[1]) / 15 - 3
        Z = float(split[2]) / 15
        points.append(np.matrix([X, Y, Z]))
    return points
