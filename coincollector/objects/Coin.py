import pygame
from random import randint
from coincollector.base import Localizer
class Coin():
	def __init__(self, img, coinValue):
		self.coinValue = coinValue
		self.img = pygame.image.load(img)
		self.x = randint(0,Localizer.dispWidth - 100)
		self.y = randint(0,Localizer.dispHeight - 100)
		self.widthHeight = (64,64)
		self.rect = pygame.Rect(self.x,self.y,self.widthHeight[0],self.widthHeight[1])	
		
	def createObject(self, gameDisplay):
		gameDisplay.blit(self.img,(self.x,self.y))
	
	def changePos(self):
		self.x = randint(0,Localizer.dispWidth - 100)
		self.y = randint(0,Localizer.dispHeight - 100)