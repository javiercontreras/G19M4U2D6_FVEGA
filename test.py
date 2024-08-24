from abc import ABC, abstractmethod

class Pelota(ABC):
	@abstractmethod
	def rebotar(self, altura: int):
	    pass
	
class PelotaDeJuguete(Pelota):
	def __init__(self):
		self.rebotes = []
		self.__color = "amarillo"
	def rebotar(self, altura: float):
		self.rebotes = []
		while altura > 0:
			self.rebotes.append(altura)
			self.rebotes.append(0)
			altura //= 2
		return self.rebotes
	
o = PelotaDeJuguete()
print(o._PelotaDeJuguete__color)