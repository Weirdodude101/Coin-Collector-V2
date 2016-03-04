import pygame
from pygame.locals import *
from coincollector.base import Localizer
from coincollector.base.Message import Message
from coincollector.base.Button import Button
from Upgrades import Upgrades

pygame.init()
class Shop():
	def __init__(self, window, player):
		self.window = window
		self.Player = player
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
						if not self.Player.numCoins >= self.Player.maxCoins:
							self.storeLoaded = False

			self.window.gameDisplay.fill(Localizer.blue)
			Message("Max Coins: " + str(self.Player.maxCoins),20,30,16,self.window.gameDisplay)
			Message("Welcome to the shop!", Localizer.dispWidth - 550,30,24,self.window.gameDisplay)
			Message("You currently have {0} coins.".format(self.Player.numCoins), Localizer.dispWidth - 535,60,16,self.window.gameDisplay)
			self.buttonDict = {}
			self.actionDict = {}
			for upgrade in self.upgradeDict:
				name = self.upgradeDict[upgrade]["Name"] + " - "
				price = self.upgradeDict[upgrade]["Price"]
				yPos = self.upgradeDict[upgrade]["yPos"]
				action = self.upgradeDict[upgrade]["Action"]
				amount = self.upgradeDict[upgrade]["Amount"]
				multiplier = self.upgradeDict[upgrade]["Multiplier"]
				if not price == 1:
					namePrice = "+" + str(amount) + name + str(price) + " Coins"
				else:
					namePrice = "+" + str(amount) + name + str(price) + " Coin"
				self.button = Button(namePrice, Localizer.dispWidth - 570, yPos, 300, 35, Localizer.green, Localizer.bright_green, action, price, amount, multiplier)
				self.buttonDict[upgrade] = {"Button": self.button}
				self.actionDict[upgrade] = action
				self.button.update(self.window.gameDisplay)
				if self.Player.numCoins >= self.Player.maxCoins:
					Message("Please purchase an item to go back", Localizer.dispWidth - 555,570,16,self.window.gameDisplay)
				else:
					Message("Press 's' to go back to game", Localizer.dispWidth - 535,570,16,self.window.gameDisplay)
			self.buttonCheck()
			pygame.display.flip()

	def buttonCheck(self):
		click = pygame.mouse.get_pressed()
		for button in self.buttonDict:
			hovering = self.buttonDict[button]["Button"].hovering
			action = self.buttonDict[button]["Button"].action
			price = self.buttonDict[button]["Button"].price
			multiplier = self.buttonDict[button]["Button"].multiplier
			amount = self.buttonDict[button]["Button"].amount
		if click[0] == 1:
			if hovering == True:
				if action == self.actionDict[0]:
					print 'Incoming purchase...'
					isValid = self.checkPrice(price)
					if isValid:
						Upgrades(self.Player, self.upgradeDict, price, multiplier, button).incMaxCoins(amount)
					else:
						print 'Invalid Purchase'

	def checkPrice(self, price):
		if price > self.Player.numCoins:
			return False
		elif price <= self.Player.numCoins:
			return True
		else:
			return False





