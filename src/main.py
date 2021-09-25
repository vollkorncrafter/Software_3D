import pygame
import math
import numpy as np
import objekt_loader
from functools import cache
import random
from numba import jit
import pygame.gfxdraw


clock = pygame.time.Clock()
#SCREEN SIZEE
WIDTH = 1376
HEIGHT = 720

#COLORS BABYYY
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#S- S- .. i dont know if i can say it... S- S- Sc.. Scale...
Scale = 100

#ANGELSSSS
Z_angle = 0
Y_angle = 0
X_angle = 0

#Projection_Matrix
Projection_Matrix = np.matrix([
	[1, 0, 0],
	[0, 1, 0]
])

#Vertexes...or....vertecies?
points = []

points = objekt_loader.OBJ()
faces = objekt_loader.FACES()

#print(points)

#Storing Things
projected_points = [
	[n, n] for n in range(len(points))
]


#connecting verts...or should i say...points....
def con_lin_p(i,j,projected_points):
	pygame.draw.line(screen, BLACK, (projected_points[i][0], projected_points[i][1]), (projected_points[j][0], projected_points[j][1]))
#our math
def Get2D_2(Rotated2D):
	Rotated2D = np.dot(rotation_y, Rotated2D)
	Rotated2D = np.dot(rotation_x, Rotated2D)
	Projected2D = np.dot(Projection_Matrix, Rotated2D)
	return Projected2D

def Get2D(point):
	shaped = point.reshape((3,1)) #+ np.matrix([cam_Y,cam_Z,cam_Y]).reshape((3,1))
	Rotated2D = np.dot(rotation_z, shaped)

	return Get2D_2(Rotated2D)





#Im just Here to create the Window :discord_sob_emojie_please_imagine_here:
pygame.display.set_caption("Bye World")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
cam_X = 0
cam_Y = 0
cam_Z = 0
texture=pygame.image.load("block.png").convert()
#"IM a MAIN LOOP IM THE God OF ALL CO.." Bro I made you...cringe
while True:
	screen.fill(BLACK)
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				cam_Y -= 0.1
			if event.key == pygame.K_RIGHT:
				cam_Y += 0.1
			if event.key == pygame.K_DOWN:
				cam_Z -= 0.1
			if event.key == pygame.K_UP:
				cam_Z += 0.1
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()





	X_angle -= 0.1
	Y_angle += 0.1
	Z_angle += 0.1

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
	for point in points:
		Projected2D = Get2D(point)
		proj_X = int(Projected2D[0][0] * Scale) + WIDTH / 2
		proj_Y = int(Projected2D[1][0] * Scale) + HEIGHT / 2
		projected_points[counter] = [proj_X,proj_Y]
		xl.append(int(proj_X))
		yl.append(int(proj_Y))
	for face in range(len(faces)):
		c_face = faces[face]
		fx = int(c_face[0,0]) - 1
		fy = int(c_face[0,1]) - 1
		fz = int(c_face[0,2]) - 1

		pygame.gfxdraw.polygon(screen,[(xl[fx],yl[fx]), (xl[fy],yl[fy]), (xl[fz],yl[fz])],RED)




		counter +=1
	pygame.display.update()


main()
