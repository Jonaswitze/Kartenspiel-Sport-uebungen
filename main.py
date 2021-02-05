import pygame
from settings import StaticValues

def run_game():
    pygame.init()

    #   Properties of the screen are set

    screen = pygame.display.set_mode((StaticValues.W, StaticValues.H))
    pygame.display.set_caption("Sport")

    clock = pygame.time.Clock()

    #   Main loop
    while True:  # While game is running:
        clock.tick(StaticValues.FPS)


run_game()  # Main function is called
