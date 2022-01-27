import pygame
from boardgame.constants import WIDTH, HEIGHT
from boardgame.board import Board
from graphics import *
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Impeccable Board Game")

def main():
    board = Board()
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
           if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_cubes(WIN)
        pygame.display.update()
    pygame.quit() 
main()