#file for class of bubble and it's events
#Paweł Gałka 11.08


from settings import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 90
        arrowImage = pygame.image.load('arrow.png')
        arrowImage.convert_alpha()
        arrowRect = arrowImage.get_rect()
        self.image = arrowImage
        self.transImage = self.image
        self.rect = arrowRect
        self.rect.centerx = STARTX
        self.rect.centery = STARTY

    def draw(self):
        display.blit(self.transImage, self.rect)

    def update(self, angle, vector):
        self.transImage = pygame.transform.rotate(self.image, -self.angle+angle)
        self.rect = self.transImage.get_rect(center=self.rect.midbottom)
        self.rect.centerx = STARTX
        self.rect.centery = STARTY


