import pygame, sys

#constants and some drawing

######board / screen colors
#boarder of board and lines -->olive color
board = pygame.Color("#979683")
#where tiles go --> sand color
board2 = pygame.Color("#c2b280")
#main screen color --> brown
screenColor2 = pygame.Color("#907163")

####tile colors

colorDictionary = {
#empty tile --> sand
"0": pygame.Color("#c2b280"),
#red
"2" : pygame.Color("#ff0000"),
#orange
"4" : pygame.Color("#ffa500"),
#yellow
"8" : pygame.Color("#ffff00"),
#green
"16" : pygame.Color("#008000"),
#blue
"32" : pygame.Color("#0000ff"),
#indigo
"64" : pygame.Color("#4b0082"),
#violet
"128" : pygame.Color("#ee82ee"),
#pink
"256" : pygame.Color("#ffb6c1"),
#white
"512" : pygame.Color("#ffffff"),
#silver
"1024" : pygame.Color("#C0C0C0"),
#black
"2048" : pygame.Color("#000000") }





padLeft = 100
padTop = 130
displayWidth = 755
displayLength = 750
boardWidth = 555
tileWidth = 120
numTilesInARowOrColumn = 4
totalTiles = numTilesInARowOrColumn ** 2



borderWidth = 15

tileAndBorder = tileWidth + borderWidth

def boardDivider(display, iter):
    #vertical line
    pygame.draw.rect(display, board, pygame.Rect((padLeft + tileAndBorder) + (iter * tileAndBorder), padTop, borderWidth, boardWidth))
    #horizontal line
    pygame.draw.rect(display, board, pygame.Rect(padLeft, (padTop + tileAndBorder) + (iter * tileAndBorder), boardWidth, borderWidth))

def emptyTiles(display):
     pygame.draw.rect(display, board2, pygame.Rect(padLeft + borderWidth, padTop + borderWidth, boardWidth - (2 * borderWidth), boardWidth - (2 * borderWidth)))

def boardBorder(display):
    pygame.draw.rect(display, board, pygame.Rect(padLeft, padTop, boardWidth, boardWidth))

def drawTile(display, tileIndex, tileValue):
    # change color
    pygame.draw.rect(display, colorDictionary.get(str(tileValue)), pygame.Rect((padLeft + borderWidth) + (tileIndex % numTilesInARowOrColumn) * tileAndBorder,
                                                                               (padTop + borderWidth) + ((tileIndex // numTilesInARowOrColumn) * tileAndBorder),
                                                                               tileWidth,
                                                                               tileWidth))
def drawAllTiles(display, tiles):
    for i in range(totalTiles):
        drawTile(display, i, tiles[i])
