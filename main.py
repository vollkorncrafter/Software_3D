import pygame
import math
import numpy as np

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
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

#Im just Here to create the Window :discord_sob_emojie_please_imagine_here:
pygame.display.set_caption("Bye World")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

#"IM a MAIN LOOP IM THE God OF ALL CO.." Bro I made you...cringe
while True:
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
	screen.fill(WHITE)

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
	for point in points:
		Rotated2D = np.dot(rotation_z, point.reshape((3, 1)))
		Rotated2D = np.dot(rotation_y, Rotated2D)
		Rotated2D = np.dot(rotation_x, Rotated2D)
		Projected2D = np.dot(Projection_Matrix, Rotated2D)
		proj_X = int(Projected2D[0][0] * Scale) + WIDTH / 2
		proj_Y = int(Projected2D[1][0] * Scale) + HEIGHT / 2
		pygame.draw.circle(screen, RED, (proj_X,proj_Y), 5)
