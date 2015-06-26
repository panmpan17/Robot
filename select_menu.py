import pygame, sys
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def Draw():
	global window, wordSignle, textRectObj
	window.fill(BLACK)
	wordSignle = fontObj.render('Single Mode', True, WHITE,BLACK)
	textRectObj.center = (120, 20)
	window.blit(wordSignle,textRectObj)
	wordSignle = fontObj.render('Online Mode', True, WHITE,BLACK)
	textRectObj.center = (120, 48)
	window.blit(wordSignle,textRectObj)

pygame.init()
window = pygame.display.set_mode((400,400))
pygame.display.set_caption(' Robot ')
fontObj = pygame.font.Font('freesansbold.ttf', 32)
wordSignle = fontObj.render('Single Player', True, WHITE,BLACK)
textRectObj = wordSignle.get_rect()
textRectObj.center = (120, 14)
def Select():
	global window, wordSignle, textRectObj
	window = pygame.display.set_mode((400,400))
	while True:
		Draw()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP:
				x,y = event.pos
				if x >= 0 and x <= 400:
					if y >= 0 and y <= 32:
						pygame.quit()
						return "single"
					# elif y >= 33 and y <= 64:
					# 	pygame.quit()
					# 	return "online"
		pygame.display.flip()

if __name__ == "__main__":
	a = Select()
	print (a)
