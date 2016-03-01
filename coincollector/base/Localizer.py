import pygame

window_title = "Coin Collector V2"
player_img = "images/player.png"
yellowCoin_img = "images/coinyellow.png"
enemy_img = "images/enemy.png"

player_maxCoins = 20
coinValues = {
	0: 1
}

upgradeDict = {
	0: {
		"Name": "+10 Max Coins",
		"Price": 1,
		"Action": "incMaxCoins",
		"Amount": 10,
		"Multiplier": 2
	}
}


yPos = 50
number = 40
for x in upgradeDict:
	yPos += number
	upgradeDict[x]["yPos"] = yPos


dispWidth = 800
dispHeight = 600
black = (0,0,0)
white = (255,255,255)
red = (205,0,0)
green = (0,205,0)
blue = (0,0,235)
purple = (100,0,255)
cyan = (0,255,221)
bright_green = (0,255,0)
bright_red = (255,0,0)
