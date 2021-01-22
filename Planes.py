# Plane game inspired form falppy bird


import random  # to generate random numbers/ creating random names in games
import sys
import pygame
import pygame.locals
from pygame import *

# Global variable for games
FPS = 32  # FRAMES PER SECOND  FOR IMAGE REINDERSCREEN
SCREENWIDTH = 289
SCREENHEIGHT = 511

pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {

}
GAME_SOUNDS = {}
PLAYER = "bird.png"
BACKGROUND = "background.png"
PIPE = "pipe.png"

if __name__ == "__main__":
    # This is the main function from where the game will start
    pygame.init()  # initiliaze pygame modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Esquiver_Plane ")
    GAME_SPRITES["numbers"] = (pygame.image.load("0.png").convert.alpha(),
                               pygame.image.load("1.png").convert.alpha(),
                               pygame.image.load("2.png").convert.alpha(),
                            pygame.image.load("3.png").convert.alpha(),
                               pygame.image.load("4.png").convert.alpha(),
                               pygame.image.load("5.png").convert.alpha(),
                               pygame.image.load("6.png").convert.alpha(),
                               pygame.image.load("7.png").convert.alpha(),
                               pygame.image.load("8.png").convert.alpha(),
                               pygame.image.load("9.png").convert.alpha()
                               )
    


