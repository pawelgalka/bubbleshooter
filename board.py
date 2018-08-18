# coding=utf-8

from settings import *
from bubble import *

def CreateEmptyBoard():
    board = []

    for i in range (ROWS):
        col = []
        for j in range (COLS):
            col.append(EMPTY)
        board.append(col)

    return board


def FillBoard(board, colorlist):
    for i in range(STARTLAYERS):
        for j in range(len(board[i])):
            random.shuffle(colorlist)
            newBubble = Bubble(colorlist[0])
            board[i][j] = newBubble
    setPosition(board)


def setPosition(board):
    #set them in array
    for row in range(ROWS):
        for col in range(len(board[row])):
            if board[row][col]!=EMPTY:
                board[row][col].rect.x = (BALLSIZE*col)+5*WIDTH/640
                board[row][col].rect.y = (BALLSIZE*row)+5*HEIGHT/480
                #print(row,col,board[row][col].rect.x,board[row][col].rect.y)

    #make pattern - move odd rows
    for row in range (1, ROWS, 2):
        for col in range(len(board[row])):
            if board[row][col]!=EMPTY:
                board[row][col].rect.x += BALLRADIUS

    #delete empty space between balls
    for row in range(1, ROWS):
        for col in range(len(board[row])):
            if board[row][col]!=EMPTY:
                board[row][col].rect.y -= row*5*HEIGHT/480

    deleteExtraBalls(board)


def deleteExtraBalls(board):
    for row in range(ROWS):
        for col in range(len(board[row])):
            if board[row][col] != EMPTY:
                if board[row][col].rect.right > WIDTH:
                    board[row][col] = EMPTY

def drawBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                board[i][j].draw()


def getVector():
    mousePos = pygame.mouse.get_pos()
    vector = pygame.math.Vector2((mousePos[0] - STARTX, STARTY - mousePos[1]))
    if vector.x == 0 :
        return vector, 90
    if vector.y < 0 and vector.x < 0:
        return vector, 179
    if vector.y < 0 and vector.x > 0:
        return vector, 1
    angle = math.degrees(math.atan(vector.y / vector.x))
    if angle < 0:
        angle += 180
    #print(angle)
    return vector, angle


def getBubble(colors):
    random.shuffle(colors)
    return Bubble(colors[0], x=WIDTH-BALLSIZE-10)


def stopBubble(board, ball):
    for row in range(len(board)):
        for col in range(len(board[row])):
            # print(row,col)
            if (board[row][col] != EMPTY and ball != None):
                # print(ball.rect.top)
                if (pygame.sprite.collide_rect(ball, board[row][col])) or ball.rect.top <= 0:
                    # print(pygame.sprite.collide_rect(ball, board[row][col]))

                    if ball.rect.top <= 0:
                        newCol, newRow = addToTop(ball, board)
                        board[newRow][newCol] = copy.copy(ball)
                        board[newRow][newCol].row = newRow
                        board[newRow][newCol].col = newCol
                        # print(newRow,newCol)



                    elif ball.rect.centery>=board[row][col].rect.centery: #hitting under ball
                        # print('pod',row,col)
                        if ball.rect.centerx<board[row][col].rect.centerx: #LD corner

                            if row%2==0: #longer line
                                newRow = row + 1
                                newCol = col - 1

                            else: #shorter line
                                newRow = row + 1
                                newCol = col

                        else:               #RD corner
                            if row%2==0: #longer line
                                newRow = row + 1
                                newCol = col

                            else: #shorter line
                                newRow = row + 1
                                newCol = col + 1

                        board[newRow][newCol] = copy.copy(ball)
                        # print(board[newRow][newCol] is EMPTY)
                        board[newRow][newCol].row = newRow
                        board[newRow][newCol].col = newCol


                    else:  # hitting over ball
                        # print('nad',row,col)
                        if row == 0:
                            # pass
                            newCol, newRow = addToTop(ball, board)
                        elif ball.rect.centerx < board[row][col].rect.centerx:  # LU corner


                            if row % 2 == 0:  # longer line
                                newRow = row - 1
                                newCol = col - 1
                                if board[newRow][newCol] is not EMPTY:
                                    newRow += 1

                            else:  # shorter line
                                newRow = row - 1
                                newCol = col
                                if board[newRow][newCol] is not EMPTY:
                                    newRow += 1
                                    newCol -= 1

                        else:  # RU corner
                            if row % 2 == 0:  # longer line
                                newRow = row - 1
                                newCol = col
                                if board[newRow][newCol] is not EMPTY:
                                    newRow += 1
                                    newCol += 1


                            else:  # shorter line
                                newRow = row - 1
                                newCol = col + 1
                                if board[newRow][newCol] is not EMPTY:
                                    newRow += 1

                        # print(newRow, newCol)
                        board[newRow][newCol] = copy.copy(ball)
                        board[newRow][newCol].row = newRow
                        board[newRow][newCol].col = newCol

                    deleteList = []
                    deleteBubbles(board, newRow, newCol, ball.color, deleteList)
                    if len(deleteList)>=3:
                        popBubbles(board,deleteList)
                        print(deleteList)

                    deleteFloaters(board)
                    ball = None
    setPosition(board)
    # updateColors(board,COLORS)
    print(COLORS)
    checkwin = checkWin(board)
    return ball, board, checkwin



