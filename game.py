# importing libraries
import pygame
import random

# initalizing display
pygame.init()
resolution = (1280 ,720)

#settingup tile size and varible for window
ts = 40
win = pygame.display.set_mode(resolution)

pygame.display.set_caption("Game")

#enemy moment speed controll
enemy_delay = 1

# intializing player position and direction 
px = 2
py = 2
pd = 'RIGHT'

#randomizing enemy spawn points for the first two enemies
e1x = (random.randint(5,31))
e2x = (random.randint(5,31))
e1y = (random.randint(5,17))
e2y = (random.randint(5,17))
e3x = -5
e3y = -5

# defining world tiles and player tiles
W = 1
B = 0
L = 2
D = 3
F = 4

player_Left = pygame.image.load('LEFT.png') 
player_Right = pygame.image.load('RIGHT.png')
player_Up = pygame.image.load('UP.png')
player_Down = pygame.image.load('DOWN.png')


int1 = pygame.image.load('int1.png')
int2 = pygame.image.load('int2.png')
int3 = pygame.image.load('int3.png')
inst = pygame.image.load('inst.png')

wall = pygame.image.load('wall.png')
floor = pygame.image.load('floor.png')
lava = pygame.image.load('lava.png')
door = pygame.image.load('door.png')
flower = pygame.image.load('flower.png')
enemy = pygame.image.load('enemy.png')
GREEN =pygame.image.load('green.png')
start = pygame.image.load('start.png')
game_over = pygame.image.load('game_over.png')
next_level = pygame.image.load('loading.png')
the_end = pygame.image.load('end.png')

tile ={W : wall,
         B : floor,
         L : lava,
         D : door,
         F : flower
         }

# initalizing door location and level no
level_no = 1

doorx = 0
doory = 0

#setting map tile height and width
mapheight = 18
mapwidth = 32


# initalizing lava array and game run status
lava = []
game_status = True


# displaying the intro
win.blit(int1,(0,0))
pygame.display.flip()
pygame.time.delay(9000)
win.blit(int2,(0,0))
pygame.display.flip()
pygame.time.delay(9000)
win.blit(int3,(0,0))
pygame.display.flip()
pygame.time.delay(6000)

# displaying instructions
win.blit(inst,(0,0))
pygame.display.flip()
pygame.time.delay(5000)


# loading the BGM and GAME_over sound
Game_over = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('bgm.wav')
pygame.mixer.music.play(-1)






# initalizing all 5 maps

mp1 = [[W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,L,L,B,B,B,L,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,D,W],
      [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],]


mp2 = [[W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,L,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,L,B,W],
      [W,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,D,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],]

mp3 = [[W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,L,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,L,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,L,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,L,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,L,L,L,L,B,D,W],
      [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],]

mp4 = [[W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,L,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,D,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,L,L,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],]



mp5 = [[W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,L,L,L,L,L,L,L,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,L,B,B,F,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,L,B,B,B,L,B,B,B,B,B,L,B,B,B,L,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,B,B,B,B,B,L,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,L,L,L,L,L,L,L,L,L,L,L,L,L,L,L,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,W],
      [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],]
# defining random enemy spawn function
def rand_enemy():
    global e1x
    global e2x
    global e3x
    global e1y
    global e2y
    global e3y
    
    e1x = (random.randint(5,31))
    e2x = (random.randint(5,31))
    e1y = (random.randint(5,17))
    e2y = (random.randint(5,17))
    
    
    if level_no == 5 :
        e3x = -5
        e3y = -5
    else:
        e3x = (random.randint(5,31))
        e3y = (random.randint(5,17))
        
    
# defining draw function for all elements 
def draw(mpc,px,py,pd):
    for col in range(mapwidth):
        for row in range(mapheight):
            win.blit(tile[mpc[row][col]], (col*ts, row*ts))
            
    win.blit(enemy,(e1x*ts,e1y*ts))
    win.blit(enemy,(e2x*ts,e2y*ts))
    win.blit(GREEN,(e3x*ts,e3y*ts))
    
    if pd == 'LEFT':
        win.blit(player_Left , (px*ts,py*ts))
    if pd == 'RIGHT':
        win.blit(player_Right , (px*ts,py*ts))
    if pd == 'UP':
        win.blit(player_Up , (px*ts,py*ts))
    if pd == 'DOWN':
        win.blit(player_Down , (px*ts,py*ts))
        
    pygame.display.flip()
    
# defining lava position calculation function    
def  lava_pos_calc(mpc):
    for col in range(mapwidth):
        for row in range(mapheight):
            if mpc[row][col] == L :
                lava.append((col,row))


#  defining a method to find door in given map
def find_door(mpc):
    global doorx
    global doory
    for col in range(mapwidth):
        for row in range(mapheight):
            if mpc[row][col] == D or mpc[row][col] == F :
                doorx = col
                doory = row
    
