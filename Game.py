import pygame
import pygame._view
from pygame.locals import *
from components.Window import Window
from components.Player import Player
from components.Message import Message
from components.Coin import Coin
from components.Enemy import Enemy
from components import Localizer
pygame.init()

class Game():
	def __init__(self):
		self.Player = Player(Localizer.player_img, 20)
		self.yellowCoin = Coin(Localizer.yellowCoin_img, 1)
		self.Enemy = Enemy(Localizer.enemy_img)
		self.window = Window(
			Localizer.window_title,
			self.Player.img,
			Localizer.dispWidth,
			Localizer.dispHeight,
			Localizer.red)

	def load(self):
		self.window.clock.tick(30)
		self.gameLoaded = True
		while self.gameLoaded:
			events = pygame.event.get()
			for event in events:
				if event.type == QUIT:
					self.gameLoaded = False

				self.Player.update(event)

			if self.Player.x > Localizer.dispWidth - 64:
				self.Player.x += -5
			elif self.Player.x < 0:
				self.Player.x += 5
			else:
				self.Player.x += self.Player.velX

			if self.Player.y > Localizer.dispHeight - 64:
				self.Player.y += -5
			elif self.Player.y < 0:
				self.Player.y += 5
			else:
				self.Player.y += self.Player.velY

			self.window.gameDisplay.fill(Localizer.blue)
			coinCollision = self.detectCollisions(self.yellowCoin.x,self.yellowCoin.y,self.yellowCoin.widthHeight[0],self.yellowCoin.widthHeight[1],self.Player.x,self.Player.y,self.Player.widthHeight[0],self.Player.widthHeight[1])
			enemyCollision = self.detectCollisions(self.Enemy.x,self.Enemy.y,self.Enemy.widthHeight[0],self.Enemy.widthHeight[1],self.Player.x,self.Player.y,self.Player.widthHeight[0],self.Player.widthHeight[1])
			if enemyCollision:
				enemyCollide = self.Player.checkCollision(0, coinCollision, enemyCollision)
			else:
				coinCollide = self.Player.checkCollision(self.yellowCoin.coinValue,coinCollision, enemyCollision)
			if coinCollide:
				self.yellowCoin.changePos()
			self.yellowCoin.createObject(self.window.gameDisplay)
			self.Enemy.createObject(self.window.gameDisplay)
			self.Player.createObject(self.window.gameDisplay)
			self.Enemy.update(self.Player.x, self.Player.y)
			#Message("Player: " + Player.name,20,30,16)
			Message("Coins: " + str(self.Player.numCoins),20,30,16,self.window.gameDisplay)
			Message("Lives: " + str(self.Player.lives),20,50,16,self.window.gameDisplay)
			pygame.display.flip()

	def unload(self):
		del self.window
		del self.Player
		self.gameLoaded = False

	def detectCollisions(self, x1, y1, w1, h1, x2, y2, w2, h2):
		if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
			return True
		elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
			return True 
		elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
			return True
		elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
			return True 
		else:
			return False

game = Game()
game.load()