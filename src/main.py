import pygame
import math
import numpy as np
import objekt_loader
from functools import cache
import random


#Clock
#clock = pygame.time.Clock()
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
X_angle = 90

#MATRICESSS
#110010010001000010000100
#010000100001000001000001
#100010001000001000001000
#101010010101010101010000
#111010010110101001011010
#...not that matrix idiot....

#Projection_Matrix
Projection_Matrix = np.matrix([
	[1, 0, 0],
	[0, 1, 0]
])

#Vertexes...or....vertecies?
points = []

#DEFAULT CUBEEEEEE :) #Delte me please
#points.append(np.matrix([-1, -1, 1]))
#points.append(np.matrix([1, -1, 1]))
#points.append(np.matrix([1,  1, 1]))
#points.append(np.matrix([-1, 1, 1]))
#points.append(np.matrix([-1, -1, -1]))
#points.append(np.matrix([1, -1, -1]))
#points.append(np.matrix([1, 1, -1]))
#points.append(np.matrix([-1, 1, -1]))
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

#Im just Here to create the Window :discord_sob_emojie_please_imagine_here:
pygame.display.set_caption("Bye World")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)

#"IM a MAIN LOOP IM THE God OF ALL CO.." Bro I made you...cringe
while True:
	#clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				Y_angle -= 0.1
			if event.key == pygame.K_RIGHT:
				Y_angle += 0.1
			if event.key == pygame.K_DOWN:
				X_angle -= 0.1
			if event.key == pygame.K_UP:
				X_angle += 0.1
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


	pygame.display.update()
	screen.fill(BLACK)

	X_angle -= 0.01
	Y_angle += 0.01

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
	for point in points:
		shaped = point.reshape((3,1))
		Rotated2D = np.dot(rotation_z, shaped)
		Rotated2D = np.dot(rotation_y, Rotated2D)
		Rotated2D = np.dot(rotation_x, Rotated2D)
		Projected2D = np.dot(Projection_Matrix, Rotated2D)
		proj_X = int(Projected2D[0][0] * Scale) + WIDTH / 2
		proj_Y = int(Projected2D[1][0] * Scale) + HEIGHT / 2
		projected_points[counter] = [proj_X,proj_Y]
		R = int(abs(shaped[0]*15)) + 10
		G = int(abs(shaped[1]*15)) + 20
		B = int(abs(shaped[2]*15)) + 50
		#pygame.draw.circle(screen, (R,G,B), (proj_X,proj_Y), 1)
		for face in range(len(faces)):
			c_face = faces[face]
			fx = int(c_face[0,0]) - 1
			fy = int(c_face[0,1]) - 1
			fz = int(c_face[0,2]) - 1
			try:
				pygame.draw.polygon(screen, (57, 156, 223),points=[projected_points[fx], projected_points[fy], projected_points[fz]])
			except:
				pass

		counter +=1


main()
