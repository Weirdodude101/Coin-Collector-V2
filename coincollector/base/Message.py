import pygame
import Localizer
class Message():
	def __init__(self, text, x, y, fontSize, gameDisplay):
		self.gameDisplay = gameDisplay
		self.text = text
		self.x = x
		self.y = y
		self.fontSize = fontSize
		self.message_display()

	def text_objects(self, font):
		textSurface = font.render(self.text,True,Localizer.white)
		return textSurface, textSurface.get_rect()

	def message_display(self):
		smallText = pygame.font.Font("freesansbold.ttf",self.fontSize)
		TextSurf,TextRect = self.text_objects(smallText)
		TextRect = ((self.x),(self.y))
		self.gameDisplay.blit(TextSurf,TextRect)