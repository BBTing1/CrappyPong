import pygame
import random

pygame.init()

pygame.display.set_caption("literally just pong") # Title
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
timer = 0

counter = True

WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 50, False, False)

ScoreI1 = 0
ScoreStr1 = str(ScoreI1)

ScoreI2 = 0
ScoreStr2 = str(ScoreI2)

plyr1Y = 250
plyr2Y = 250

ballX = 400
ballY = 300
ballVel = [0, 0]
Randx = 0
Randy = 0

speed = 5

running = True
while running == True:
    clock.tick_busy_loop(60)
    pygame.display.flip()
    keys = pygame.key.get_pressed()

    ScoreStr1 = str(ScoreI1)
    ScoreStr2 = str(ScoreI2)
    ScoreText1 = font.render(ScoreStr1, False, (WHITE))
    ScoreText2 = font.render(ScoreStr2, False, (WHITE))

    # Prevents the players from leaving an afterimage
    screen.fill((0, 0, 0))
    screen.blit(ScoreText1, (350, 50))
    screen.blit(ScoreText2, (450, 50))

    plyr1 = pygame.draw.rect(screen, (WHITE), (50, plyr1Y, 10, 100))
    plyr2 = pygame.draw.rect(screen, (WHITE), (740, plyr2Y, 10, 100))
    ball = pygame.draw.rect(screen, (WHITE), (ballX, ballY, 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    def centerBall():
        global ballX
        global ballY
        global timer

        ballX = 400
        ballY = 300


    if timer == 60:
        centerBall()
        timer = 0

    def bounce(start):
        global counter
        global ballVel
        global timer
        thing = [-2, 2]

        if start and (counter):
            ballVel = [random.choice(thing), random.choice(thing)]
            counter = False

        if counter:
            ballVel = [random.choice(thing), random.choice(thing)]
            counter = False
            timer += 1

    ballX += ballVel[0]
    ballY += ballVel[1]


    if keys[pygame.K_w]:
        plyr1Y -= speed
        bounce(True)

    if keys[pygame.K_s]:
        plyr1Y += speed
        bounce(True)

    if keys[pygame.K_UP]:
        plyr2Y -= speed
        bounce(True)

    if keys[pygame.K_DOWN]:
        plyr2Y += speed
        bounce(True)

    # Prevents the players and balls from moving off screen
    if plyr1Y <= 0:
        plyr1Y += speed
    if plyr1Y >= 500:
        plyr1Y -= speed
    if plyr2Y <= 0:
        plyr2Y += speed
    if plyr2Y >= 500:
        plyr2Y -= speed

    if ballY >= 600:
        bounce(False)
        counter = True

    if ballY <= 0:
        bounce(False)
        counter = True

        # Update Score
    if ballX >= 800:
        ScoreI1 += 1
        centerBall()
        counter = True
    if ballX <= 0:
        centerBall()
        counter = True

    if ball.colliderect(plyr1):
        bounce(False)
        counter = True

    if ball.colliderect(plyr2):
        bounce(False)
        counter = True
