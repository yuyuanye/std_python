import pygame						#导入pygame模块
from pygame.locals import *
import sys
def hello_world():
    pygame.init()    #任何pygame程序均需要执行此句进行模块初始化    
    #设置窗口的模式，（680，480）表示窗口像素，及（宽度，高度）
    #此函数返回一个surface对象，本程序不使用它，故没保存到对象变量中
    pygame.display.set_mode((680, 480))    
    #设置窗口标题
    pygame.display.set_caption('Hello World!')
    
    #循环，直到接收到窗口关闭事件
    while True:
        #处理事件
        for event in pygame.event.get():
            #接收到窗口关闭事件
            if event.type == QUIT:
                #退出
                pygame.quit()
                sys.exit()
        #将surface对象上绘制在屏幕上        
        pygame.display.update()
if __name__ == "__main__":
    hello_world()
