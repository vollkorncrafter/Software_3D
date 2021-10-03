import numpy as np

def OBJ():
    obj = open("mario.obj", "r")
    obj_list = obj.readlines()
    obj_data = []
    points = []
    faces = []
    for l in obj_list:
        #n_V = l.replace("v","")
        n_V = l
        split = n_V.split()
        obj_data.append(split)

    for i in range(3):
        obj_data.pop(0)
    for c in obj_data:
        if c[0] == "v":
            X = float(c[1])
            Y = float(c[2])
            Z = float(c[3])
            points.append(np.matrix([X, Y, Z]))
    for c in obj_data:
        if c[0] == "f":
            Xf = float(c[1])
            Yf = float(c[2])
            Zf = float(c[3])
            faces.append(np.matrix([Xf, Yf, Zf]))
    return points
    #return points
def FACES():
    obj = open("mario.obj", "r")
    obj_list = obj.readlines()
    obj_data = []
    points = []
    faces = []
    for l in obj_list:
        #n_V = l.replace("v","")
        n_V = l
        split = n_V.split()
        obj_data.append(split)

    for i in range(3):
        obj_data.pop(0)
    for c in obj_data:
        if c[0] == "v":
            X = float(c[1])
            Y = float(c[2])
            Z = float(c[3])
            points.append(np.matrix([X, Y, Z]))
    for c in obj_data:
        if c[0] == "f":
            Xf = float(c[1])
            Yf = float(c[2])
            Zf = float(c[3])
            Xf = int(Xf)
            Yf = int(Yf)
            Zf = int(Zf)
            faces.append(np.matrix([Xf, Yf, Zf]))
    return faces

OBJ()
FACES()