import pygame
from pygame.locals import *
import sys
def play_tank():    
    pygame.init()
    fpsClock = pygame.time.Clock()
     
    #窗口大小
    window_size = (width, height) =(600, 400)    
    #坦克运行偏移量[水平，垂直]，值越大，移动越快
    speed = [1, 1]    
    #窗口背景色RGB值
    color_black = (255, 255, 255)    
    #设置窗口模式
    screen = pygame.display.set_mode(window_size)    
    #设置窗口标题
    pygame.display.set_caption('自由移动的坦克')    
    #加载坦克图片
    tank_image = pygame.image.load('tankU.bmp')    
    #获取坦克图片的区域开状
    tank_rect = tank_image.get_rect()
    fpsClock = pygame.time.Clock()
    while True:
        fpsClock.tick(50)
        #退出事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #使坦克移动，速度由speed变量控制
        tank_rect = tank_rect.move(speed)        
        #当坦克运动出窗口时，重新设置偏移量
        if (tank_rect.left < 0) or (tank_rect.right > width):#水
            speed[0] =- speed[0]
        if (tank_rect.top < 0) or (tank_rect.bottom > height):#垂直平方向
            speed[1] =- speed[1]        
        
        screen.fill(color_black) #填充窗口背景
        screen.blit(tank_image, tank_rect) #在背景Surface上绘制 坦克
        pygame.display.update() #更新窗口内容
        #fpsClock.tick(50)
        
if __name__ == '__main__':
    play_tank()
