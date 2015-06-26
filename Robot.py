import pygame, sys
from pygame.locals import *

def check_xy(number):
	return 200 - (number * 10)

def readlevel(level):
	f = open("level/level_"+level+".txt")
	r = f.read()
	f.close()
	s1 = r.split("\n")
	start_y = check_xy(len(s1))
	a = {"block":[],"star":[],"box":[]}
	n = 0
	for i in s1:
		a[n] = {"y":start_y}
		n2 = 0
		start_x = check_xy(len(i))
		for e in i:
			a[n][n2] = (e,start_x)
			if e == "h":
				a["cn"] = [start_x,start_y]
				a["block"].append([start_x,start_y])
			elif e == "d":
				a["d"] = [start_x,start_y]
				a["block"].append([start_x,start_y])
			elif e == "0":
				a["block"].append([start_x,start_y])
			elif e == "b":
				a["box"].append([start_x,start_y])
			elif e == "p":
				a["block"].append([start_x,start_y])
				a["star"].append([start_x,start_y])
			n2 += 1
			start_x += 20
		n += 1
		start_y += 20
	a["c"] = [190-a["cn"][0], 190-a["cn"][1],]
	return a

def cahngelevel(level):
	a = readlevel(level)
	return a

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

menu = "main"
direction = "r" # r l u d
bite = "" # "" "_c"
scene = None
hold = []# ["star",[scene["star"]]

pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption(' Robot ')
fontObj = pygame.font.Font(None, 32)
wordSignle = fontObj.render('Single Player', True, GREEN, BLUE)
textRectObj = wordSignle.get_rect()
textRectObj.center = (0, 16)

image = {
"character_r":pygame.image.load("source/robot_r.png"),
"character_r_c":pygame.image.load("source/robot_r_c.png"),
"character_l":pygame.image.load("source/robot_l.png"),
"character_l_c":pygame.image.load("source/robot_l_c.png"),
"character_u":pygame.image.load("source/robot_u.png"),
"character_u_c":pygame.image.load("source/robot_u_c.png"),
"character_d":pygame.image.load("source/robot_d.png"),
"character_d_c":pygame.image.load("source/robot_d_c.png"),
"door":pygame.image.load("source/door.png"),
"box":pygame.image.load("source/box.png"),
"stone":pygame.image.load("source/stone.png"),
"home":pygame.image.load("source/home.png"),
"star":pygame.image.load("source/star.png"),
"empty_star":pygame.image.load("source/star_e.png"),
}

