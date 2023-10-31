import random
from tkinter import *
from tkinter.messagebox import *
#本文实例借鉴mvc模式，核心数据为model，维护1个矩阵，0表无雷，1表雷。

#设计数据类Model
class Model:
  """
  核心数据类，维护一个矩阵
  """
  def __init__(self,row,col):
    self.width=col
    self.height=row
    #self.items游戏地图
    #主要存储所有方块所在（r,c）位置的雷信息，有雷为1，无雷为0。
    self.items=[[0 for c in range(col)] for r in range(row)]  #所有方块初始为无雷
               # [0,0,0,0,0,0,0,0,1,0]
  def setItemValue(self,r,c,value):
    """
    设置某个位置的值为value
    """
    self.items[r][c]=value;
 
  def checkValue(self,r,c,value):
    """
    检测某个位置的值是否为value
    """
    if  self.items[r][c]==value :      
      return True
    else:
      return False
     
  def countValue(self,r,c,value):
    """
    统计某个位置周围8个位置中，值为value的个数
    """
    count=0
    if r-1>=0 and c-1>=0:
      if self.items[r-1][c-1]==1:count+=1
    if r-1>=0 and c>=0:
      if self.items[r-1][c]==1:count+=1
    if r-1>=0 and c+1<=self.width-1:
      if self.items[r-1][c+1]==1:count+=1
    if c-1>=0:
      if self.items[r][c-1]==1:count+=1
    if c+1<=self.width-1 :
      if self.items[r][c+1]==1:count+=1
    if r+1<=self.height-1 and c-1>=0:
      if self.items[r+1][c-1]==1:count+=1
    if r+1<=self.height-1 :
      if self.items[r+1][c]==1:count+=1
    if r+1<=self.height-1 and c+1<=self.width-1:
      if self.items[r+1][c+1]==1:count+=1
    return count
 
