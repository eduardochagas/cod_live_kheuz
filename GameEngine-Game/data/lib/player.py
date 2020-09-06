import pygame
from AulaEngine.core.GameObject import *
from AulaEngine.core.Component import *

class Move(Component):
	def __init__(self, GameObject):
		super().__init__(GameObject, "Move")

	def update(self):
		self.object.position.x += 2


class Player(GameObject):
	def __init__(self, group):
		super().__init__(
			group=group
		)

		# criando o componente
		self.moveComponent = Move(self)

		# adicionando o componente
		self.addComponent(self.moveComponent)

		print(self.components)


	def update(self):
		# setando a posiçaõ nos rect
		self.rect.x = self.position.x
		self.rect.y = self.position.y

		# atualizando os componentes
		self.updateComponents()
		