while True: # main game loop
	window.fill(BLACK)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONUP and menu == "main":
			menu = "1"
			scene = cahngelevel(menu)
		elif event.type == KEYDOWN and menu != "main" and menu != "end":
			if event.key == K_UP:#################################################
				if direction == "u":#scene["cn"][0],scene["cn"][1]
					new = [scene["cn"][0],scene["cn"][1]-20]
					if new in scene["block"]:
						if hold == []:
							scene["cn"] = new
							scene["c"][1] += 20
						else:# push
							if [hold[1][0],hold[1][1]] in scene["star"]:# push star
								new1 = [hold[1][0],hold[1][1]-20]
								if new1 in scene["block"]:
									scene["cn"] = new
									scene["c"][1] += 20
									index = scene["star"].index(hold[1])
									scene["star"][index][1] -= 20
					elif hold != []:
						if [hold[1][0],hold[1][1]] in scene["box"]:# push box
							new1 = [hold[1][0],hold[1][1]-20]
							if new1 in scene["block"]:
								scene["cn"] = new
								scene["c"][1] += 20
								scene["block"].append([]+hold[1])
								index = scene["box"].index(hold[1])
								scene["box"][index][1] -= 20
								scene["block"].remove(hold[1])
				else:# pull
					if hold != []:
						if [hold[1][0],hold[1][1]] in scene["star"] and hold[0] == "star":# pull star
							new = [scene["cn"][0],scene["cn"][1]-20]
							if new in scene["block"] and [hold[1][0],hold[1][1]-20] in scene["block"]:
								scene["cn"] = new
								scene["c"][1] += 20
								index = scene["star"].index(hold[1])
								scene["star"][index][1] -= 20
						elif [hold[1][0],hold[1][1]] in scene["box"] and hold[0] == "box":# pull box
							new = [scene["cn"][0],scene["cn"][1]-20]
							if new in scene["block"] and [hold[1][0],hold[1][1]-20] in scene["block"]:
								scene["cn"] = new
								scene["c"][1] += 20
								scene["block"].append([]+hold[1])
								index = scene["box"].index(hold[1])
								scene["box"][index][1] -= 20
								scene["block"].remove(hold[1])
					else:
						direction = "u"
			elif event.key == K_DOWN:#################################################
				if direction == "d":
					new = [scene["cn"][0],scene["cn"][1]+20]
					if new in scene["block"]:
						if hold == []:
							scene["cn"] = new
							scene["c"][1] -= 20
						else:# push
							if [hold[1][0],hold[1][1]] in scene["star"]:# push star
								new1 = [hold[1][0],hold[1][1]+20]
								if new1 in scene["block"]:
									scene["cn"] = new
									scene["c"][1] -= 20
									index = scene["star"].index(hold[1])
									scene["star"][index][1] += 20
					elif hold != []:
						if [hold[1][0],hold[1][1]] in scene["box"]:# push box
							new1 = [hold[1][0],hold[1][1]+20]
							if new1 in scene["block"]:
								scene["cn"] = new
								scene["c"][1] -= 20
								scene["block"].append([]+hold[1])
								index = scene["box"].index(hold[1])
								scene["box"][index][1] += 20
								scene["block"].remove(hold[1])
				else:# pull
					if hold != []:
						if [hold[1][0],hold[1][1]] in scene["star"] and hold[0] == "star":# pull star
							new = [scene["cn"][0],scene["cn"][1]+20]
							if new in scene["block"] and [hold[1][0] ,hold[1][1]+20] in scene["block"]:
								scene["cn"] = new
								scene["c"][1] -= 20
								index = scene["star"].index(hold[1])
								scene["star"][index][1] += 20
						elif [hold[1][0],hold[1][1]] in scene["box"] and hold[0] == "box":# pull box
							new = [scene["cn"][0],scene["cn"][1]+20]
							if new in scene["block"] and [hold[1][0] ,hold[1][1]+20] in scene["block"]:
								scene["cn"] = new
								scene["c"][1] -= 20
								scene["block"].append([]+hold[1])
								index = scene["box"].index(hold[1])
								scene["box"][index][1] += 20
								scene["block"].remove(hold[1])
					else:
						direction = "d"
			elif event.key == K_RIGHT:#################################################
				if direction == "r":
					new = [scene["cn"][0]+20,scene["cn"][1]]
					if new in scene["block"]:
						if hold == []:
							scene["cn"] = new
							scene["c"][0] -= 20
						else:# push
							if [hold[1][0],hold[1][1]] in scene["star"]:# push star
								new1 = [hold[1][0]+20,hold[1][1]]
								if new1 in scene["block"]:
									scene["cn"] = new
									scene["c"][0] -= 20
									index = scene["star"].index(hold[1])
									scene["star"][index][0] += 20
					elif hold != []:
						if [hold[1][0],hold[1][1]] in scene["box"]:# push box
							new1 = [hold[1][0]+20,hold[1][1]]
							if new1 in scene["block"]:
								scene["cn"] = new
								scene["c"][0] -= 20
								scene["block"].append([]+hold[1])
								index = scene["box"].index(hold[1])
								scene["box"][index][0] += 20
								scene["block"].remove(hold[1])
				else:# pull
					if hold != []:
						if [hold[1][0],hold[1][1]] in scene["star"] and hold[0] == "star":# pull star
							new = [scene["cn"][0]+20,scene["cn"][1]]
							if new in scene["block"] and [hold[1][0]+20 ,hold[1][1]] in scene["block"]:
								scene["cn"] = new
								scene["c"][0] -= 20
								index = scene["star"].index(hold[1])
								scene["star"][index][0] += 20
						elif [hold[1][0],hold[1][1]] in scene["box"] and hold[0] == "box":# pull box
							new = [scene["cn"][0]+20,scene["cn"][1]]
							if new in scene["block"] and [hold[1][0]+20 ,hold[1][1]] in scene["block"]:
								scene["cn"] = new
								scene["c"][0] -= 20
								scene["block"].append([]+hold[1])
								index = scene["box"].index(hold[1])
								scene["box"][index][0] += 20
								scene["block"].remove(hold[1])
					else:
						direction = "r"
			elif event.key == K_LEFT:#################################################
				if direction == "l":
					new = [scene["cn"][0]-20,scene["cn"][1]]
					if new in scene["block"]:
						if hold == []:
							scene["cn"] = new
							scene["c"][0] += 20
						else:#push
							if [hold[1][0],hold[1][1]] in scene["star"]:# push star
								new1 = [hold[1][0]-20,hold[1][1]]
								if new1 in scene["block"]:
									scene["cn"] = new
									scene["c"][0] += 20
									index = scene["star"].index(hold[1])
									scene["star"][index][0] -= 20
					elif hold != []:
						if [hold[1][0],hold[1][1]] in scene["box"]:# push box
							new1 = [hold[1][0]-20,hold[1][1]]
							if new1 in scene["block"]:
								scene["cn"] = new
								scene["c"][0] += 20
								scene["block"].append([]+hold[1])
								index = scene["box"].index(hold[1])
								scene["box"][index][0] -= 20
								scene["block"].remove(hold[1])
				else:# pull
					if hold != []:
						if [hold[1][0],hold[1][1]] in scene["star"] and hold[0] == "star":# pull star
							new = [scene["cn"][0]-20,scene["cn"][1]]
							if new in scene["block"] and [hold[1][0]-20 ,hold[1][1]] in scene["block"]:
								scene["cn"] = new
								scene["c"][0] += 20
								index = scene["star"].index(hold[1])
								scene["star"][index][0] -= 20
						elif [hold[1][0],hold[1][1]] in scene["box"] and hold[0] == "box":# pull box
							new = [scene["cn"][0]-20,scene["cn"][1]]
							if new in scene["block"] and [hold[1][0]-20 ,hold[1][1]] in scene["block"]:
								scene["cn"] = new
								scene["c"][0] += 20
								scene["block"].append([]+hold[1])
								index = scene["box"].index(hold[1])
								scene["box"][index][0] -= 20
								scene["block"].remove(hold[1])
					else:
						direction = "l"
			elif event.key == K_SPACE:#################################################
				if bite == "":
					if direction == "d":
						if ([scene["cn"][0],scene["cn"][1]+20] in scene["star"] or 
								[scene["cn"][0],scene["cn"][1]+20] in scene["box"]):
							bite = "_c"
							try:
								index = scene["star"].index([scene["cn"][0],scene["cn"][1]+20])
								hold = ["star",scene["star"][index]]
							except:
								index = scene["box"].index([scene["cn"][0],scene["cn"][1]+20])
								hold = ["box",scene["box"][index]]
					if direction == "u":
						if ([scene["cn"][0],scene["cn"][1]-20] in scene["star"] or
								[scene["cn"][0],scene["cn"][1]-20] in scene["box"]):
							bite = "_c"
							try:
								index = scene["star"].index([scene["cn"][0],scene["cn"][1]-20])
								hold = ["star",scene["star"][index]]
							except:
								index = scene["box"].index([scene["cn"][0],scene["cn"][1]-20])
								hold = ["box",scene["box"][index]]
					if direction == "r":
						if ([scene["cn"][0]+20,scene["cn"][1]] in scene["star"] or
								[scene["cn"][0]+20,scene["cn"][1]] in scene["box"]):
							bite = "_c"
							try:
								index = scene["star"].index([scene["cn"][0]+20,scene["cn"][1]])
								hold = ["star",scene["star"][index]]
							except:
								index = scene["box"].index([scene["cn"][0]+20,scene["cn"][1]])
								hold = ["box",scene["box"][index]]
					if direction == "l":
						if ([scene["cn"][0]-20,scene["cn"][1]] in scene["star"] or
								[scene["cn"][0]-20,scene["cn"][1]] in scene["box"]):
							bite = "_c"
							try:
								index = scene["star"].index([scene["cn"][0]-20,scene["cn"][1]])
								hold = ["star",scene["star"][index]]
							except:
								index = scene["box"].index([scene["cn"][0]-20,scene["cn"][1]])
								hold = ["box",scene["box"][index]]
				else:
					bite = ""
					if hold:
						hold = []
	if menu == "main":
		textRectObj.center = (150, 16)
		wordSignle = fontObj.render('Play', True, WHITE, BLACK)
		window.blit(wordSignle,textRectObj)
	elif menu == "end":
		textRectObj.center = (200, 150)
		wordSignle = fontObj.render('Congratulations !', True, WHITE, BLACK)
		window.blit(wordSignle,textRectObj)
		textRectObj.center = (150, 200)
		wordSignle = fontObj.render('You Finish The Game', True, WHITE, BLACK)
		window.blit(wordSignle,textRectObj)
		textRectObj.center = (200, 250)
		wordSignle = fontObj.render('More Detail in', True, WHITE, BLACK)
		window.blit(wordSignle,textRectObj)

		f = pygame.font.Font('freesansbold.ttf', 20)
		wss = f.render('http://mime-studio.appspot.com', True, BLUE,BLACK)
		tr = wss.get_rect()
		tr.center = (200,300)
		window.blit(wss,tr)
	else:
		if scene["cn"] == scene["d"] and len(scene["star"]) == 0:
			menu = str(int(menu) + 1)
			try:
				scene = cahngelevel(menu)
				# print (scene)
			except:
				menu = "end"
		else:
			c = "character_" + direction + bite
			window.blit(image[c],(190,190))
			for i in scene:
				if type(i) == type(1):
					for e in scene[i]:
						if e != "y":
							if scene[i][e][0] == "s":
								window.blit(image["stone"],(scene[i][e][1]+scene["c"][0],scene[i]["y"]+scene["c"][1]))
							if scene[i][e][0] == "d":
								window.blit(image["door"],(scene[i][e][1]+scene["c"][0],scene[i]["y"]+scene["c"][1]))
							if scene[i][e][0] == "h":
								window.blit(image["home"],(scene[i][e][1]+scene["c"][0],scene[i]["y"]+scene["c"][1]))
			for i in scene["star"]:
				window.blit(image["star"],(i[0]+scene["c"][0],i[1]+scene["c"][1]))
				if i == scene["d"]:
					scene["star"].remove(i)
					bite = ""
					hold = []
			for i in scene["box"]:
				window.blit(image["box"],(i[0]+scene["c"][0],i[1]+scene["c"][1]))
	pygame.display.flip()