#设计Mines类
#继承Frame的Mines类，实现显示游戏方块，无雷的方块区域拓展。完成标记地雷和输赢判断功能。
class Mines(Frame):
  def __init__(self,m,master=None):
    Frame.__init__(self,master)
    self.model=m
    self.initmine()     #布雷
    self.grid()         #表格布局
    self.createWidgets()#表格布局中添加按钮组件,产生model.width* model.height个按钮组件
 
  
   
  def createWidgets(self):
    self.rowconfigure(self.model.height,weight=1)
    self.columnconfigure(self.model.width,weight=1)
    self.buttongroups=[[Button(self,height=1,width=2) for i in range(self.model.width)]
              for j in range(self.model.height)]
    for r in range(self.model.height):
      for c in range(self.model.width):
        #button放置到r行c列，sticky=(W,E,N,S)填满整个单元格
        self.buttongroups[r][c].grid(row=r,column=c,sticky=(W,E,N,S))
        self.buttongroups[r][c].bind('<Button-1>',self.clickevent) #左键事件
        self.buttongroups[r][c].bind('<Button-3>',self.Rightclickevent) #右键事件
        self.buttongroups[r][c]['padx']=r   #记录行列号
        self.buttongroups[r][c]['pady']=c
 

 
  def recureshow(self,r,c):
    if 0<=r<=self.model.height-1 and 0<=c<=self.model.width-1:
      if model.checkValue(r,c,0) and self.buttongroups[r][c]['state']==NORMAL and model.countValue(r,c,1)==0:#本身不是雷且周围雷数是零
        self.buttongroups[r][c]['state']=DISABLED #无效按钮
        self.buttongroups[r][c]['bd']=4           #边框为4个像素
        self.buttongroups[r][c]['disabledforeground']='red'       #前景色为红色
        self.buttongroups[r][c]['text']='0'
        #递归翻开周围8个button
        self.recureshow(r-1,c-1)
        self.recureshow(r-1,c)
        self.recureshow(r-1,c+1)
        self.recureshow(r,c-1)
        self.recureshow(r,c+1)
        self.recureshow(r+1,c-1)
        self.recureshow(r+1,c)
        self.recureshow(r+1,c+1)
      elif model.countValue(r,c,1)!=0:#仅仅本身翻开
        self.buttongroups[r][c]['text']=model.countValue(r,c,1)
        self.buttongroups[r][c]['state']=DISABLED
        self.buttongroups[r][c]['bd']=4           #边框为4个像素
        self.buttongroups[r][c]['disabledforeground']='red'       #前景色为红色
    else:
      pass
    
  #showall(self)函数将地图中所有雷标识出来。  
  def showall(self):
    for r in range(model.height):
      for c in range(model.width):
        self.showone(r,c)
 
  def showone(self,r,c):
    if model.checkValue(r,c,0):
      self.buttongroups[r][c]['text']=model.countValue(r,c,1)
    else:
      self.buttongroups[r][c]['text']='Q'
      self.buttongroups[r][c]['image']=mineImage          
       
  def clickevent(self,event):
    """
    单击事件
    case 1:是雷，所有都显示出来，游戏结束
    case 2:是周围雷数为0的，递归触发周围8个button
    case 3:周围雷数不为0的，显示周围雷数
    """
    r=int(str(event.widget['padx']))
    c=int(str(event.widget['pady']))
    if model.checkValue(r,c,1):#是雷
      self.showall()       #是雷，所有都显示出来，游戏结束
      showinfo(title="提示",message="你挑战失败了")
    else:#不是雷
      self.recureshow(r,c) #递归翻开周围雷数是零的方块按钮
      if(self.Victory()):       # 检测是否胜利
         showinfo(title="提示",message="你赢了")
    
      
  def Rightclickevent(self,event):
    """
    右键单击事件

    """
    r=int(str(event.widget['padx']))
    c=int(str(event.widget['pady']))
    if(self.buttongroups[r][c]['text']=="X"):#已标记，则取消标记
        self.buttongroups[r][c]['image']=askImage  #变成问号
        self.buttongroups[r][c]['text']=""
    else:
        self.buttongroups[r][c]['image']=flagImage  #自己标记是雷，显示旗帜图形
        self.buttongroups[r][c]['text']="X"
    
    if(self.Victory()):        # 检测是否胜利
       showinfo(title="提示",message="你赢了")
    
  #Victory()实现胜利判断并处理。
  def Victory(self):# 检测是否胜利
    for r in range(model.height):
       for c in range(model.width):
          #没翻开且未标示旗帜,则未成功
          if (self.buttongroups[r][c]['state']==NORMAL and self.buttongroups[r][c]['text']!="X"):
             return False
          #不是雷却误标示为雷,则也未成功
          if (model.checkValue(r,c,0) and self.buttongroups[r][c]['text']=="X"):
             return False          
    return True     
      
  def initmine(self):
    """
    埋雷,每行埋height/width+1个暂定
    """
    n=random.randint(1,int(model.height/model.width)+1)
    for r in range(model.height):
      for i in range(n):
        rancol=random.randint(0,model.width-1)
        model.setItemValue(r,rancol,1)
 
   
  def printf(self):
    """
    打印
    """
    print ('地图')
    for r in range(model.height):
      for c in range(model.width):
        print (model.items[r][c],end=" ")
      print ('')
    
#——————————————————————————      

def new():
  """
  重新开始游戏
  
  """
  global m
  m.grid_remove()
  global model
  model=Model(10,10)
  m=Mines(model,root)
  m.printf()
  pass
#—————————————————————————— 

 
if __name__=='__main__':
  model=Model(10,10)
  root=Tk()
  mineImage=PhotoImage(file='.\\mine.gif')
  flagImage=PhotoImage(file='.\\flag.gif')
  askImage=PhotoImage(file='.\\ask.gif') 
  #menu
  menu = Menu(root)
  root.config(menu=menu)
  filemenu = Menu(menu)
  menu.add_cascade(label="File", menu=filemenu)
  filemenu.add_command(label="New",command=new)
  filemenu.add_separator()
  filemenu.add_command(label="Exit", command=root.destroy)
 
  #Mines
  m=Mines(model,root)  #实现显示游戏方块
  m.printf()           #打印游戏地图，主要用于测试
  root.mainloop()
