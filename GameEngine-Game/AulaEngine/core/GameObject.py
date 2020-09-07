import pygame

class GameObject(pygame.sprite.Sprite):
	def __init__(self, group=None, name="GameObject", posX=0, posY=0, scaleX=32, scaleY=32, color=(255, 255, 255)):
		if group != None: super().__init__(group)
		else: super().__init__()

		# Variaveis
		self.type = "GameObject"
		self.name = name
		self.position = pygame.math.Vector2(posX, posY)
		self.scale = pygame.math.Vector2(scaleX, scaleY)
		self.visible = True
		self.properties = {}
		self.components = {}
		self.parents = {}

		# Defininfo a imagem e o rect do GameObject
		self.image = pygame.Surface((self.scale.x, self.scale.y))
		self.image.fill(color)
		self.rect = self.image.get_rect()

		# Aplicando a posição inicial no rect
		self.rect.x = self.position.x
		self.rect.y = self.position.y

	# Função para adicionar um component
	def addComponent(self, component):
		if component.type == "Component":
			if not component.name in self.components:
				component.object = self
				self.components[component.name] = component
			else:
				print("Erro: classe -> [GameObject] função -> (addComponent) -> 0 componente "+component.name+" já foi adicionado ao GameObject "+self.name)
		else:
			print("Erro: classe -> [GameObject] função -> (addComponent) -> não foi passado um componente válido.")

	# Função para remover um componente
	def removeComponent(self, component_name):
		if component_name in self.components:
			del self.components[component_name]
		else:
			print("Erro: classe -> [GameObject] função -> (removeComponent) -> O componente "+component_name+" não existe no GameObject "+ self.name)

	# Funão para checar se esse GameObject tem determinado componente
	def hasComponent(self, component_name):
		if component_name in self.components:
			return True
		return False

	# Função para atualizar os componentes
	def updateComponents(self):
		for component in self.components:
			try:
				self.components[component].update()
			except:
				pass


	# Função para movimentar o GameObject
	def move(self, vector2):
		self.position.x += vector2.x
		self.position.y += vector2.y
		self.updateParentPosition()

	# Função para parentear um GameObject 
	def parent(self, GameObject, distance_x=0, distance_y=0):
		obj = GameObject
		obj.parents[obj.name] = [self, distance_x, distance_y]


	# Funçao para atualizar a posição dos GameObjects parentes
	def updateParentPosition(self):
		for obj in self.parents:
			vec = pygame.math.Vector2(
				self.position.x + self.parents[obj][1],
				self.position.y + self.parents[obj][2]
			)
			self.parents[obj][0].setPosition(vec)


	# ----------- GET -----------------

	# Função para pegar um componente
	def getComponent(self, component_name):
		if self.hasComponent(component_name):
			return self.components[component_name]
		else:
			print("Erro: classe -> [GameObject] função -> (getComponent) -> O componente "+component_name+" não existe no GameObject "+self.name)

	# Função para pegar a posição em x de um componente
	def getPosition(self):
		vec = pygame.math.Vector2(self.position.x, self.position.y)
		return vec

	# Função para pegar a posição em x de um componente
	def getPositionX(self):
		return self.position.x

	# Função para pegar a posição em y de um componente
	def getPositionY(self):
		return self.position.y



	# ----------- END GET -----------------


	# ----------- SET -----------------
	
	# Função para setar a posição de um GameObject
	def setPosition(self, vector2):
		self.position.x = vector2.x
		self.position.y = vector2.y
		self.updateParentPosition()

	# Função para setar a posição de um GameObject no eixo x
	def setPositionX(self, int):
		self.position.x = int
		self.updateParentPosition()

	# Função para setar a posição de um GameObject no eixo y
	def setPositionY(self, int):
		self.position.y = int
		self.updateParentPosition()

	# ----------- END SET -----------------
