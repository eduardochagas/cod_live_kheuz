import pygame
from pygame.locals import *
from AulaEngine.core.Component import *


class Move(Component):
	def __init__(self, speed=3):
		super().__init__("Move")

		self.speed = speed
		self.vx, self.vy = 0, 0



	def getInputs(self):
		keyboard = pygame.key.get_pressed()

		if keyboard[K_w]:
			self.vy = -1

		elif keyboard[K_s]:
			self.vy = 1


		if keyboard[K_a]:
			self.vx = -1

		elif keyboard[K_d]:
			self.vx = 1 


	def movement(self):
		vec = pygame.math.Vector2(self.vx, self.vy)

		if vec.x != 0 or vec.y != 0:
			vec = vec.normalize()

		vec.x *= self.speed
		vec.y *= self.speed

		self.object.move(vec) 

		self.vx = 0
		self.vy = 0


	def update(self):
		self.getInputs()
		self.movement()
