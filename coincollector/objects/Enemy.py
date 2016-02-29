import pygame
from random import randint
from coincollector.base import Localizer

class Enemy():
	def __init__(self, img):
		self.img = pygame.image.load(img)
		self.x = randint(0,700)
		self.y = randint(0,500)
		self.velX = 0
		self.velY = 0
		self.maxVel = 0
		self.minVel = 0
		self.velInc = 0.01
		self.widthHeight = (64,64)
		self.timer = 0
		self.rect = pygame.Rect(self.x,self.y,self.widthHeight[0],self.widthHeight[1])

	def update(self,playerX,playerY):
		if playerX > self.x:
			self.x += self.maxVel
		if playerX < self.x:
			self.x += self.minVel
		if playerY < self.y:
			self.y += self.minVel
		if playerY > self.y:
			self.y += self.maxVel

		self.timer += 1
		if self.timer >= 1000:
			self.timer = 0
			self.maxVel += self.velInc
			self.minVel -= self.velInc
			if self.maxVel >= 3:
				self.maxVel += 0
			if self.minVel <= 3:
				self.minVel -= 0

	def changePos(self,x,y):
		self.x = x
		self.y = y

	def createObject(self, gameDisplay):
		gameDisplay.blit(self.img, (self.x, self.y))