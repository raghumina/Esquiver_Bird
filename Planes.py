# Plane game inspired form falppy bird
# The game is same as flappy bird, with slight changes.


import random  # to generate random numbers/ creating random names in games
import sys
import pygame
from pygame.locals import *

# Global variable for games
FPS = 32  # FRAMES PER SECOND  FOR IMAGE REINDERSCREEN
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = "bird.png"
BACKGROUND = "background.png"
PIPE = "pipe.png"


def welcomeScreen():
    # Shows welcome screen on image
    # This for aliginig messages and player on screen
    playerx = int(SCREENWIDTH / 5)  # creating the starting position of player on screen
    palyery = int((SCREENHEIGHT - GAME_SPRITES['PLAYER'].get_height()) / 2)
    mesasgex = int((SCREENWIDTH - GAME_SPRITES['PLAYER'].get_width()) / 2)
    messagey = int((SCREENHEIGHT * 0.13))

    basex = 0
    while True:
        for event in pygame.event.get():
            # If user click on cross button close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        # If user presses space or up key start game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or K_UP ):
                return
            else:
                SCREEN.blit(GAME_SPRITES['Background'],(0,0))
                SCREEN.blit(GAME_SPRITES['PLAYER'], (playerx,palyery))
                SCREEN.blit(GAME_SPRITES['message'], (mesasgex, messagey))
                lpha(),
