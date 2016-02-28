import pygame
from random import randint
import Localizer
pygame.init

class Player():
	def __init__(self, img, maxCoins):
		self.img = pygame.image.load(img)
		self.maxCoins = maxCoins
		self.numCoins = 0
		self.lives = 3
		self.x = randint(0,700)
		self.y = randint(0,500)
		self.widthHeight = (64, 64)
		self.rect = pygame.Rect(self.x,self.y,self.widthHeight[0],self.widthHeight[1])
		self.velX = 0
		self.velY = 0
		self.maxVelX = 0.6
		self.minVelX = -0.6
		self.maxVelY = 0.6
		self.minVelY = -0.6

	def createPlayerObject(self,gameDisplay):
		gameDisplay.blit(self.img, (self.x,self.y))

	def update(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.velX = self.minVelX
			elif event.key == pygame.K_RIGHT:
				self.velX = self.maxVelX
			elif event.key == pygame.K_UP:
				self.velY = self.minVelY
			elif event.key == pygame.K_DOWN:
				self.velY = self.maxVelY
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or pygame.K_RIGHT:
				self.velX = 0
				self.velY = 0
