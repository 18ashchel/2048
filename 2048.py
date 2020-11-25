import pygame, sys
import random
import aux
import constants as c

pygame.init()

pygame.display.set_caption('2048')
display = pygame.display.set_mode((c.displayWidth, c.displayLength))
#display.fill(c.screenColor2)

#board
#outside border
c.boardBorder(display)

#where empty tiles will go
c.emptyTiles(display)

#board/tile dividers
for i in range(c.numTilesInARowOrColumn):
    c.boardDivider(display, i)

pygame.display.flip()

# Loop until the user clicks the close button.
done = False
firstMove = True
gameOver = False

# initial tiles present on the board
tiles = [0 for i in range(16)]
if firstMove:
    tiles = aux.placeRandomTile(tiles, 2)
    c.drawAllTiles(display, tiles)
    pygame.display.flip()



while not done:
    if gameOver:
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and not gameOver:
            if event.key == pygame.K_UP:
                results = aux.turn(display, tiles, 'Up')
                tiles = results[0]
                gameOver = results[1]

            if event.key == pygame.K_DOWN:
                results = aux.turn(display, tiles, 'Down')
                tiles = results[0]
                gameOver = results[1]

            if event.key == pygame.K_LEFT:
                results = aux.turn(display, tiles, 'Left')
                tiles = results[0]
                gameOver = results[1]

            if event.key == pygame.K_RIGHT:
                results = aux.turn(display, tiles, 'Right')
                tiles = results[0]
                gameOver = results[1]

pygame.quit()
