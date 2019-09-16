import pygame
from pygame.locals import *
from sys import exit
from Enums import PieceColor
from SquareClickDetection import coordinatestosquareindex
from BoardSetup import setupboard, boarddraw
from MovementLogic import movelist, makemove, check, checkmate

def rungame():
    pygame.init()
    SCREENWIDTH = 640
    SCREENLENGTH = 640
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENLENGTH))
    pygame.display.flip()
    board = []
    setupboard(board)
    boarddraw(screen, board)
    winner = False
    turn = PieceColor.WHITE
    select = False  # If the player currently wants to move a piece
    selected = -1  # If the player does want to move the piece, the index that the piece is located
    while not winner:
        x,y = pygame.mouse.get_pos()
        index = coordinatestosquareindex(x,y)
        if check(board, turn):
            if checkmate(board,turn):
                if turn == PieceColor.WHITE:
                    print("Black wins!")
                else:
                    print("White wins!")
                break
        if not select:
            if pygame.event.get(MOUSEBUTTONDOWN):
                move = coordinatestosquareindex(x, y)
                print(movelist(move,board))
                if turn == board[move].boardpiece.color and len(movelist(move,board)) > 0:
                    select = True
                    selected = move
                    print("selected")
        if select:
            if pygame.event.peek(MOUSEBUTTONDOWN) and not index in movelist(selected,board) and (board[index].boardpiece.color!=board[selected].boardpiece.color or index == selected):
                print("unselected")
                select = False
                selected = -1
            elif pygame.event.peek(MOUSEBUTTONDOWN) and board[index].boardpiece.color==board[move].boardpiece.color:
                print("changed selected")
                selected = index
            elif pygame.event.peek(MOUSEBUTTONDOWN) and index in movelist(move,board):
                print("intendedmove!")
                intendedmove = coordinatestosquareindex(x,y)
                turn = makemove(selected,intendedmove, turn,board)
                boarddraw(screen,board)
                select = False
                selected = -1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.flip()


rungame()
