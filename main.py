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
    arrow = Arrow()
    while 1:

        display.fill(BEIGE)

        vector, angle = getVector()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if not launchBall:
                    ball.shoot(angle)

                launchBall = True


            if event.type == MOUSEMOTION:
                arrow.update(angle, vector)


        nextBall = getBubble(COLORS)
        drawBoard(board)

        if ball is not None:
            ball.update()
            ball.draw()
            ball, board = stopBubble(board, ball)

        else:
            launchBall = False
            ball = nextBall

        arrow.draw()

        if not checkBottom(board):
            return
        pygame.display.update()
        clock.tick(FPS)




if __name__=='__main__':
    main()