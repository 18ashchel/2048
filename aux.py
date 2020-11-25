import constants as c
import random
import pygame
#auxilary functions / utilities

#input all tiles
#output the columns of tiles --> list of lists
def sliceVertical(tiles):
    arr = [[] for i in range(4)]
    for i in range(16):
        arr[i % 4].append(tiles[i])
    return arr

#input all tiles
#output the rows of tiles -->lists of lists
def sliceHorizontal(tiles):
    arr = [[] for i in range(4)]
    for i in range(16):
        arr[i // 4].append(tiles[i])
    return arr

#input the column or row of tiles and if they are moving left or up
#new positions of the tiles for that column / row in proper place
def slideSection(subSection, leftUp):
    # if you're moving left / up you need to slide everything to the left
    # start from the beginning / left of the array and move the tiles towards index 0
    # touching the farthest tile from the top / left last
    if leftUp:
        iStart = 0
        iEnd = 4
        iChange = 1
    # same thing as above but now you're moving everyting to the end of the array (index 3)
    # touching everything farthest from the right / bottom (index 0) last
    else:
        iStart = 3
        iEnd = -1
        iChange = -1

    #outter loop to move each of the tiles
    for i in range(iStart, iEnd, iChange):
        if subSection[i] == 0:
            continue
        tempNewPosition = i
        currentValue = subSection[i]
        flag = True
        # for the j for Loop
        if leftUp:
            jStart = i - 1
            jEnd = -1
            jChange = -1
            jBeginning = 0
        else:
            jStart = i + 1
            jEnd = 4
            jChange = 1
            jBeginning = 3
            #inner loop to see where the tile will combine or move (if it can)
        for j in range(jStart, jEnd, jChange):
            # empty tile
            if subSection[j] == 0:
                tempNewPosition = j
                subSection[i] = 0
            # combine tiles
            elif subSection[j] == currentValue:
                subSection[j] *= 2
                subSection[i] = 0
                flag = False
                break
            # block that is not equal
            else:
                subSection[tempNewPosition] = currentValue
                flag = False
                break
        # if it reached the end of the inner loop and couldn't move
        if flag:
            subSection[jBeginning] = currentValue
    return subSection


#input all tiles, if they're moving left or up, and if they're moving horizontally
#output final position of tiles on the proper movement
#slide up all the tiles
def slideAll(tiles, leftUp, horizontal):
    # list of lists of the row/column
    #if you're moving horizontally -->slice by row major order
    if horizontal:
        subSection = sliceHorizontal(tiles)
    #otherwise column major order
    else:
        subSection = sliceVertical(tiles)

    # slide up each subSection
    for i in range(4):
        subSection[i] = slideSection(subSection[i], leftUp)

    # put tiles together and return
    if horizontal:
        final = []
        for i in range(4):
            for j in range(4):
                final.append(subSection[i][j])

    else:
        #2D array to 1D array
        final = [0 for i in range(16)]
        for i in range(4):
            for j in range(4):
                final[i * 4 + j] = subSection[j][i]

    return final


#print the tiles in a 4x4 fashion
def prettyPrint(tiles):
    print('\t==========')
    for i in range(16):
        if i % 4 == 0:
            print('\n')
            print('\t', tiles[i], end=" ")
        else:
            print(tiles[i], end=" ")
    print('\n')
    print('\t==========')

#if all tiles are filled you cannot place another tile
def allFilledCheck(tiles):
    allFilled = True
    for i in range(c.totalTiles):
        if tiles[i] == 0:
            allFilled = False
    return allFilled


def placeRandomTile(tiles, numberTimes = 1):
    if not allFilledCheck(tiles):
        for i in range(numberTimes):
            #give a value of either 2 or 4
            value = 2 * random.randrange(1, 3)
            # keep searching for an empty tile
            while True:
                place = random.randrange(0, c.totalTiles)
                if tiles[place] == 0:
                    tiles[place] = value
                    break
    return tiles

def turn(display, tiles, keyStroke):
    oldTiles = tiles
    tilesUp = slideAll(tiles, True, False)
    tilesDown = slideAll(tiles, False, False)
    tilesLeft = slideAll(tiles, True, True)
    tilesRight = slideAll(tiles, False, True)

    tileDictionary = {
        'Up' : tilesUp,
        'Down' : tilesDown,
        'Left' : tilesLeft,
        'Right' : tilesRight
    }

    #did the move make a difference?
    if oldTiles == tilesUp and oldTiles == tilesDown and oldTiles == tilesLeft and oldTiles == tilesRight:
        #game over
        return [[], True]

    else:
        newTiles = tileDictionary.get(keyStroke)
        if oldTiles == newTiles:
            #not game over, but no change
            pass
        else:
            #draw the new tiles
            c.drawAllTiles(display, newTiles)
            display.blit(display, (0, 0))
            newTiles = placeRandomTile(newTiles)
            c.drawAllTiles(display, newTiles)
            pygame.display.flip()
        return [newTiles, False]
