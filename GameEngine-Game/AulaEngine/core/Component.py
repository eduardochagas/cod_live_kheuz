
class Component():
	def __init__(self, GameObject, name):
		if GameObject.type == "GameObject":
			self.type = "Component"
			self.name = name
			self.object = GameObject

		else:
			print("Erro: class -> [Component] - > não foi passado um parâmetro GameObject")
			