SQUARELENGTH = 80
def coordinatestosquareindex(x,y): #Used to convert x,y coordinates to square IDs. First square is ID 0, last square is ID 63
    return y//SQUARELENGTH*8+x//SQUARELENGTH
def squareindextocoordinates(square): #Used to convert square IDs to the first x,y coordinate of a square.
    return (SQUARELENGTH*(square%8),SQUARELENGTH*(square//8))
def squaretocoordinatespiecelocation(square): #Used to place the actual Chess pieces.
    return (10+SQUARELENGTH*(square%8),10+SQUARELENGTH*(square//8))

