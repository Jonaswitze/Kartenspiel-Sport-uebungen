import pygame
from settings import StaticValues, Specs

#   Check any event on keyboard
def checkEvents(character):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):       #   Quit viá Escape
            Specs.aktiv = False  #   Quit
            quit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, character)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, character)

#   Check any event on the keyboard related to the movement (KeyDown)

def checkKeyDownEvents(event, character):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            character.newDir = 3
        elif event.key == pygame.K_RIGHT:
            character.newDir = 1
        elif event.key == pygame.K_DOWN:
            character.newDir = 2
        elif event.key == pygame.K_UP:
            character.newDir = 0

        #   Check any event on the keyboard related to the movement (KeyUp)

def checkKeyUpEvents(event, character):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            character.movingLeft = False
        elif event.key == pygame.K_RIGHT:
            character.movingRight = False
        elif event.key == pygame.K_DOWN:
            character.movingDown = False
        elif event.key == pygame.K_UP:
            character.movingUp = False