def deleteFloaters(board):
    filledFirst = []
    pattern = [i for i in range(16)]

    for col in range(len(board[0])):
        if board[0][col]!=EMPTY:
            filledFirst.append(col)


    unfilledList = diff(filledFirst,pattern)
    unfilledList.insert(0,0)
    print(unfilledList)
    copyBoard = copy.deepcopy(board)
    for row in range (len(board)):
        for col in range(len(board[row])):
            board[row][col]=EMPTY
    print(board)
    for col in unfilledList:
        checkFloaters(board,copyBoard,0,col)


def checkFloaters(board, copyBoard, row, col):

    if row<0 or row>len(board)-1 or col<0 or col>len(board[row])-1:
        print(1)
        return

    elif copyBoard[row][col]==EMPTY:
        # print(row, col, board[row][col], copyBoard[row][col], end=' ')
        print(2)
        return

    elif board[row][col] == copyBoard[row][col]:
        # print(row, col, board[row][col], copyBoard[row][col], end=' ')
        print(3)
        return

    board[row][col] = copyBoard[row][col]

    if row%2 == 0: #check LU,RU,L,R,LD,RD
        if row!=0:
            checkFloaters(board, copyBoard, row - 1, col - 1)  # left up
            checkFloaters(board, copyBoard, row - 1, col)  # right up

        checkFloaters(board, copyBoard, row, col - 1) # left
        checkFloaters(board, copyBoard, row, col + 1) # right
        checkFloaters(board, copyBoard, row + 1, col - 1) # left down
        checkFloaters(board, copyBoard, row + 1, col) # right down

    else:
        checkFloaters(board, copyBoard, row - 1, col)  # left up
        checkFloaters(board, copyBoard, row - 1, col + 1)  # right up
        checkFloaters(board, copyBoard, row, col - 1)  # left
        checkFloaters(board, copyBoard, row, col + 1)  # right
        checkFloaters(board, copyBoard, row + 1, col)  # left down
        checkFloaters(board, copyBoard, row + 1, col + 1)  # right down


def addToTop(ball, board):
    newRow = 0
    x = ball.rect.centerx

    newCol = math.floor(x*COLS/WIDTH)
    # newCol = ((x + 5) * COLS) // WIDTH
    # if (board[newRow][newCol] is not EMPTY):
    #     if ball.rect.right <= board[newRow][newCol].rect.left:
    #         newCol -= 1
    #     else:
    #         newCol += 1
    return newCol, newRow


def deleteBubbles(board, row, col, color, deleteList):
    # print("wejscie")
    if row < 0 or row > len(board)-1 or col < 0 or col > len(board[row])-1: # out of range
        return

    if board[row][col] is EMPTY: # field is empty
        return

    if board[row][col].color != color: # not right color
        return

    for ball in deleteList: # check if field is not already on list to delete
        if ball[0]==row and ball[1]==col:
            return

    deleteList.append((row,col))


    # if row == 0: #check L,R,LD,RD
    #     deleteBubbles(board, row, col - 1, color, deleteList) # left
    #     deleteBubbles(board, row, col + 1, color, deleteList) # right
    #     deleteBubbles(board, row + 1, col - 1, color, deleteList) # left down
    #     deleteBubbles(board, row + 1, col, color, deleteList) # right down

    if row%2 == 0: #check LU,RU,L,R,LD,RD
        if row!=0:
            deleteBubbles(board, row - 1, col - 1, color, deleteList)  # left up
            deleteBubbles(board, row - 1, col, color, deleteList)  # right up

        deleteBubbles(board, row, col - 1, color, deleteList) # left
        deleteBubbles(board, row, col + 1, color, deleteList) # right
        deleteBubbles(board, row + 1, col - 1, color, deleteList) # left down
        deleteBubbles(board, row + 1, col, color, deleteList) # right down

    else:
        deleteBubbles(board, row - 1, col, color, deleteList)  # left up
        deleteBubbles(board, row - 1, col + 1, color, deleteList)  # right up
        deleteBubbles(board, row, col - 1, color, deleteList)  # left
        deleteBubbles(board, row, col + 1, color, deleteList)  # right
        deleteBubbles(board, row + 1, col, color, deleteList)  # left down
        deleteBubbles(board, row + 1, col + 1, color, deleteList)  # right down

# def updateColors(board, colorList):
#     colorList.clear()
#     for row in range (len(board)):
#         for col in range(len(board[row])):
#             if board[row][col]!=EMPTY and board[row][col].color not in colorList :
#                 colorList.append(color)

def popBubbles(board, deleteList):
    pygame.time.delay(40)
    for bubble in deleteList:
        board[bubble[0]][bubble[1]] = EMPTY

def checkWin(board):
    for row in range (len(board)):
        for col in range(len(board[row])):
            if board[row][col]!=EMPTY:
                return False
    return True

def checkBottom(board):
    for col in range (len(board[10])):
        if board[10][col]!=EMPTY:
            return False
    return True