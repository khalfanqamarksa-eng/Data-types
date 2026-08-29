import pygame
import random
import math
screen_width = 800
screen_height = 500
player_start_x= 370
player_start_y= 380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y= 40
bullet_speed_y=10
collision_distance= 27

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('Space invaders.jpg')
pygame.display.set_caption('Space Invaders')

#Player
Playerimg= pygame.image.load('Player.png')
playerX= player_start_x
playerY=player_start_y
PlayerX_change = 0

#Enemy
Enemyimg = []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range (num_of_enemies):
    Enemyimg.append(pygame.image.load('Enemy 1.png'))
    enemyX.append(random.randint(0, screen_width - 64))
    enemyY.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)

#Bullet
bulletImg = pygame.image.load('Bullet.jpg')
bulletX = 0
bulletY = player_start_y
bulletX_change= 0
bulletY_change = bullet_speed_y
bullet_state = "ready"

#score
score_value=0
font = pygame.font.Font('freesansbold.ttf', 32)
textX= 10
textY= 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score : ", str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text=over_font.render("GAME OVER", True (255,255,255))
    screen.blit(over_text, (200,250))