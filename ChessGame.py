import copy
import pygame
from pygame.locals import *
from sys import exit
from Color import PieceColor as Color
from ChessPieces import ChessPiece
pygame.init()
screen = pygame.display.set_mode((640, 640))
winner = False
turn = Color.WHITE
select = False
selected = -1
black = (200,200,200)
white = (100,100,100)

wP = pygame.image.load('ChessPieces\wP.png')
wB = pygame.image.load('ChessPieces\wB.png')
wR = pygame.image.load('ChessPieces\wR.png')
wK = pygame.image.load('ChessPieces\wK.png')
wQ = pygame.image.load('ChessPieces\wQ.png')
wN = pygame.image.load('ChessPieces\wN.png')
bP = pygame.image.load('ChessPieces\\bP.png')
bB = pygame.image.load('ChessPieces\\bB.png')
bR = pygame.image.load('ChessPieces\\bR.png')
bK = pygame.image.load('ChessPieces\\bK.png')
bQ = pygame.image.load('ChessPieces\\bQ.png')
bN = pygame.image.load('ChessPieces\\bN.png')

def coordinatestosquare(x,y):
    return y//80*8+x//80
def squaretocoordinatespiecelocation(square):
    return (10+80*(square%8),10+80*(square//8))
def squaretocoordinates(square):
    return (80*(square%8),80*(square//8))

class boardpiece:
    occupied = False
    piece = ChessPiece.NONE
    color = Color.NONE
    image = None

class boardsquare:
    boardpiece = boardpiece()
    backgroundcolor = (0,0,0)
    backgroundrect = pygame.Rect(0,0,0,0)

def getbackgroundcolor(index):
    background = (125,125,125)
    bwswitch = True
    if index%2==0 and (index//8)%2==0:
        background=black
    elif index%2==0 and (index//8)%2==1:
        background= white
    elif index%2==1 and  (index//8)%2==0:
        background = white
    elif index%2==1 and (index//8)%2==1:
        background = black
    return background
board=[]
for i in range(64):
    board.append(boardsquare())
    board[i].backgroundrect=pygame.Rect(squaretocoordinates(i)[0],squaretocoordinates(i)[1],80,80)
wp = boardpiece()
wp.piece = "p"
wp.color = Color.WHITE
wp.image = wP.copy()
wr = boardpiece()
wr.piece = "r"
wr.color = Color.WHITE
wr.image = wR.copy()
wb = boardpiece()
wb.piece = "b"
wb.color = Color.WHITE
wb.image = wB.copy()
wn = boardpiece()
wn.piece = "n"
wn.color = Color.WHITE
wn.image = wN.copy()
wk = boardpiece()
wk.piece = "k"
wk.color = Color.WHITE
wk.image = wK.copy()
wq = boardpiece()
wq.piece = "q"
wq.color = Color.WHITE
wq.image = wQ.copy()
bp = boardpiece()
bp.piece = "P"
bp.color = Color.BLACK
bp.image = bP.copy()
br = boardpiece()
br.piece = "R"
br.color = Color.BLACK
br.image = bR.copy()
bb = boardpiece()
bb.piece = "B"
bb.color = Color.BLACK
bb.image = bB.copy()
bn = boardpiece()
bn.piece = "N"
bn.color = Color.BLACK
bn.image = bN.copy()
bk = boardpiece()
bk.piece = "K"
bk.color = Color.BLACK
bk.image = bK.copy()
bq = boardpiece()
bq.piece = "Q"
bq.color = Color.BLACK
bq.image = bQ.copy()
board[0].boardpiece = br
board[1].boardpiece = bn
board[2].boardpiece = bb
board[3].boardpiece = bq
board[4].boardpiece = bk
board[5].boardpiece = bb
board[6].boardpiece = bn
board[7].boardpiece = br
board[8].boardpiece = bp
board[9].boardpiece = bp
board[10].boardpiece = bp
board[11].boardpiece = bp
board[12].boardpiece = bp
board[13].boardpiece = bp
board[14].boardpiece = bp
board[15].boardpiece = bp

board[63].boardpiece = wr
board[62].boardpiece = wn
board[61].boardpiece = wb
board[60].boardpiece = wk
board[59].boardpiece = wq
board[58].boardpiece = wb
board[57].boardpiece = wn
board[56].boardpiece = wr
board[55].boardpiece = wp
board[54].boardpiece = wp
board[53].boardpiece = wp
board[52].boardpiece = wp
board[51].boardpiece = wp
board[50].boardpiece = wp
board[49].boardpiece = wp
board[48].boardpiece = wp
for i in range(64):
    board[i].backgroundcolor = getbackgroundcolor(i)
    if board[i].boardpiece.piece != " ":
        board[i].boardpiece.occupied = True


def boarddraw():
    for i in range(64):
        pygame.draw.rect(screen, board[i].backgroundcolor,board[i].backgroundrect)
        if board[i].boardpiece.image!=None:
           screen.blit(board[i].boardpiece.image,squaretocoordinatespiecelocation(i))
    pygame.display.flip()
boarddraw()
pygame.display.flip()

def alphabet(int):
    thealphabet = {
        0: "8",
        1: "7",
        2: "6",
        3: "5",
        4: "4",
        5: "3",
        6: "2",
        7: "1",
    }
    print(" " + thealphabet.get(int, ""), end="")

location = {
    "A8": 0,
    "A7": 8,
    "A6": 16,
    "A5": 24,
    "A4": 32,
    "A3": 40,
    "A2": 48,
    "A1": 56,
    "B8": 1,
    "B7": 9,
    "B6": 17,
    "B5": 25,
    "B4": 33,
    "B3": 41,
    "B2": 49,
    "B1": 57,
    "C8": 2,
    "C7": 10,
    "C6": 18,
    "C5": 26,
    "C4": 34,
    "C3": 42,
    "C2": 50,
    "C1": 58,
    "D8": 3,
    "D7": 11,
    "D6": 19,
    "D5": 27,
    "D4": 35,
    "D3": 43,
    "D2": 51,
    "D1": 59,
    "E8": 4,
    "E7": 12,
    "E6": 20,
    "E5": 28,
    "E4": 36,
    "E3": 44,
    "E2": 52,
    "E1": 60,
    "F8": 5,
    "F7": 13,
    "F6": 21,
    "F5": 29,
    "F4": 37,
    "F3": 45,
    "F2": 53,
    "F1": 61,
    "G8": 6,
    "G7": 14,
    "G6": 22,
    "G5": 30,
    "G4": 38,
    "G3": 46,
    "G2": 54,
    "G1": 62,
    "H8": 7,
    "H7": 15,
    "H6": 23,
    "H5": 31,
    "H4": 39,
    "H3": 47,
    "H2": 55,
    "H1": 63
}


def movelist(selected):  # Creates a list of validmoves. The purpose is to check check, and to apply collision (pieces blocking pieces)
    possiblemoves = []
    occupiedcheck = []  # A list of indexes that are in the path of validmoves (blocking the piece)
    for moves in range(64):  # Check all 64 squares to see if there is a validmove
        if validmove(selected, moves):
            possiblemoves.append(moves)  # If there is a valid move, add it to the list, ignoring collision
    for deletion in possiblemoves:  # Looking for impossible moves due to collision, and deleting them
        if board[deletion].boardpiece.occupied:
            occupiedcheck.append(deletion)
    if board[selected].boardpiece.piece == "r" or board[selected].boardpiece.piece == "R":
        for square in occupiedcheck:
            try:
                if square > selected and square % 8 == selected % 8:
                    i = square
                    while i % 8 == selected % 8:
                        if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                            possiblemoves.remove(i)
                        i += 8
                if square < selected and square % 8 == selected % 8:
                    i = square
                    while i % 8 == selected % 8:
                        if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                            possiblemoves.remove(i)
                        i -= 8
                if square > selected and square // 8 == selected // 8:
                    i = square
                    while i // 8 == selected // 8:
                        if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                            possiblemoves.remove(i)
                        i += 1
                if square < selected and square // 8 == selected // 8:
                    i = square
                    while i // 8 == selected // 8:
                        if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                            possiblemoves.remove(i)
                        i -= 1
                if selected == square:
                    possiblemoves.remove(selected)
            except:
                pass
    if board[selected].boardpiece.piece == "b" or board[selected].boardpiece.piece == "B":
        for square in occupiedcheck:
            try:
                if square > selected:
                    if square % 8 < selected % 8:
                        i = square
                        while i % 8 != 7:
                            if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                                possiblemoves.remove(i)
                            i += 7
                    if square % 8 > selected % 8:
                        i = square
                        while i % 8 != 0:
                            if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                                possiblemoves.remove(i)
                            i += 9
                if square < selected:
                    if square % 8 < selected % 8:
                        i = square
                        while i % 8 != 7:
                            if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                                possiblemoves.remove(i)
                            i -= 9
                    if square % 8 > selected % 8:
                        i = square
                        while i % 8 != 0:
                            if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                                possiblemoves.remove(i)
                            i -= 7
                if selected == square:
                    possiblemoves.remove(selected)
            except:
                pass

    if board[selected].boardpiece.piece == "Q" or board[selected].boardpiece.piece == "q":
        for square in occupiedcheck:
            try:
                if square > selected and square % 8 == selected % 8:
                    i = square
                    while i % 8 == selected % 8:
                        if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                            possiblemoves.remove(i)
                        i += 8
                if square < selected and square % 8 == selected % 8:
                    i = square
                    while i % 8 == selected % 8:
                        if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                            possiblemoves.remove(i)
                        i -= 8
                if square > selected and square // 8 == selected // 8:
                    i = square
                    while i // 8 == selected // 8:
                        if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                            possiblemoves.remove(i)
                        i += 1
                if square < selected and square // 8 == selected // 8:
                    i = square
                    while i // 8 == selected // 8:
                        if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                            possiblemoves.remove(i)
                        i -= 1
                if square > selected:
                    if square % 8 < selected % 8:
                        i = square
                        while i % 8 != 7:
                            if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                                possiblemoves.remove(i)
                            i += 7
                    if square % 8 > selected % 8:
                        i = square
                        while i % 8 != 0:
                            if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                                possiblemoves.remove(i)
                            i += 9
                if square < selected:
                    if square % 8 < selected % 8:
                        i = square
                        while i % 8 != 7:
                            if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                                possiblemoves.remove(i)
                            i -= 9
                    if square % 8 > selected % 8:
                        i = square
                        while i % 8 != 0:
                            if i != square or board[square].boardpiece.color == board[selected].boardpiece.color:
                                possiblemoves.remove(i)
                            i -= 7
                if selected == square:
                    possiblemoves.remove(selected)
            except:
                pass
    return possiblemoves


def validmove(selected,
              intendedmove):  # piece is type of chess piece that is being moved. selected is location of chess piece that is being moved, color is the color of said piece, and intendedmove is where you want to move it
    if board[selected].boardpiece.piece == "p" or board[selected].boardpiece.piece == "P":
        if board[selected].boardpiece.color == Color.BLACK and selected > 7 and selected < 16:  # If the white pawn hasn't moved yet
            if ((board[selected + 8].boardpiece.occupied == False and intendedmove == selected + 8) or (
                    board[selected + 16].boardpiece.occupied == False and intendedmove == selected + 16)):
                return True
            else:
                return False
        if board[selected].boardpiece.color == Color.WHITE and selected > 47 and selected < 56:  # If the black pawn hasn't moved yet
            if ((board[selected - 8].boardpiece.occupied == False and intendedmove == selected - 8) or (
                    board[selected - 16].boardpiece.occupied == False and intendedmove == selected - 16)):
                return True
            else:
                return False
        if board[selected].boardpiece.color == Color.BLACK:
            if intendedmove == selected + 8 and board[intendedmove].boardpiece.occupied == False:
                return True
            elif selected % 8 == 0 and intendedmove == selected + 9 and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color:
                return True
            elif selected % 8 == 7 and intendedmove == selected + 7 and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color:
                return True
            elif (intendedmove == selected + 9 or intendedmove == selected + 7) and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color and selected % 8 != 0 and selected % 8 != 7:
                return True
        if board[selected].boardpiece.color == Color.WHITE:
            if intendedmove == selected - 8 and board[intendedmove].boardpiece.occupied == False:
                return True
            elif selected % 8 == 0 and intendedmove == selected - 7 and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color and board[intendedmove].boardpiece.color != "":
                return True
            elif selected % 8 == 7 and intendedmove == selected - 9 and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color and board[intendedmove].boardpiece.color != "":
                return True
            elif (intendedmove == selected - 9 or intendedmove == selected - 7) and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color and selected % 8 != 0 and selected % 8 != 7:
                return True
    elif board[selected].boardpiece.piece == "r" or board[selected].boardpiece.piece == "R":
        if abs(intendedmove - selected) % 8 == 0:
            return True
        if intendedmove // 8 == selected // 8:
            return True
    elif board[selected].boardpiece.piece == "b" or board[selected].boardpiece.piece == "B":
        i = 0
        while i + selected % 8 != 8:
            if intendedmove == 8 * i + i + selected or intendedmove == -(8 * i) + i + selected:
                return True
            i += 1
        i = 0
        while selected % 8 - i != -1:
            if intendedmove == 8 * i - i + selected or intendedmove == -(8 * i) - i + selected:
                return True
            i += 1
        i = 0
    elif (board[selected].boardpiece.piece == "n" or board[selected].boardpiece.piece == "N") and board[intendedmove].boardpiece.color != board[
        selected].boardpiece.color:
        if selected % 8 == 0:
            if selected // 8 == 0:
                if intendedmove == selected + 17 or intendedmove == selected + 10:
                    return True
            if selected // 8 == 1:
                if intendedmove == selected - 6 or intendedmove == selected + 10 or intendedmove == selected + 17:
                    return True
            if selected // 8 == 6:
                if intendedmove == selected - 15 or intendedmove == selected - 6 or intendedmove == selected + 10:
                    return True
            if selected // 8 == 7:
                if intendedmove == selected - 15 or intendedmove == selected - 6:
                    return True
            else:
                if intendedmove == selected + 17 or intendedmove == selected + 10 or intendedmove == selected - 15 or intendedmove == selected - 6:
                    return True
        elif selected % 8 == 1:
            if selected // 8 == 0:
                if intendedmove == selected + 17 or intendedmove == selected + 10 or intendedmove == selected + 15:
                    return True
            if selected // 8 == 1:
                if intendedmove == selected + 17 or intendedmove == selected + 10 or intendedmove == selected + 15 or intendedmove == selected - 6:
                    return True
            if selected // 8 == 6:
                if intendedmove == selected - 17 or intendedmove == selected - 15 or intendedmove == selected - 6 or intendedmove == selected + 10:
                    return True
            if selected // 8 == 7:
                if intendedmove == selected - 17 or intendedmove == selected - 15 or intendedmove == selected - 6:
                    return True
            else:
                if intendedmove == selected - 17 or intendedmove == selected - 15 or intendedmove == selected - 6 or intendedmove == selected + 10 or intendedmove == selected + 15 or intendedmove == selected + 17:
                    return True
        elif selected % 8 == 6:
            if selected // 8 == 0:
                if intendedmove == selected + 17 or intendedmove == selected + 15 or intendedmove == selected + 6:
                    return True
            if selected // 8 == 1:
                if intendedmove == selected + 17 or intendedmove == selected + 15 or intendedmove == selected - 10 or intendedmove == selected + 6:
                    return True
            if selected // 8 == 6:
                if intendedmove == selected - 17 or intendedmove == selected - 15 or intendedmove == selected + 66 or intendedmove == selected - 10:
                    return True
            if selected // 8 == 7:
                if intendedmove == selected - 17 or intendedmove == selected - 15 or intendedmove == selected - 10:
                    return True
            else:
                if intendedmove == selected - 17 or intendedmove == selected - 15 or intendedmove == selected + 6 or intendedmove == selected - 10 or intendedmove == selected + 15 or intendedmove == selected + 17:
                    return True
        elif selected % 8 == 7:
            if selected // 8 == 0:
                if intendedmove == selected + 6 or intendedmove == selected + 15:
                    return True
            if selected // 8 == 1:
                if intendedmove == selected - 10 or intendedmove == selected - 6 or intendedmove == selected + 16:
                    return True
            if selected // 8 == 6:
                if intendedmove == selected - 17 or intendedmove == selected - 10 or intendedmove == selected + 6:
                    return True
            if selected // 8 == 7:
                if intendedmove == selected - 10 or intendedmove == selected - 17:
                    return True
            else:
                if intendedmove == selected - 17 or intendedmove == selected - 10 or intendedmove == selected + 15 or intendedmove == selected + 6:
                    return True
        else:
            if intendedmove == selected - 17 or intendedmove == selected - 15 or intendedmove == selected - 10 or intendedmove == selected - 6 or intendedmove == selected + 6 or intendedmove == selected + 10 or intendedmove == selected + 15 or intendedmove == selected + 17:
                return True
    elif board[selected].boardpiece.piece == "q" or board[selected].boardpiece.piece == "Q":
        if abs(intendedmove - selected) % 8 == 0:
            return True
        if intendedmove // 8 == selected // 8:
            return True
        i = 0
        while i + selected % 8 != 8:
            if intendedmove == 8 * i + i + selected or intendedmove == -(8 * i) + i + selected:
                return True
            i += 1
        i = 0
        while selected % 8 - i != -1:
            if intendedmove == 8 * i - i + selected or intendedmove == -(8 * i) - i + selected:
                return True
            i += 1
        i = 0
    elif board[selected].boardpiece.piece == "k" or board[selected].boardpiece.piece == "K":
        if board[selected].boardpiece.color != board[intendedmove].boardpiece.color:
            if abs(intendedmove - selected) % 8 == 0 and (selected + 8 == intendedmove or selected - 8 == intendedmove):
                return True
            if intendedmove // 8 == selected // 8 and (selected + 1 == intendedmove or selected - 1 == intendedmove):
                return True
            if selected % 8 == 0:
                if selected // 8 == 0 and intendedmove == selected + 9:
                    return True
                if selected // 8 == 7 and intendedmove == selected - 7:
                    return True
                else:
                    if intendedmove == selected + 9 or intendedmove == selected - 7:
                        return True
            if selected % 8 == 7:
                if selected // 8 == 0 and intendedmove == selected + 7:
                    return True
                if selected // 8 == 7 and intendedmove == selected - 9:
                    return True
                else:
                    if intendedmove == selected + 7 or intendedmove == selected - 9:
                        return True
            else:
                if intendedmove == selected - 9 or intendedmove == selected + 7 or intendedmove == selected - 7 or intendedmove == selected + 9:
                    return True
    else:
        return False


def check(chessboard):  # Checks the moves that can be made in every square. If a opposite color piece can capture the king, then return true.
    for check in range(64):
        thelist = movelist(check)
        for number in thelist:
            if chessboard[number].boardpiece.piece == "k" and chessboard[check].boardpiece.color == Color.BLACK and turn == Color.WHITE:
                return True
            if chessboard[number].boardpiece.piece == "K" and chessboard[check].boardpiece.color == Color.WHITE and turn == Color.BLACK:
                return True
    return False


def checkmate():  # Checks for check in every situation given the possible moves each piece can make. If there is a instance where check will be false, return false.
    possibilities = 0
    for i in range(64):
        thelist = movelist(i)
        if board[i].boardpiece.color==turn:
            for square in thelist:
                if not check(simulatedmovement(i, square)):
                    print(thelist)
                    print(i)
                    print(square)
                    printgame(board)
                    printgame(simulatedmovement(i, square))
                    return False
    return True


def simulatedmovement(originalsquare,
                      simulatedsquare):  # Returns a copy of the board that has a square moved to the desire position. Used for checking for check if you move to other squares.
    simulatedboard = copy.deepcopy(board)
    simulatedboard[simulatedsquare].boardpiece = board[originalsquare].boardpiece
    simulatedboard[originalsquare].boardpiece = boardpiece().boardpiece
    return simulatedboard

def makemove(selected, intendedmove):
    if intendedmove in movelist(selected):
        oldsquarepiece = boardpiece()
        oldsquarepiece.color = copy.deepcopy(board[intendedmove].boardpiece.color)
        if board[intendedmove].boardpiece.image!=None:
            oldsquarepiece.image = board[intendedmove].boardpiece.image.copy()
        oldsquarepiece.piece = copy.deepcopy(board[intendedmove].boardpiece.piece)
        oldsquarepiece.occupied = copy.deepcopy(board[intendedmove].boardpiece.occupied)
        board[intendedmove].boardpiece = board[selected].boardpiece
        board[selected].boardpiece = boardpiece()
        if check(board):
            board[selected].boardpiece = board[intendedmove].boardpiece
            board[intendedmove].boardpiece = oldsquarepiece
        else:
            if intendedmove // 8 == 0 and board[intendedmove].boardpiece.piece == "p":
                promotion = input("Please select a piece to promote your pawn to: ")
                if promotion == "q" or promotion == "Q" or promotion == "Queen":
                    board[intendedmove].boardpiece.piece = "q"
                if promotion == "b" or promotion == "B" or promotion == "Bishop":
                    board[intendedmove].boardpiece.piece = "b"
                if promotion == "r" or promotion == "R" or promotion == "Rook":
                    board[intendedmove].boardpiece.piece = "r"
                if promotion == "n" or promotion == "N" or promotion == "Knight":
                    board[intendedmove].boardpiece.piece = "n"
            if intendedmove // 8 == 7 and board[intendedmove].boardpiece.piece == "P":
                promotion = input("Please select a piece to promote your pawn to: ")
                if promotion == "q" or promotion == "Q" or promotion == "Queen":
                    board[intendedmove].boardpiece.piece = "Q"
                if promotion == "b" or promotion == "B" or promotion == "Bishop":
                    board[intendedmove].boardpiece.piece = "B"
                if promotion == "r" or promotion == "R" or promotion == "Rook":
                    board[intendedmove].boardpiece.piece = "R"
                if promotion == "n" or promotion == "N" or promotion == "Knight":
                    board[intendedmove].boardpiece.piece = "N"
            global turn
            if turn == Color.WHITE:
                turn = Color.BLACK
            else:
                turn = Color.WHITE


def rungame():
    intendedmove = -1
    global winner
    while not winner:
        pygame.event.clear()
        if check(board):
            if checkmate():
                if turn == Color.WHITE:
                    print("Black wins!")
                else:
                    print("White wins!")
                break
        global select
        global selected
        if not select:
            if pygame.event.get(MOUSEBUTTONDOWN):
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                move = coordinatestosquare(x, y)
                print(movelist(move))
                if turn == board[move].boardpiece.color and len(movelist(move)) > 0:
                    select = True
                    selected = move
                    print("selected")
                else:
                    move = (-1,-1)
        if select:
            if pygame.event.peek(MOUSEBUTTONDOWN) and not coordinatestosquare(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) in movelist(selected) and (board[coordinatestosquare(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])].boardpiece.color!=board[selected].boardpiece.color or coordinatestosquare(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) == selected):
                print("unselected")
                select = False
                selected = -1
            elif pygame.event.peek(MOUSEBUTTONDOWN) and board[coordinatestosquare(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])].boardpiece.color==board[move].boardpiece.color:
                print("changed selected")
                selected = coordinatestosquare(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
            elif pygame.event.peek(MOUSEBUTTONDOWN) and coordinatestosquare(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) in movelist(move):
                print("intendedmove!")
                intendedmove = coordinatestosquare(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                makemove(selected,intendedmove)
                boarddraw()
                select = False
                selected = -1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.flip()
rungame()

