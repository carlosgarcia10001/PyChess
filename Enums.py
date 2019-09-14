from enum import Enum
class PieceColor(Enum):
    NONE = 0
    WHITE = 1
    BLACK = 2

class ChessPiece(Enum):
    NONE = 0
    PAWN = 1
    KNIGHT = 2
    KING = 3
    QUEEN = 4
    BISHOP = 5
    ROOK = 6