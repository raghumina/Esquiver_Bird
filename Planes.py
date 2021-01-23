# Plane game inspired form falppy bird
# The game is same as flappy bird, with slight changes.


import random  # to generate random numbers/ creating random names in games
import sys
import pygame
from pygame.locals import *

# Global variable for games
FPS = 32  # FRAMES PER SECOND  FOR IMAGE REINDERSCREEN
SCREENWIDTH = 1080
SCREENHEIGHT = 720

pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {

}
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
    messagey = int(SCREENHEIGHT * 0.13['PLAYER'].get_height()) / 2

    basex = 0


if __name__ == "__main__":
    # This is the main function from where the game will start
    pygame.init()  # initialize pygame modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Esquiver_Plane ")
    GAME_SPRITES["numbers"] = (pygame.image.load("0.png").convert_alpha(),
                               pygame.image.load("1.png").convert_alpha(),
                               pygame.image.load("2.png").convert_alpha(),
                               pygame.image.load("3.png").convert_alpha(),
                               pygame.image.load("4.png").convert_alpha(),
                               pygame.image.load("5.png").convert_alpha(),
                               pygame.image.load("6.png").convert_alpha(),
                               pygame.image.load("7.png").convert_alpha(),
                               pygame.image.load("8.png").convert_alpha(),
                               pygame.image.load("9.png").convert_alpha()
                               )
GAME_SPRITES['message'] = pygame.image.load("message.png").convert_alpha()
GAME_SPRITES['base'] = pygame.image.load("base.png").convert_alpha()
GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                        pygame.image.load(PIPE).convert_alpha())
# Code for Game Sounds
#
GAME_SOUNDS['die'] = pygame.mixer.Sound('die.wav')
GAME_SOUNDS['hit'] = pygame.mixer.Sound('hit.wav')
GAME_SOUNDS['point'] = pygame.mixer.Sound('point.wav')
GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('swoosh.wav')
GAME_SOUNDS['wing'] = pygame.mixer.Sound('wing.wav')

GAME_SPRITES['Background'] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['PLAYER'] = pygame.image.load(PLAYER).convert_alpha()

while True:
    welcomeScreen()  # this will show game message until player clicks button
    mainGame()  # this is main game function
