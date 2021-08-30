# Initializing pygame + some important variables 

import pygame
from random import randint

pygame.init()

score = 0
total = 0

myfont = pygame.font.SysFont('monospace', 50)

# Making dictionaries with settings for everything.

display = {
    "width": 800,
    "height": 600
}

paddle = {
    "width": 200,
    "height": 20,
    "x": 300,
    "y": 400,
    "velocity": 50
}

ball = {
    "radius": 15,
    "y": 30,
    "x": randint(0, display["width"]),
    "velocity": 20
}

# Launching the window, setting it to the dimensions of the `display` dictionary.

win = pygame.display.set_mode((display["width"], display["height"]))

# The Main game loop

while True:
    pygame.time.delay(100)
    win.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle["x"] -= paddle["velocity"]

    if keys[pygame.K_RIGHT]:
        paddle["x"] += paddle["velocity"]

    if ball["y"] + ball["radius"] >= paddle["y"]:
        if ball["x"] > paddle["x"] and ball["x"] < paddle["x"] + paddle["width"]:
            score += 1
        total += 1
        ball["y"] = ball["radius"]
        ball["x"] = randint(0, display["width"])


    ball["y"] += ball["velocity"]

    pygame.draw.circle(win, (0, 0, 255), (ball["x"], ball["y"]), ball["radius"])
    pygame.draw.rect(win, (255, 0, 0), (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))
    
    textsurface = myfont.render("score: {0}/{1}".format(score, total), False, (0, 0, 0))
    win.blit(textsurface, (10, 10))
    
    pygame.display.update()

pygame.quit()