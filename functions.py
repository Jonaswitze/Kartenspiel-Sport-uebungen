import pygame
from settings import StaticValues, Specs

#   Check any event on keyboard
def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):       #   Quit viá Escape
            Specs.aktiv = False  #   Quit
            quit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event)

#   Check any event on the keyboard related to the movement (KeyDown)

def checkKeyDownEvents(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print('')
        elif event.key == pygame.K_RIGHT:
            print('')
        elif event.key == pygame.K_DOWN:
            print('')
        elif event.key == pygame.K_UP:
            print('')

        #   Check any event on the keyboard related to the movement (KeyUp)

def checkKeyUpEvents(event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            print('')
        elif event.key == pygame.K_RIGHT:
            print('')
        elif event.key == pygame.K_DOWN:
            print('')
        elif event.key == pygame.K_UP:
            print('')
