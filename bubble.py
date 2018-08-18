#file for class of bubble and it's events
#Paweł Gałka 11.08


from settings import *


class Bubble(pygame.sprite.Sprite):
    def __init__(self, color, row=0, column=0, x=STARTX, y=STARTY):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0,0,30,30) #30 because balls have grid
        self.rect.centerx = x
        self.rect.centery = y
        self.radius = BALLRADIUS
        self.color = color
        self.row = row
        self.column = column
        self.speed = 0
        self.angle = 0

    def update(self, *args):
        xmove = math.cos(math.radians(self.angle))*self.speed
        ymove = -math.sin(math.radians(self.angle))*self.speed
        self.rect.centerx += xmove
        self.rect.centery += ymove

        if self.rect.left<0 or self.rect.right>WIDTH:
            self.angle = 180-self.angle

        if self.rect.top<0 or self.rect.bottom>HEIGHT:
            self.angle = 180-self.angle
            self.speed *= -1

    def draw(self):
        pygame.gfxdraw.filled_circle(display, self.rect.centerx, self.rect.centery, self.radius, self.color)
        pygame.gfxdraw.aacircle(display,self.rect.centerx, self.rect.centery, self.radius, BLACK)


    def shoot(self, angle):
        self.angle = angle
        self.speed = 10




