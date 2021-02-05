import pygame
from settings import StaticValues, Specs
import functions

def run_game():
    pygame.init()

    #   Properties of the screen are set

    screen = pygame.display.set_mode((StaticValues.W, StaticValues.H))
    pygame.display.set_caption("Sport")

    clock = pygame.time.Clock()

    Specs.aktiv = True

    #   Main loop
    while Specs.aktiv:  # While game is running:
        clock.tick(StaticValues.FPS)
        functions.checkEvents()


run_game()  # Main function is called
