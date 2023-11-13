import pygame,sys

pygame.init()
size=width,height=640,480
screen=pygame.display.set_mode(size)
background=pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock=pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=location
        self.speed=speed
        
    def move(self):
        
        if self.rect.left<=screen.get_rect().left or self.rect.right>=screen.get_rect().right:
            self.speed[0]=-self.speed[0]
        newpos=self.rect.move(self.speed)
        self.rect=newpos
myball=Ball('beach_ball.png',[10,0],[20,20])

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    clock.tick(30)
    screen.blit(background,(0,0))
    myball.move()
    screen.blit(myball.image,myball.rect)
    pygame.display.flip()
pygame.quit()
