import pygame,sys
pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('beach_ball.png')
x=50
y=50
z=5
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        screen.blit(my_ball,[x,y])
#pygame.draw.cirrancle(screen,[255,0,0],[320,240],30,0)
        pygame.display.flip()
        for i in range(100):
    
            for j in range(10):
        
                pygame.time.delay(20)
                pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
        
                y+=5
                screen.blit(my_ball,[x,y])
                pygame.display.flip()
    
            pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
            x+=z
            y=50
            if x>screen.get_width()-90 or x<0:
                z=-z


pygame.quit()
print p
