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
    #print(board[0][1].color)
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
        return vector, 0
    if vector.y < 0 and vector.x < 0:
        return vector, 180
    if vector.y < 0 and vector.x > 0:
        return vector, 0
    angle = math.degrees(math.atan(vector.y / vector.x))
    if angle < 0:
        angle += 180
    #print(angle)
    return vector, angle


def getBubble(colors):
    random.shuffle(colors)
    return Bubble(colors[0])


def stopBubble(board, ball):
    for row in range(len(board)):
        for col in range(len(board[row])):
            # print(row,col)
            if (board[row][col] != EMPTY and ball != None):
                if (pygame.sprite.collide_rect(ball, board[row][col])) or ball.rect.top < 0:
                    # print(pygame.sprite.collide_rect(ball, board[row][col]))
                    if ball.rect.top < 0:
                        #newRow, newColumn = addBubbleToTop(board, ball)
                        pass

                    elif ball.rect.centery>=board[row][col].rect.centery: #hitting under ball

                        if ball.rect.centerx<board[row][col].rect.centerx: #LD corner

                            if row%2==0: #longer line
                                newRow = row + 1
                                newCol = col - 1

                            else: #shorter line
                                newRow = row + 1
                                newCol = col

                        else:                                           #RD corner
                            if row%2==0: #longer line
                                newRow = row + 1
                                newCol = col

                            else: #shorter line
                                newRow = row + 1
                                newCol = col + 1

                        board[newRow][newCol] = copy.copy(ball)
                        print(board[newRow][newCol] is EMPTY)
                        board[newRow][newCol].row = newRow
                        board[newRow][newCol].col = newCol
                        ball = None

                    else:  # hitting over ball

                        if ball.rect.centerx < board[row][col].rect.centerx:  # LU corner

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
                                    newCol -= 1


                            else:  # shorter line
                                newRow = row - 1
                                newCol = col + 1
                                if board[newRow][newCol] is not EMPTY:
                                    newRow += 1


                        board[newRow][newCol] = copy.copy(ball)
                        board[newRow][newCol].row = newRow
                        board[newRow][newCol].col = newCol
                        ball = None

    setPosition(board)
    return ball, board

def checkBottom(board):
    for col in range (len(board[10])):
        if board[10][col]!=EMPTY:
            return False
    return True