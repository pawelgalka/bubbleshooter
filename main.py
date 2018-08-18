# coding=utf-8

#Paweł Gałka 11.08

from settings import *
from bubble import *
from arrow import Arrow
from board import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    board = CreateEmptyBoard()

    FillBoard(board,COLORS)
    launchBall = False
    ball = getBubble(COLORS)
    ball.rect.centerx = STARTX
    nextBall = getBubble(COLORS)
    # board[0][15] = copy.deepcopy(ball)
    # setPosition(board)
    arrow = Arrow()

    while 1: # main game loop
        display.fill(BEIGE)
        vector, angle = getVector()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()



            if event.type == MOUSEBUTTONDOWN:
                if not launchBall:
                    ball.shoot(angle)

                launchBall = True


            if event.type == MOUSEMOTION:
                arrow.update(angle, vector)



        drawBoard(board)
        nextBall.draw()

        if ball is not None:

            ball.update()
            ball.draw()
            #print(ball.rect.centerx, ball.rect.centery)
            ball, board, checkwin = stopBubble(board, ball)


        else:
            launchBall = False
            ball = Bubble(nextBall.color)
            nextBall = getBubble(COLORS)

        arrow.draw()


        if checkwin:
            return 1
        elif checkBottom(board)==False:
            return 2
        pygame.display.update()
        clock.tick(FPS)




if __name__=='__main__':
    main()