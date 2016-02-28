import pygame
import pygame._view
from pygame.locals import *
from components.Window import Window
from components.Player import Player
from components import Localizer
pygame.init()

class Game():
	def __init__(self):
		self.Player = Player("images/player.png", 20)
		self.window = Window("Coin Collector V2",
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
			self.Player.createPlayerObject(self.window.gameDisplay)
			pygame.display.flip()

	def unload(self):
		del self.window
		del self.Player
		self.gameLoaded = False

game = Game()
game.load()