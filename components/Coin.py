import pygame
from random import randint
pygame.init()

class Coin():
	def __init__(self, img, coinValue):
		self.coinValue = coinValue
		self.img = pygame.image.load(img)
		self.x = randint(0,700)
		self.y = randint(0,500)
		self.widthHeight = (64,64)
		self.rect = pygame.Rect(self.x,self.y,64,64)	
		
	def createCoinObject(self, gameDisplay):
		gameDisplay.blit(self.img,(self.x,self.y))
	
	def changePos(self):
		self.x = randint(0,700)
		self.y = randint(0,500)