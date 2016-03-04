import pygame

class Button():
	def __init__(self,msg,x,y,w,h,ic,ac,action = None,price = None,amount = None,multiplier = None):
		self.msg = msg
		self.x = x
		self.y = y
		self.width = w
		self.height = h
		self.ic = ic
		self.ac = ac
		self.action = action
		self.hovering = False
		self.price = price
		self.amount = amount
		self.multiplier = multiplier
	
	def text_objects(self,text,font):
		textSurface = font.render(text,True,(0,0,0))
		return textSurface, textSurface.get_rect()
	
	def update(self,display):
		mouse = pygame.mouse.get_pos()
		if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
			pygame.draw.rect(display, self.ac,(self.x,self.y,self.width,self.height))
			self.hovering = True
		else:
			pygame.draw.rect(display, self.ic,(self.x,self.y,self.width,self.height))
			self.hovering = False
			
		smallText = pygame.font.Font("freesansbold.ttf",20)
		textSurf, textRect = self.text_objects(self.msg,smallText)
		textRect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
		display.blit(textSurf,textRect)