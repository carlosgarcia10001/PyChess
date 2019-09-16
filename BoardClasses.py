from Enums import ChessPiece
from Enums import PieceColor
import pygame

class boardpiece:
    occupied = False
    piece = ChessPiece.NONE
    color = PieceColor.NONE
    image = None

class boardsquare:
    boardpiece = boardpiece()
    backgroundcolor = (0,0,0)
    backgroundrect = pygame.Rect(0,0,0,0)
