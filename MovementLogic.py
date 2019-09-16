from BoardClasses import boardpiece
from Enums import ChessPiece, PieceColor
from BoardSetup import emptyimages, addimages
import copy
def movelist(selected,board):  # Creates a list of validmoves. The purpose is to check check, and to apply collision (pieces blocking pieces)
    possiblemoves = []
    occupiedcheck = []  # A list of indexes that are in the path of validmoves (blocking the piece)
    for moves in range(64):  # Check all 64 squares to see if there is a validmove
        if validmove(selected, moves,board):
            possiblemoves.append(moves)  # If there is a valid move, add it to the list, ignoring collision
    for deletion in possiblemoves:  # Looking for impossible moves due to collision, and deleting them
        if board[deletion].boardpiece.occupied:
            occupiedcheck.append(deletion)
    if board[selected].boardpiece.piece == ChessPiece.ROOK:
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
    if board[selected].boardpiece.piece == ChessPiece.BISHOP:
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

    if board[selected].boardpiece.piece == ChessPiece.QUEEN:
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
              intendedmove,board):  # piece is type of chess piece that is being moved. selected is location of chess piece that is being moved, color is the color of said piece, and intendedmove is where you want to move it
    if board[selected].boardpiece.piece == ChessPiece.PAWN:
        if board[selected].boardpiece.color == PieceColor.BLACK and 7 < selected < 16:  # If the white pawn hasn't moved yet
            if board[selected + 16].boardpiece.occupied == False and intendedmove == selected + 16:
                return True
        if board[selected].boardpiece.color == PieceColor.WHITE and 47 < selected < 56:  # If the black pawn hasn't moved yet
            if board[selected - 16].boardpiece.occupied == False and intendedmove == selected - 16:
                return True
        if board[selected].boardpiece.color == PieceColor.BLACK:
            if intendedmove == selected + 8 and not board[intendedmove].boardpiece.occupied:
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
        if board[selected].boardpiece.color == PieceColor.WHITE:
            if intendedmove == selected - 8 and not board[intendedmove].boardpiece.occupied:
                return True
            elif selected % 8 == 0 and intendedmove == selected - 7 and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color and board[intendedmove].boardpiece.color != PieceColor.NONE:
                return True
            elif selected % 8 == 7 and intendedmove == selected - 9 and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color and board[intendedmove].boardpiece.color != PieceColor.NONE:
                return True
            elif (intendedmove == selected - 9 or intendedmove == selected - 7) and board[intendedmove].boardpiece.color != board[
                selected].boardpiece.color and selected % 8 != 0 and selected % 8 != 7:
                return True
    elif board[selected].boardpiece.piece == ChessPiece.ROOK:
        if abs(intendedmove - selected) % 8 == 0:
            return True
        if intendedmove // 8 == selected // 8:
            return True
    elif board[selected].boardpiece.piece == ChessPiece.BISHOP:
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
    elif (board[selected].boardpiece.piece == ChessPiece.KNIGHT) and board[intendedmove].boardpiece.color != board[
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
    elif board[selected].boardpiece.piece == ChessPiece.QUEEN:
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
    elif board[selected].boardpiece.piece == ChessPiece.KING:
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


def check(chessboard,turn):  # Checks the moves that can be made in every square. If a opposite color piece can capture the king, then return true.
    for index in range(64):
        thelist = movelist(index,chessboard)
        for checker in thelist:
            if chessboard[checker].boardpiece.piece == ChessPiece.KING:
                if chessboard[index].boardpiece.color == PieceColor.BLACK and chessboard[checker].color == PieceColor.WHITE\
                        and turn == PieceColor.WHITE:
                    return True
                elif chessboard[index].boardpiece.color == PieceColor.WHITE and chessboard[checker].boardpiece.color == PieceColor.BLACK\
                        and turn == PieceColor.BLACK:
                    return True
    return False


def checkmate(board,turn):  # Checks for check in every situation given the possible moves each piece can make. If there is a instance where check will be false, return false.
    possibilities = 0
    for i in range(64):
        thelist = movelist(i,board)
        if board[i].boardpiece.color==turn:
            for square in thelist:
                if not check(simulatedmovement(i, square,board),turn):
                    print(thelist)
                    print(i)
                    print(square)
                    return False
    return True

def simulatedmovement(originalsquare,
                      simulatedsquare,board):  # Returns a copy of the board that has a square moved to the desire position. Used for checking for check if you move to other squares.
    emptyimages(board)
    simulatedboard = copy.deepcopy(board)
    addimages(board)
    simulatedboard[simulatedsquare].boardpiece = board[originalsquare].boardpiece
    simulatedboard[originalsquare].boardpiece = boardpiece()
    return simulatedboard

def makemove(selected, intendedmove, turn,board): #Makes a move (if allowed), and returns whether it's Black or White's turn
    if intendedmove in movelist(selected,board):
        oldsquarepiece = boardpiece()
        oldsquarepiece.color = copy.deepcopy(board[intendedmove].boardpiece.color)
        if board[intendedmove].boardpiece.image!=None:
            oldsquarepiece.image = board[intendedmove].boardpiece.image.copy()
        oldsquarepiece.piece = copy.deepcopy(board[intendedmove].boardpiece.piece)
        oldsquarepiece.occupied = copy.deepcopy(board[intendedmove].boardpiece.occupied)
        board[intendedmove].boardpiece = board[selected].boardpiece
        board[selected].boardpiece = boardpiece()
        if check(board, turn):
            board[selected].boardpiece = board[intendedmove].boardpiece
            board[intendedmove].boardpiece = oldsquarepiece
        else:
            if intendedmove // 8 == 0 and board[intendedmove].boardpiece.piece == ChessPiece.PAWN:
                promotion = input("Please select a piece to promote your pawn to: ")
                if promotion == "q" or promotion == "Q" or promotion == "Queen":
                    board[intendedmove].boardpiece.piece = "q"
                if promotion == "b" or promotion == "B" or promotion == "Bishop":
                    board[intendedmove].boardpiece.piece = "b"
                if promotion == "r" or promotion == "R" or promotion == "Rook":
                    board[intendedmove].boardpiece.piece = "r"
                if promotion == "n" or promotion == "N" or promotion == "Knight":
                    board[intendedmove].boardpiece.piece = "n"
            if intendedmove // 8 == 7 and board[intendedmove].boardpiece.piece == ChessPiece.PAWN:
                promotion = input("Please select a piece to promote your pawn to: ")
                if promotion == "q" or promotion == "Q" or promotion == "Queen":
                    board[intendedmove].boardpiece.piece = "Q"
                if promotion == "b" or promotion == "B" or promotion == "Bishop":
                    board[intendedmove].boardpiece.piece = "B"
                if promotion == "r" or promotion == "R" or promotion == "Rook":
                    board[intendedmove].boardpiece.piece = "R"
                if promotion == "n" or promotion == "N" or promotion == "Knight":
                    board[intendedmove].boardpiece.piece = "N"
            if turn == PieceColor.WHITE:
                turn = PieceColor.BLACK
            else:
                turn = PieceColor.WHITE
    return turn
