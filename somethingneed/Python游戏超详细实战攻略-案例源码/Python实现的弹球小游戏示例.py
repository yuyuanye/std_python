from tkinter import *
import random
import time
class Ball:
  def __init__(self, canvas, paddle, color):
    self.canvas = canvas
    self.paddle = paddle
    self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
    self.canvas.move(self.id, 245, 100)
    startx = [-3, -2, -1, 1, 2, 3]
    random.shuffle(startx)
    self.x = startx[0]
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()
    self.hit_bottom = False
  def draw(self):
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)#top-left bottom-right
    if (pos[1] <= 0 or self.hit_paddle(pos) == True):
      self.y = -self.y
    if (pos[0] <= 0 or pos[2] >= self.canvas_width):
      self.x = -self.x
    if (pos[3] >= self.canvas_height):
      self.hit_bottom = True
  def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)
    if (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]):
      if (pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]):
        return True
    return False
class Paddle:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
    self.x = 0
    self.canvas.move(self.id, 200, 300)
    self.canvas_width = self.canvas.winfo_width()
    self.canvas.bind_all("<Key-Left>", self.turn_left)
    self.canvas.bind_all("<Key-Right>", self.turn_right)
    self.canvas.bind("<Button-1>", self.turn)   #鼠标单击事件
    self.canvas.bind("<B1-Motion>", self.turnmove)#鼠标拖动事件
    
  def draw(self):
    pos = self.canvas.coords(self.id)
    if (pos[0] + self.x >= 0 and pos[2] + self.x <= self.canvas_width):
      self.canvas.move(self.id, self.x, 0)
    #self.x = 0
  def turn_left(self, event):
    self.x = -4
  def turn_right(self, event):
    self.x = 4
  def turn(self, event):      #鼠标单击事件函数
    print ("clicked at", event.x, event.y)
    self.mousex=event.x
    self.mousey=event.y
  def turnmove(self, event):  #鼠标拖动事件函数
    #print ("现在为止", event.x, event.y)
    self.x =  event.x - self.mousex
    self.mousex=event.x
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)#not resizable
tk.wm_attributes("-topmost", 1)#at top
canvas = Canvas(tk, width = 500, height = 500, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update() 
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
while True:
  if (ball.hit_bottom == False):  #弹球是否碰到底部
    ball.draw()
    paddle.draw()
    tk.update()
    time.sleep(0.01)
  else:                           #游戏循环结束
     break  
