from tkinter.tix import InputOnly
import pygame

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)
(width, height) = (1920, 1080)
circlecolor =  (255,   0,   0)

running = True

def main():
    global running, screen

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Very Cool Board Game")
    screen.fill(WHITE)
    pygame.display.update()

    while running:
        ev = pygame.event.get()
        for event in ev:
            drawCircle()
            pygame.display.update()

            if event.type == pygame.QUIT:
                running = False

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawCircle():
    pos=getPos()
    pygame.draw.circle(screen, circlecolor, pos, 75)


if __name__ == '__main__':
    main()