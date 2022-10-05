import pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

import sys
from settings import *
from level import Level
import random
# import powerup
from powerup import *


POWERUP_SIZE = (50, 50)
POWERUP1_COLOR = (200, 0, 200)
POWERUP2_COLOR = (255, 255, 0)
POWERUP3_COLOR = (0, 255, 255)

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level(self.screen)
        pygame.display.set_caption("Pong")


    def run(self):
            
        start_time = pygame.time.get_ticks()
        height = Powerup.randomizeHeight()

        while True:
            # event detection
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.level.run()
           
            # ~~~~ generate powerup block ~~~~~
            time_elapsed = pygame.time.get_ticks()
            changeHeight = False

            if (time_elapsed - start_time) > 5000:
                changeHeight = True

            if changeHeight:
                start_time = pygame.time.get_ticks()
                height = Powerup.randomizeHeight()

            powerup1 = pygame.Rect((WIDTH-50)/2, height, 50, 50)
            pygame.draw.rect(self.screen, POWERUP3_COLOR, powerup1)
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()