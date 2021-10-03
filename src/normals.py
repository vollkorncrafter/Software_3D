import numpy

def normalize_v3(arr):
    ''' Normalize a numpy array of 3 component vectors shape=(n,3) '''
    lens = numpy.sqrt( arr[:,0]**2 + arr[:,1]**2 + arr[:,2]**2 )
    arr[:,0] /= lens
    arr[:,1] /= lens
    arr[:,2] /= lens                
    return arr


def Get_Normal(vertices,faces):
    N = []
    print(len(faces))
    print(len(vertices))
    for face in range(len(faces)):
        c_face = faces[face]
        v_1 = int(c_face[0,0]) - 1
        v_2 = int(c_face[0,1]) - 1
        v_3 = int(c_face[0,2]) - 1
        v_1 = vertices[v_1]
        v_2 = vertices[v_2]
        v_3 = vertices[v_3]
        n = numpy.cross(v_1-v_3  , v_2-v_3 )
        n = normalize_v3(n)
        N.append(n)
    return N
