import pygame
from .constants import WHITE
from project.graphics import *
board = pygame.image.load('Untitled-1_0012_board.png')
class Board(): 
    def __init__(self):
        self.board = []
        self.selected_piece = None
    def draw_cubes(self, win):
        win.blit(board, 1920, 1080)

        