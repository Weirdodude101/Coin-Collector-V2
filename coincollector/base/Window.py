import pygame

class Window():
	def __init__(self, title, icon, width, height, bgColor):
		self.dispWH = (width, height)
		pygame.display.set_caption(title)
		self.gameDisplay = pygame.display.set_mode((self.dispWH[0], self.dispWH[1]))
		self.clock = pygame.time.Clock()
		self.gameIcon = pygame.display.set_icon(icon)
		self.bgColor = bgColor