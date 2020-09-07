import pygame
from AulaEngine.core.GameObject import *
from AulaEngine.core.Component import *
from data.lib.move import *



class Player(GameObject):
	def __init__(self, group):
		super().__init__(
			group=group,
			name="Player" 
		)


		self.moveComponent = Move(speed=5) # atribuindo o valor 5 na velocidade 

		self.addComponent(self.moveComponent)




	def update(self):
		# setando a posiçaõ nos rect
		self.rect.x = self.position.x
		self.rect.y = self.position.y

		#self.getComponent('Move').update()

		# atualizando os componentes
		self.updateComponents()
