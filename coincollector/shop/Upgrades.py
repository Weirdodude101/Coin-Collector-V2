import pygame
from coincollector.base import Localizer

class Upgrades():
	def __init__(self, player, upgradeDict, price, multiplier, number):
		self.Player = player
		self.upgradeDict = upgradeDict
		self.price = price
		self.multiplier = multiplier
		self.number = number

	def incMaxCoins(self, amt):
		self.Player.maxCoins += amt
		self.Player.numCoins -= self.price
		self.upgradeDict[self.number]["Price"] *= self.multiplier
		print 'Purchase completed'