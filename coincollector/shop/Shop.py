import pygame
from pygame.locals import *
from coincollector.base import Localizer
from coincollector.base.Message import Message
from coincollector.base.Button import Button

pygame.init()
class Shop():
	def __init__(self, window, numCoins):
		self.window = window
		self.numCoins = numCoins
		self.upgradeDict = Localizer.upgradeDict

	def load(self):
		self.window.clock.tick(30)
		self.storeLoaded = True
		while self.storeLoaded:
			events = pygame.event.get()
			for event in events:
				if event.type == QUIT:
					self.storeLoaded = False
					quit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_s:
						self.storeLoaded = False

			self.window.gameDisplay.fill(Localizer.blue)
			Message("Welcome to the shop!", Localizer.dispWidth - 550,30,24,self.window.gameDisplay)
			Message("You currently have {0} coins.".format(self.numCoins), Localizer.dispWidth - 535,60,16,self.window.gameDisplay)
			for upgrade in self.upgradeDict:
				name = self.upgradeDict[upgrade]["Name"]
				price = self.upgradeDict[upgrade]["Price"]
				yPos = self.upgradeDict[upgrade]["yPos"]
				if not price == 1:
					namePrice = name + str(price) + " Coins"
				else:
					namePrice = name + str(price) + " Coin"
				self.button = Button(namePrice, Localizer.dispWidth - 570, yPos, 300, 37.5, Localizer.green, Localizer.bright_green, "test", price)
				self.button.update(self.window.gameDisplay)
			Message("Press 's' to go back to game", Localizer.dispWidth - 535,570,16,self.window.gameDisplay)
			pygame.display.flip()