# defining a method to move enemies towards the player
def enemy_movement():
    global e1x
    global e2x
    global e3x
    global e1y
    global e2y
    global e3y
    
    if e1x > px:
        e1x = e1x-1
    else :
        e1x = e1x+1
    
    if e1y > py:
        e1y = e1y-1
    else :
        e1y = e1y+1
    
    if e2x > px:
        e2x = e2x-1
    else :
        e2x = e2x+1
    
    if e2y > py:
        e2y = e2y-1
    else :
        e2y = e2y+1
    
    if level_no == 5:

        if e3x > px:
            e3x = e3x-1
        else :
            e3x = e3x+1
        if e3y > py:
            e3y = e3y-1
        else :
           e3y = e3y+1
    else:
        e3x = -5
        e3y = -5
# defining boundary collusion check    
def collusion_check():
    global px
    global py
    
    if px == 0:
        px =1
    if px > (mapwidth-2):
        px = mapwidth-2
    if py == 0:
        py =1
    if py > (mapheight-2):
        py = mapheight-2
# function to get key press
def keypress():
    global px
    global py
    global pd
    key =  pygame.key.get_pressed()
        
    if key[pygame.K_LEFT]:
        px = px - 1
        pd = "LEFT"
            
    if key[pygame.K_RIGHT]:
        px = px + 1
        pd = "RIGHT"   
    if key[pygame.K_UP]:
        py = py - 1
        pd = "UP"
    if key[pygame.K_DOWN]:
        py = py + 1
        pd = "DOWN"
        
#function to find if the player has collided with the enemy or lava
def enemy_lava_check():
    global px
    global py
    global e1x
    global e2x
    global e3x
    global e1y
    global e2y
    global e3y
    
    
    for i in range(len(lava)):
        if (px,py) == lava[i]:
            return True
    if (e1x,e1y) == (px,py):
        return True

    if (e2x,e2y) == (px,py):
        return True
    
    if (e3x,e3y) == (px,py):
        return True

# to check if the player has reached a door
def door_check():
    if doorx == px and doory == py :
        return True
    else:
        return False
# function to draw start screen    
def start_screen():
    win.blit(start,(0,0))
    pygame.display.flip()
    pygame.time.delay(200)
    pygame.event.clear()
    ev = pygame.event.wait()
        
        
# function to draw load screen
def load_screen():
    win.blit(next_level,(0,0))
    pygame.display.flip()


# function to draw game over screen
def game_over_screen():
    pygame.mixer.music.stop()
    
    Game_over.play()
    win.blit(game_over,(0,0))
    pygame.display.flip()
    pygame.time.delay(5000)
    pygame.mixer.music.play(-1)
      

# to check if the game is over or not
def game_status_check():
    if(enemy_lava_check()):
        return 'game_over'
    elif(door_check()):
        return 'next_level'
# to initaly go to the start screen

start_screen()

while game_status:
    # game clock
    pygame.time.delay(15)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        
            game_status = False
    
    
    #enemy movement restriction
    enemy_delay += 1
    # getting level no to load correct lava and door position
    if level_no == 1 :
        lava_pos_calc(mp1)
        find_door(mp1)
        
    if level_no == 2 :
        lava_pos_calc(mp2)
        find_door(mp2)
    
    if level_no == 3 :
        lava_pos_calc(mp3)
        find_door(mp3)
    
    if level_no == 4 :
        lava_pos_calc(mp4)
        find_door(mp4)
    
    if level_no == 5 :
        lava_pos_calc(mp5)
        find_door(mp5)
    
    keypress()
    
    if enemy_delay % 4 == 0:
        enemy_movement()
        enemy_delay = 1
    
    collusion_check()
    # drawing the correct level on screen
    if level_no == 1:
        draw(mp1,px,py,pd)
    
    if level_no == 2:
        draw(mp2,px,py,pd)
    
    if level_no == 3:
        draw(mp3,px,py,pd)
    
    if level_no == 4:
        draw(mp4,px,py,pd)
    
    if level_no == 5:
        draw(mp5,px,py,pd)
     # game status check   
    if (game_status_check() == 'game_over'):
        game_over_screen()
        pygame.time.delay(25)
        start_screen()
        level_no = 1
        px = 2
        py = 2
        rand_enemy()
        
    elif(game_status_check() == 'next_level' and level_no != 6 ):
        load_screen()
        level_no = level_no + 1
        px = 2
        py = 2
        rand_enemy()
        pygame.time.delay(900)
        
    if(level_no == 6 ):
        win.blit(the_end,(0,0))
        pygame.display.flip()
        pygame.time.delay(6000)
        game_status = False
     # clearing old lava spots   
    lava = []
    
        
    


pygame.quit()

