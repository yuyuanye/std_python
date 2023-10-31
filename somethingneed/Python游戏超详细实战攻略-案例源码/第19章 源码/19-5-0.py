import pygame,sys
pygame.init()
class Tank(pygame.sprite.Sprite):
    def __init__(self,filename,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename)
        self.rect=self.image.get_rect()			#获取self.image大小
        #self.rect.topleft=initial_position			#确定左上角显示位置
        self.rect.bottomright=initial_position

screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
fi='tankU.bmp'
b=Tank(fi,[150,100])

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(b.image,b.rect)
    pygame.display.update()

