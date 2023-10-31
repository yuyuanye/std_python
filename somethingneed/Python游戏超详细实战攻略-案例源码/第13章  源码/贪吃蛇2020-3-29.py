from tkinter import *
from tkinter.messagebox import *
from random import randint
import sys
class Grid(object):
    def __init__(self,master=None,window_width=800,window_height=600,grid_width=50,offset=10):
        self.height = window_height
        self.width = window_width
        self.grid_width = grid_width
        self.offset = offset
        self.grid_x = self.width//self.grid_width   #计算格子X方向数量
        self.grid_y = self.height//self.grid_width  #计算格子Y方向数量
        self.bg = "#EBEBEB"
        self.canvas = Canvas(master, width=self.width+2*self.offset,
                                 height=self.height+2*self.offset, bg=self.bg)#设置画布大小
        self.canvas.pack()
        self.grid_list()			#获取游戏场地的所有格子，可以用来判断出界
    def draw(self, pos, color): 		#绘制方格
        x = pos[0]*self.grid_width + self.offset
        y = pos[1]*self.grid_width + self.offset
        self.canvas.create_rectangle(x, y, x+self.grid_width, y+self.grid_width,fill=color,outline=self.bg)
    def grid_list(self):
        grid_list = []
        for y in range(0,self.grid_y):
            for x in range(0,self.grid_x):
                grid_list.append((x,y))
        self.grid_list = grid_list

#Food类（食物豆类）
class Food(object):
    def __init__(self, Grid):
        self.grid = Grid
        self.color = "#23D978"                  #食物豆颜色
        self.set_pos()
    def set_pos(self):
        x = randint(0,self.grid.grid_x - 1)	#随机新的位置
        y = randint(0,self.grid.grid_y - 1)
        self.pos =  (x, y)    
    def display(self):				#显示豆
        self.grid.draw(self.pos,self.color)
        
# Snake（蛇类）
class Snake(object):
    #构造函数__init__(self, Grid)根据游戏开始时蛇运动的默认方向（向上）和给定的参数，确定组成蛇的初始有5“块”的位置坐标
    def __init__(self, Grid):			#构造函数
        self.grid = Grid
        self.body = [(10,6),(10,7),(10,8) ,(10,9),(10,10)]#蛇身初始有5“块”（或称节）
        self.direction = "Up"			#运动方向
        self.status = ['run','stop']		#游戏状态——运行或暂停（结束）
        self.speed = 300			#速度（每0.3秒移动一次）
        self.color = "#5FA8D9"        
        self.gameover = False
        self.hit = False                	#是否吃到豆
    def available_grid(self): 			#计算蛇身有效位置，可以有来判断出界和碰到自身
        return [i for i in self.grid.grid_list if i not in self.body[1:]]
    def change_direction(self, direction):	#转向
        self.direction = direction
    def display(self):				#显示蛇
        for (x,y) in self.body:
            self.grid.draw((x,y),self.color)

    #move(self, food) 采用“添头去尾”方式实现蛇的移动。
    def move(self, food):			#蛇的移动
        head = self.body[0]
        if self.direction == 'Up':		#向上
            new = (head[0], head[1]-1)
        elif self.direction == 'Down':		#向下
            new = (head[0], head[1]+1)
        elif self.direction == 'Left':		#向左
            new = (head[0]-1,head[1])
        else:
            new = (head[0]+1,head[1])		#向右
            
        if not food.pos == head:  		#没吃到食物豆
            pop = self.body.pop()		#去掉蛇尾（删最后一个元素)
            self.grid.draw(pop,self.grid.bg)
        else:					#吃到食物豆
            self.hit = True
        self.body.insert(0,new)      		#添到蛇身中[(10,6),(10,7),(10,8) ,(10,9),(10,10)]
        if not new in self.available_grid():	#计算蛇身不在有效位置，即出界或碰到自身
            self.status.reverse() 		#游戏状态反转，即运行或暂停（结束）反转
            self.gameover = True		#游戏结束标志
        else:
            self.grid.draw(new,color=self.color)#绘制新块
#SnakeGame（游戏逻辑类）
#该类的功能是依次显示场地内的所有对象，包括场地、食物豆和蛇           
class SnakeGame(Frame):        #Frame显示出来是矩形区域
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.score = 0
        self.master = master
        self.grid = Grid(master=master)
        self.snake = Snake(self.grid)
        self.food = Food(self.grid)
        self.display_food()
        self.bind_all("<KeyRelease>", self.key_release)
        self.snake.display()

    def display_food(self):
        while(self.food.pos in self.snake.body):
            self.food.set_pos()
        self.food.display()
    def run(self):
        if not self.snake.status[0] == 'stop':
            self.snake.move(self.food)
            if self.snake.hit == True:      	#吃到食物豆
                self.display_food()         	#重新产生位置
                self.score += 1
                self.snake.hit = False      	#恢复没吃到豆
            
        if self.snake.gameover == True:
            #messagebox.showinfo("Game Over", "your score: %d" % self.score)
            message = showinfo("Game Over", "your score: %d" % self.score)
            print(message)
            if message == 'ok':
                sys.exit()
        self.after(self.snake.speed,self.run)
    def key_release(self, event):
        key = event.keysym			#获取按键的键值
        key_dict = {"Up":"Down","Down":"Up","Left":"Right","Right":"Left"}
        #根据当前蛇的运行方向和传递来的参数来设置蛇的新运动方向  
        #蛇不可以向自己的反方向走
        if key in key_dict.keys() and not key == key_dict[self.snake.direction]:
            self.snake.change_direction(key)
            self.snake.move(self.food)
        elif key == 'p' or key == 'space':
            self.snake.status.reverse()
            
#以下是主程序
if __name__ == '__main__':
    root = Tk()
    root.title(" 贪吃蛇 ") 
    snakegame = SnakeGame(root)
    snakegame.run()
    snakegame.mainloop() 





