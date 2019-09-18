import pygame
from BoardClasses import boardsquare, boardpiece
from SquareClickDetection import squareindextocoordinates, squareindextocoordinatespiecelocation, coordinatestosquareindex
from Enums import PieceColor, ChessPiece
import copy
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

def getbackgroundcolor(index):
    background = (125,125,125)
    if index%2==0:
        if (index//8)%2==0:
            background=black
        else:
            background= white
    if index%2==1:
        if (index//8)%2==0:
            background = white
        else:
            background = black
    return background

def emptyimages(board):
    for i in range(64):
        board[i].boardpiece.image=None
def addimages(board):
    for i in range(64):
        board[i] = piecetoimage(board[i])

def setupboard(board):
    for i in range(64):
        board.append(boardsquare())
        board[i].backgroundrect = pygame.Rect((squareindextocoordinates(i))[0],
                                              (squareindextocoordinates(i))[1], 80, 80)
    wp = boardpiece()
    wp.piece = ChessPiece.PAWN
    wp.color = PieceColor.WHITE
    wr = boardpiece()
    wr.piece = ChessPiece.ROOK
    wr.color = PieceColor.WHITE
    wb = boardpiece()
    wb.piece = ChessPiece.BISHOP
    wb.color = PieceColor.WHITE
    wn = boardpiece()
    wn.piece = ChessPiece.KNIGHT
    wn.color = PieceColor.WHITE
    wk = boardpiece()
    wk.piece = ChessPiece.KING
    wk.color = PieceColor.WHITE
    wq = boardpiece()
    wq.piece = ChessPiece.QUEEN
    wq.color = PieceColor.WHITE
    bp = boardpiece()
    bp.piece = ChessPiece.PAWN
    bp.color = PieceColor.BLACK
    br = boardpiece()
    br.piece = ChessPiece.ROOK
    br.color = PieceColor.BLACK
    bb = boardpiece()
    bb.piece = ChessPiece.BISHOP
    bb.color = PieceColor.BLACK
    bn = boardpiece()
    bn.piece = ChessPiece.KNIGHT
    bn.color = PieceColor.BLACK
    bk = boardpiece()
    bk.piece = ChessPiece.KING
    bk.color = PieceColor.BLACK
    bq = boardpiece()
    bq.piece = ChessPiece.QUEEN
    bq.color = PieceColor.BLACK
    board[0].boardpiece = copy.deepcopy(br)
    board[1].boardpiece = copy.deepcopy(bn)
    board[2].boardpiece = copy.deepcopy(bb)
    board[3].boardpiece = copy.deepcopy(bq)
    board[4].boardpiece = copy.deepcopy(bk)
    board[5].boardpiece = copy.deepcopy(bb)
    board[6].boardpiece = copy.deepcopy(bn)
    board[7].boardpiece = copy.deepcopy(br)
    board[8].boardpiece = copy.deepcopy(bp)
    board[9].boardpiece = copy.deepcopy(bp)
    board[10].boardpiece = copy.deepcopy(bp)
    board[11].boardpiece = copy.deepcopy(bp)
    board[12].boardpiece = copy.deepcopy(bp)
    board[13].boardpiece = copy.deepcopy(bp)
    board[14].boardpiece = copy.deepcopy(bp)
    board[15].boardpiece = copy.deepcopy(bp)

    board[63].boardpiece = copy.deepcopy(wr)
    board[62].boardpiece = copy.deepcopy(wn)
    board[61].boardpiece = copy.deepcopy(wb)
    board[60].boardpiece = copy.deepcopy(wk)
    board[59].boardpiece = copy.deepcopy(wq)
    board[58].boardpiece = copy.deepcopy(wb)
    board[57].boardpiece = copy.deepcopy(wn)
    board[56].boardpiece = copy.deepcopy(wr)
    board[55].boardpiece = copy.deepcopy(wp)
    board[54].boardpiece = copy.deepcopy(wp)
    board[53].boardpiece = copy.deepcopy(wp)
    board[52].boardpiece = copy.deepcopy(wp)
    board[51].boardpiece = copy.deepcopy(wp)
    board[50].boardpiece = copy.deepcopy(wp)
    board[49].boardpiece = copy.deepcopy(wp)
    board[48].boardpiece = copy.deepcopy(wp)
    for i in range(64):
        board[i].backgroundcolor = getbackgroundcolor(i)
        if board[i].boardpiece.piece != ChessPiece.NONE:
            board[i].boardpiece.occupied = True
        piecetoimage(board[i])
    return board

def piecetoimage(boardsquare):
    if boardsquare.boardpiece.color==PieceColor.WHITE:
        if boardsquare.boardpiece.piece == ChessPiece.PAWN:
            boardsquare.boardpiece.image= wP.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.BISHOP:
            boardsquare.boardpiece.image= wB.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.KNIGHT:
            boardsquare.boardpiece.image = wN.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.KING:
            boardsquare.boardpiece.image = wK.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.QUEEN:
            boardsquare.boardpiece.image = wQ.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.ROOK:
            boardsquare.boardpiece.image = wR.copy()
    elif boardsquare.boardpiece.color==PieceColor.BLACK:
        if boardsquare.boardpiece.piece == ChessPiece.PAWN:
            boardsquare.boardpiece.image= bP.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.BISHOP:
            boardsquare.boardpiece.image= bB.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.KNIGHT:
            boardsquare.boardpiece.image = bN.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.KING:
            boardsquare.boardpiece.image = bK.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.QUEEN:
            boardsquare.boardpiece.image = bQ.copy()
        elif boardsquare.boardpiece.piece == ChessPiece.ROOK:
            boardsquare.boardpiece.image = bR.copy()
    return boardsquare

def boarddraw(screen, board):
    for i in range(64):
        pygame.draw.rect(screen, board[i].backgroundcolor,board[i].backgroundrect)
        if board[i].boardpiece.image!=None:
           screen.blit(board[i].boardpiece.image, squareindextocoordinatespiecelocation(i))
    pygame.display.flip()

