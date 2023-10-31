import os
import sys
import pygame
from pygame.locals import *
def show_text(surface_handle, pos, text, color, font_bold = False, font_size = 13, font_italic = False): 
    #cur_font = pygame.font.SysFont("宋体", font_size)
    cur_font = pygame.font.Font('simfang.ttf', 30)    #获取系统字体，并设置文字大小
    cur_font.set_bold(font_bold)    #设置是否加粗属性
    cur_font.set_italic(font_italic)    #设置是否斜体属性
    text_fmt = cur_font.render(text, 1, color)    #设置文字内容
    surface_handle.blit(text_fmt, pos)    #绘制文字
  
def control_tank(event):                #控制小球运动    
    speed = [x, y] = [0, 0]             #相对坐标 
    speed_offset = 1                    #速度    
    #当方向键按下时，进行位置计算
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed[0] -= speed_offset
        if event.key == pygame.K_RIGHT:
            speed[0] = speed_offset
        if event.key == pygame.K_UP:
            speed[1] -= speed_offset
        if event.key == pygame.K_DOWN:
            speed[1] = speed_offset    
    #当方向键释放时，相对偏移为0，即不移动
    if event.type in (pygame.KEYUP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN) :
        speed = [0, 0]            
    return speed
            
def play_tank():
    pygame.init()    
    window_size = Rect(0, 0, 600, 400)                  #窗口大小
    speed = [1, 1]                #坦克运行偏移量[水平，垂直]，值越大，移动越快
    color_black = (255, 255, 255)                      #窗口背景色RGB值（白色）
    screen = pygame.display.set_mode(window_size.size)  #设置窗口模式
    pygame.display.set_caption('自由移动的坦克')        #设置窗口标题
    tank_image = pygame.image.load('tankU.bmp')        #加载坦克图片    
    #加载窗口背景图片
    back_image = pygame.image.load('back_image.jpg')    
    tank_rect = tank_image.get_rect()                   #获取坦克图片的区域形状
    
    while True:        
        #退出事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #使坦克移动，速度由speed变量控制
        cur_speed = control_tank(event)
        #Rect的clamp方法使用移动范围限制在窗口内
        tank_rect = tank_rect.move(cur_speed).clamp(window_size)
        screen.blit(back_image, (0, 0))                         #设置窗口背景图片
        screen.blit(tank_image, tank_rect) 			#在窗口Surface上绘制坦克
        text_pos = "坦克大战"
        show_text(screen, (20,200), text_pos, (255, 0, 0), True)
        text_pos = u"坦克位置:(%d,%d)" % (tank_rect.left, tank_rect.top)
        show_text(screen, (20, 320), text_pos, (0, 255, 255), True)


        pygame.display.update()					#更新窗口显示内容

        
if __name__ == '__main__':
    play_tank()
