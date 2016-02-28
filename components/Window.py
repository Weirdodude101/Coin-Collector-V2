import pygame
import pygame._view
from pygame.locals import *
import os
import time

class Window():
	def __init__(self, title, icon, width, height, bgColor):
		self.dispWidth = width
		self.dispHeight = height
		pygame.display.set_caption(title)
		self.gameDisplay = pygame.display.set_mode((self.dispWidth, self.dispHeight))
		self.clock = pygame.time.Clock()
		self.gameIcon = pygame.display.set_icon(icon)
		self.bgColor = bgColor