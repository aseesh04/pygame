import pygame
import random
import math
from pygame import mixture
pygame.init()

screen = pygame.display.set_mode((800, 600))
run = True
pygame.display.set_caption("Space Game")
# icon = pygame.load('')
# pygame.display.set_icon(icon)



score_value= 0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10





game_font=pygame.font.Font('freesansbold.ttf',100)




def show(x,y):
    score=font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over():
    game=game_font.render("GAME OVER",True,(255,255,255))
    screen.blit(game,(100,200))

player_image = pygame.image.load('spaceship (1).png')
player_x = 400
player_y = 480
player_x_move = 0

def player(x, y):
    screen.blit(player_image, (x, y))

alien_image=[]
alien_x = []
alien_y = []
alien_x_move = []
alien_y_move = []
for i in range(10):
    alien_image.append(pygame.image.load('alien.png'))
    alien_x.append(random.randint(0, 735))
    alien_y.append(random.randint(25, 150))
    alien_x_move.append(3)
    alien_y_move.append(40)


def alien(x, y,i):
    screen.blit(alien_image[i], (x, y))


bullet_image = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_y_move = 10
bullet_state = "ready"


def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 21, y + 10))


# def bullet(x,y):
def distance(x2, y2, x1, y1):
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return d

background_image = pygame.image.load('background(1).png')
# def background():

while run:
    screen.fill((0, 0, 0))

    screen.blit(background_image, (0, 0))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                player_x_move = -2
                # alien_x_move = 0.1
            if i.key == pygame.K_RIGHT:
                player_x_move = 2
                # alien_x_move = -0.1
            if i.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_x = player_x
                    fire(bullet_x, bullet_y)

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                player_x_move = 0
                # alien_x_move=0
    player_x += player_x_move
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    # bullet_y+=bullet_y_move
    # bullet(player_x+21, bullet_y)
    player(player_x, player_y)
    for i in range(10):
        if alien_y[i]>440:
            for j in range(10):
                alien_y[j]=2000
            game_over()
            break
        if alien_x[i] <= 0:
            alien_x_move[i] = 3
            alien_y[i] += alien_y_move[i]
        elif alien_x[i] >= 736:
            alien_x_move[i] = -3
            alien_y[i] += alien_y_move[i]
        alien_x[i] += alien_x_move[i]
        d = distance(alien_x[i], alien_y[i], bullet_x, bullet_y)
        if d < 27:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 10
            alien_x[i] = random.randint(0, 735)
            alien_y[i] = random.randint(25, 150)
        alien(alien_x[i], alien_y[i],i)
    # alien_x_move=10
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state is 'fire':
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_move
    # if bullet_y==alien_y:
    #   alien_y=1000

    show(textx,texty)
    # background()
    pygame.display.update()
