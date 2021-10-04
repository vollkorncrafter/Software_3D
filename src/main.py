from numba.core.types.misc import literal
import pygame
import math
import numpy as np
import objekt_loader
from functools import cache
import random
from numba import jit
import pygame.gfxdraw
import time
import normals as n
num = 0


clock = pygame.time.Clock()
#SCREEN SIZEE
WIDTH = 500
HEIGHT = 500

#COLORS BABYYY
WHITE = (255, 150, 200,60)
RED = (270, 255, 255)
BLACK = (0, 0, 0)
W = (0,0,0)

#S- S- .. i dont know if i can say it... S- S- Sc.. Scale...
Scale = 100

#ANGELSSSS
Z_angle = 25
Y_angle = 25
X_angle = 25


#Projection_Matrix
Projection_Matrix = np.matrix([
	[1, 0, 0],
	[0, 1, 0]
])

#Vertexes...or....vertecies?
points = []

points = objekt_loader.OBJ()
faces = objekt_loader.FACES()


def light_multiply(v1,v2):
	C = v1 * v2
	if C > 255:
		return 255
	else:
		return C


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0

#print(points)
def get_Light(Normals,face):
	n_vec = Normals[face]
	n_vec = n_vec[0]
	n_vec = n_vec.tolist()
	v_1 = n_vec[0]
	v_2 = n_vec[1]
	v_3 = n_vec[2]
	v_1 = get_change(v_1,1)
	v_2 = get_change(v_2,1)
	v_3 = get_change(v_3,1)
	Q = (v_1 + v_2 + v_3) / 3
	L = Q / 100
	return L


#Storing Things
projected_points = [
	[n, n] for n in range(len(points))
]

def Sort(l1,l2):
	zipped_lists = zip(l1, l2)
	sorted_pairs = sorted(zipped_lists)

	tuples = zip(*sorted_pairs)
	l1, l2 = [ list(tuple) for tuple in  tuples]
	return l2

def Get_Z(faces,PointsInSpace):
	Z = []
	for face in range(len(faces)):
		c_face = faces[face]
		v_1 = int(c_face[0,0]) - 1
		v_2 = int(c_face[0,1]) - 1
		v_3 = int(c_face[0,2]) - 1
		v_1 = PointsInSpace[v_1]
		v_2 = PointsInSpace[v_2]
		v_3 = PointsInSpace[v_3]
		z_1 = 1/(10 - v_1[2][0])
		z_2 = 1/(10 - v_2[2][0])
		z_3 = 1/(10 - v_3[2][0])
		z = (z_1 + z_2 + z_3) / 3
		Z.append(z)
	return Z

#our math
def Get_Projected2D(Rotated2D):
	Projected2D = np.dot(Projection_Matrix, Rotated2D)
	return Projected2D



def Get_Rotated2D(point,cam_Y,cam_Z,cam_X):
	shaped = point.reshape((3,1))
	Camera = np.matrix([
			[cam_X],
			[cam_Y],
			[cam_Z],
		])
	Camera = Camera.reshape((3,1))
	shaped = np.subtract(shaped, Camera)
	Rotated2D = np.dot(rotation_z, shaped)
	Rotated2D = np.dot(rotation_y, Rotated2D)
	Rotated2D = np.dot(rotation_x, Rotated2D)

	return Rotated2D

####### + np.matrix([cam_X,cam_Z,cam_Y]).reshape((3,1))

#Im just Here to create the Window :discord_sob_emojie_please_imagine_here:
#pygame.display.set_caption("Bye World")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.init()
pygame.display.update()
screen.fill(W)
cam_X = 0
cam_Y = 0
cam_Z = 0

Face_Col = []
lila = False
for i in range(len(faces)):
	if lila == False:
		color = (136,0,255)
		lila = True
	else:
		lila = False
		color = (0,0,0)
	Face_Col.append(color)






#"IM a MAIN LOOP IM THE God OF ALL CO.." Bro I made you...cringe
while True:
	screen.fill(W)
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				cam_Z += 0.1
			if event.key == pygame.K_RIGHT:
				cam_X += 0.1
			if event.key == pygame.K_DOWN:
				cam_Y += 0.1
			if event.key == pygame.K_UP:
				cam_X += 0.1
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#X_angle += 0.01
	#Y_angle += 0.01
	#Z_angle += 0.01
	Z_angle, X_angle = pygame.mouse.get_pos()
	X_angle = X_angle / 50

	Z_angle = Z_angle / 50

	Z = []

	#ROTATION GOES BRRRRR
	# Z
	rotation_z = np.matrix([
		[math.cos(Z_angle), -math.sin(Z_angle), 0],
		[math.sin(Z_angle), math.cos(Z_angle), 0],
		[0, 0, 1],
	])
	# Y
	rotation_y = np.matrix([
		[math.cos(Y_angle), 0, math.sin(Y_angle)],
		[0, 1, 0],
		[-math.sin(Y_angle), 0, math.cos(Y_angle)],
	])
	# X
	rotation_x = np.matrix([
		[1, 0, 0],
		[0, math.cos(X_angle), -math.sin(X_angle)],
		[0, math.sin(X_angle), math.cos(X_angle)],
	])

	#Heres where the fun begins ;)
	#oldskool counter boys
	counter = 0 # i is kinda lame
	xl = []
	yl = []
	PointsInSpace = []
	for point in points:
		Rotated2D = Get_Rotated2D(point,cam_Y,cam_Z,cam_X)

		Projected2D = Get_Projected2D(Rotated2D)
		proj_X = int(Projected2D[0][0] * Scale) + WIDTH / 2
		proj_Y = int(Projected2D[1][0] * Scale) + HEIGHT / 2
		projected_points[counter] = [proj_X,proj_Y]
		xl.append(proj_X)
		yl.append(proj_Y)
		PointsInSpace.append(Rotated2D)
	Z = Get_Z(faces, PointsInSpace)
	Normals = n.Get_Normal(points,faces)
	Face_Col = Sort(Z,Face_Col)
	faces = Sort(Z,faces)
	Normals = Sort(Z,Normals)
	for face in range(len(faces)):
		c_face = faces[face]
		fx = int(c_face[0,0]) - 1
		fy = int(c_face[0,1]) - 1
		fz = int(c_face[0,2]) - 1
		L = get_Light(Normals,face)
		R = 255
		G = 255
		B = 51
		R = light_multiply(R,L)
		G = light_multiply(G,L)
		B = light_multiply(B,L)

		pygame.gfxdraw.filled_polygon(screen,[(xl[fx],yl[fx]), (xl[fy],yl[fy]), (xl[fz],yl[fz])],(R,G,B))
		pygame.gfxdraw.aapolygon(screen,[(xl[fx],yl[fx]), (xl[fy],yl[fy]), (xl[fz],yl[fz])],(0,0,0))

		counter +=1
	pygame.display.update()
	fps = clock.get_fps()
	print(fps)
	#num +=1
	#pygame.image.save_extended(screen, "img/"+str(num)+".png")


main()
