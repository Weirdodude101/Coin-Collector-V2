import pygame
from random import randint
from coincollector.base import Localizer
import sys
class Player():
	def __init__(self, img, maxCoins):
		self.img = pygame.image.load(img)
		self.maxCoins = maxCoins
		self.numCoins = 0
		self.lives = 3
		self.x = randint(0,Localizer.dispWidth - 100)
		self.y = randint(0,Localizer.dispHeight - 100)
		self.widthHeight = (64, 64)
		self.rect = pygame.Rect(self.x,self.y,self.widthHeight[0],self.widthHeight[1])
		self.velX = 0
		self.velY = 0
		if sys.platform == "win32":
			self.maxVelX = 1.1
			self.maxVelY = 1.1
		else:
			self.maxVelX = 3
			self.maxVelY = 3
		self.minVelX = self.maxVelX * -1
		self.minVelY = self.maxVelY * -1

	def createObject(self,gameDisplay):
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
			if event.key == pygame.K_UP or pygame.K_DOWN:
				self.velY = 0


	def checkCollision(self, value, collision, enemyCollision):
		if collision and not enemyCollision:
			self.numCoins += value
			return True
		elif enemyCollision and not collision:
			self.lives -= 1
			return True
		else:
			return False
