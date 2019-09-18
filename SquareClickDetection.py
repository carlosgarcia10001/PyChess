SQUARELENGTH = 80
ROWINDEXMULTIPLIER = 8
CHESSPIECEOFFSET = 10
def coordinatestosquareindex(x,y):  # Used to convert x,y coordinates to square indexes. First square is ID 0, last square is index 63
    return y // SQUARELENGTH * ROWINDEXMULTIPLIER + x // SQUARELENGTH


def squareindextocoordinates(index):  # Used to convert square indexes to the first x,y coordinate of a square.
    return SQUARELENGTH * (index % ROWINDEXMULTIPLIER), SQUARELENGTH * (index // ROWINDEXMULTIPLIER)


def squareindextocoordinatespiecelocation(index):  # Used to place the actual Chess pieces.
    return CHESSPIECEOFFSET + SQUARELENGTH * (index % ROWINDEXMULTIPLIER), 10 + SQUARELENGTH * (index // ROWINDEXMULTIPLIER)

