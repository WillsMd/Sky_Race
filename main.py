import pygame
import random
import math
from pygame import mixer


# Game properties
level = 1
difficulty = 1
running = True

# Set up game window
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sky Race")
icon = pygame.image.load("assets\cloud.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


backgroundImg = pygame.image.load("assets\sky1.png")

# Define fonts
font = pygame.font.Font(None, 30)


############################################# PLAYER #####################################################################3
# Player properties
player_image = pygame.image.load("assets\player_jump.png")
player_x = 195 
player_y = 300
player_speed = 5
player_points = 50 # Initial points 


def player(x, y):
    screen.blit(player_image, (player_x, player_y))


################################### OBSTACLE - ENEMY FOR SUBSTRACTING PLAYERS POINT ####################################################################
# Obstacle properties
obstacle_speeds = [3, 4, 5] # Speeds for each level
max_obstacles = [5, 7, 10] # Maximum number of obstacles for each level
obstacles = list()
obstacle_x = list()
obstacle_y = list()
obstacle_x_change = list()
obstacle_velocities = list()
num_obstacles = random.randint(1, max_obstacles[difficulty-1])
obstacle_image = pygame.image.load("assets\enemy.png")
for i in range(num_obstacles):
    obstacles.append(pygame.transform.scale(obstacle_image, (obstacle_image.get_rect().width/9, obstacle_image.get_rect().height/9))) 
    obstacle_x.append(random.randint(0, WIDTH-64))
    obstacle_y.append(random.randint(0, HEIGHT-64))
    obstacle_x_change.append(0.5)
    obstacle_velocities.append(obstacle_speeds[difficulty-1])
    
def obstacle(x, y, i):
    screen.blit(obstacles[i], (x, y) )


########################################## DIAMONDS - FOR ADDING POINTS TO PLAYER #############################################
# Diamond properties
diamond_speed = 2
max_diamonds = 4
diamond_positions_x = list()
diamond_positions_y = list()
diamond_positions_x_change = list()
#diamonds = dict()
#diamond_points = dict()

#Diamond images
diamond_image_white = pygame.image.load("assets\diamond.png") 
diamond_image_red = pygame.image.load("assets\diamondRed.png")
diamond_image_blue = pygame.image.load("assets\diamondBlue.png")
diamond_image_purple = pygame.image.load("assets\diamondPurple.png")

#Resizing the images
white_diamond = pygame.transform.scale(diamond_image_white, ((int)(diamond_image_white.get_rect().width/55), (int)(diamond_image_white.get_rect().height/55)))
red_diamond = pygame.transform.scale(diamond_image_red, ((int)(diamond_image_red.get_rect().width/55), (int)(diamond_image_red.get_rect().height/55)))
blue_diamond = pygame.transform.scale(diamond_image_blue, ((int)(diamond_image_blue.get_rect().width/55), (int)(diamond_image_blue.get_rect().height/55)))
purple_diamond = pygame.transform.scale(diamond_image_purple, ((int)(diamond_image_purple.get_rect().width/55), (int)(diamond_image_purple.get_rect().height/55)))

#Adding the diamonds to the diamonds dict

diamonds = {"1":white_diamond, "2":red_diamond, "3":blue_diamond, "4":purple_diamond}

# Points for the diamonds 

diamond_points = {"white_diamond":1, "red_diamond":4, "blue_diamond":2, "purple_diamond":3}

for i in range(len(diamonds)):
    global diamond_hint
    diamond_hint = random.randint(1, max_diamonds)
    diamond_positions_x.append(random.randint(250, 600))
    diamond_positions_y.append(random.randint(150, 500))
    diamond_positions_x_change.append(0.8)

def show_diamonds(x, y,  i):    
    screen.blit(diamonds[str(diamond_hint)], (x, y ))
 
    



######################################### DISPLAYS ON GAME WINDOW #####################################################
# Starting Screen
def start_screen():
    message = "Welcome to racing in SKY"
    font = pygame.font.Font("THEBOLDFONT.ttf", 35)
    displayed_message_one = font.render(message, True, (255, 255, 255))
    #displayed_message_two = font.render("Press any key to continue...", True, (0, 0, 255))
    screen.blit(backgroundImg, (-30, -30))
    screen.blit(displayed_message_one, (150, 250))
    #screen.blit(displayed_message_two, (150, 290))
    pygame.display.update

# Coins
coin = pygame.image.load("assets\coin.png")
coin = pygame.transform.scale(coin, ((int)(coin.get_rect().width/85), (int)(coin.get_rect().height/85)))

def show_coin(x, y):
    screen.blit(coin, (x, y))

# Player points
def show_points():
    global font
    font = pygame.font.Font("atwriter.ttf", 25)
    points = font.render("Points "+str(player_points), True, (0,0,198))
    screen.blit(points, (10, 10))

# Game over
over_font = pygame.font.Font('harry.ttf', 64)
def game_over_text():
    over_text = font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    mixer.music.load("assets\winningMusic.mp3")
    mixer.music.play(-1)


#Winning



############################################# COLISIONS MANAGEMENT ######################################################
def is_collision(point_x_one, point_x_two, point_y_one, point_y_two):
    distance = math.sqrt(math.pow((point_x_one-point_x_two), 2) + math.pow((point_y_one-point_y_two), 2))
    if distance <= 45:
        return True
    else:
        return False
   


######################################## BACKGROUND MUSICA ##############################################################
#Background music
mixer.music.load("assets\gameMusic.mp3")
mixer.music.play(-1)


############################################## GAME LOOP- Not sure if this is how they call it @pythoners😅 ##############
start = True

while running:
    while start:
        start_screen()
        pygame.display.update()
        pygame.time.wait(2000)
        start = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_vel_y = -8
            if event.key == pygame.K_DOWN:
                player_vel_y = 8
            if event.key == pygame.K_RIGHT:
                playerplayer_vel_x = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_vel_y = 0
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0


    #diamonds movements
    for i in range(len(diamonds)):
        diamond_positions_x[i] -= diamond_positions_x_change[i]
        if diamond_positions_x[i] <= 215:
            diamond_positions_x[i] = 550
        elif diamond_positions_y[i] >= 500:
            diamond_positions_y[i] = 500
        elif diamond_positions_y[i] <= 100:
            diamond_positions_y[i] = 100



    #obstacle movements
    for i in range(num_obstacles):
        obstacle_x[i] -= obstacle_x_change[i]
        if obstacle_x[i] <= 215:
            obstacle_x[i] = 550
        elif obstacle_y[i] >= 450:
            obstacle_y[i] = 430
        elif obstacle_y[i] <= 100:
            obstacle_y[i] = 100

    #Collisions inside game loop
    diamond_collision = is_collision(player_x, diamond_positions_x[i], player_y, diamond_positions_y[i])
    
    obstacle_collision = is_collision(player_x, obstacle_x[i], player_y, obstacle_y[i])

    if diamond_collision:
        collision_sound = mixer.Sound("assets/coin_drop.wav")
        collision_sound.play()
        diamond_positions_x[i] = random.randint(160, 725)
        diamond_positions_y[i] = random.randint(160, 450)
        if diamonds.keys == 1:
            player_points += 1
        elif diamonds.keys == 2:
            player_points += 4
        elif diamonds.keys == 3:
            player_points += 2
        else:
            player_points += 3    

    if obstacle_collision:
        collision_sound = mixer.Sound('assets/explosion.wav')
        collision_sound.play()
        obstacle_x[i] = random.randint(158, 735)
        obstacle_y[i] = random.randint(200, 500)
        if player_points <= 0:
            player_points = 0
            show_points()
            game_over_text()
            pygame.display.update()
            pygame.time.delay(7000)
            break
        else:
            player_points -= 3
    

    #Guiding player movement
    player_x += 5
    player_y += player_vel_y

    #player boudaries on screen
    temp_y = player_y
    if player_x >= 400:
        player_x = 195
    if player_y <= 100 or player_y >= 450:
        player_y = 300

    screen.fill((255, 255, 255))
    screen.blit(backgroundImg, (-30, -30))
    show_points()
    player(player_x, player_y)
    show_coin(130, 12)
    obstacle_x[i] -= 0.5
    obstacle(obstacle_x[i], obstacle_y[i], i)
    show_diamonds(diamond_positions_x[i], diamond_positions_y[i], i)    
    pygame.display.update()
    
    clock.tick(60)