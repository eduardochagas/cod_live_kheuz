import pygame
from pygame.locals import *
from data.lib import * # onde fica as libs do nosso jogo
from AulaEngine.core import * # importa todas as classes da nossa engine 

class GameApp():
	def __init__(self):
		self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption(WINDOW_TITLE)
		self.clock = pygame.time.Clock()
		self.deltaTime = 0.0

		# Grupos
		self.all_sprites = pygame.sprite.Group()
		#---------

		# GameObjects
		self.player = Player(self.all_sprites) # essa classe Player é do arquivo Player em: data.lib 
		
		self.obj = GameObject(group=self.all_sprites, color=(0, 0, 255))

		#self.obj.parent(self.player, -32, 0)
		#----------------

		self.gameLoop = True
		self.run()

	def run(self):
		while self.gameLoop:
			self.deltaTime = self.clock.tick(FPS)
			self.events()
			self.update()
			self.render()

	def events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.gameLoop = False

	def update(self):
		pygame.display.update()

		self.obj.rect.x = int(self.obj.position.x)
		self.obj.rect.y = int(self.obj.position.y)

		self.all_sprites.update()


	def render(self):
		self.display.fill((0, 0, 0))
		# Desenhando as sprites do grupo all_sprites
		self.all_sprites.draw(self.display)

if __name__ == "__main__":
	GameApp()