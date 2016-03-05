import pygame
from coincollector.base import Localizer
import time
import math
class Upgrades():
	def __init__(self, player, upgradeDict, price, multiplier, number):
		self.Player = player
		self.upgradeDict = upgradeDict
		self.price = price
		self.multiplier = multiplier
		self.number = number
		self.debounce = False
		time.sleep(0.5)

	def incMaxCoins(self, amt):
		self.Player.maxCoins += amt
		self.Player.numCoins -= self.price
		self.upgradeDict[self.number]["Price"] *= self.multiplier
		self.upgradeDict[self.number]["Price"] = math.ceil(self.upgradeDict[self.number]["Price"] * 100) / 100.0
		#self.changePrice()
		print 'Purchase completed'

	def incPlayerSpeed(self, amt):
		self.Player.maxVelX += amt
		self.Player.maxVelY += amt
		self.Player.minVelX = self.Player.maxVelX * -1
		self.Player.minVelY = self.Player.maxVelY * -1
		self.upgradeDict[self.number]["Price"] *= self.multiplier
		self.upgradeDict[self.number]["Price"] = math.ceil(self.upgradeDict[self.number]["Price"] * 100) / 100.0
		self.changePrice()


	"""def changePrice(self):
		self.upgradeDict[self.number]["Price"] *= self.multiplier
		self.upgradeDict[self.number]["Price"] = math.ceil(self.upgradeDict[self.number]["Price"] * 100) / 100.0
		self.Player.numCoins -= self.price"""