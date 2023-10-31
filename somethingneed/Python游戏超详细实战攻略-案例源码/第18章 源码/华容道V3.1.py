from tkinter import *
from tkinter.messagebox import *
#One表示小正方形，TwoH表示横长方形，TwoV表示竖长方形，Four表示大正方形
One=1
TwoH=2
TwoV=3
Four=4
#---------------------点类Point比较简单，主要存储方块所在棋盘坐标（X,Y）。
class Point:     #点类
     def __init__(self,x,y):
        self.X=x
        self.Y=y
        
#----------------------Block类
''' 
    块类
''' 
class Block(Button):   #块类  
  
    '''构造函数创建一个块，一旦确定方块类型和左上角的坐标后，就可以确定一个块了。
      <param name="p">左上角位置</param>
      <param name="blockType">块类型</param>
    '''
    def __init__(self,p,blockType,master,r,bm):
        Button.__init__(self,master)
        self.Location=p
        self.BType=blockType
        self["text"]=r
        self["image"]=bm
        self.bind("<ButtonPress>",btn_MouseDown);
        self.bind("<ButtonRelease>",btn_Realse);
        #self.bind("<ButtonPress>",btn_MouseDown);
        self.place(x=self.Location.X*80,y=self.Location.Y*80)
    '''
      GetPoints()方法获取块中所有点
      GetPoints()方法返回一个该方块所占据的所有坐标位置的集合。
      通过方块类型和左上角的坐标就可以确定一个方块所占据的所有坐标位置。
    '''
    def  GetPoints(self):
      pList = []
      if self.BType==One :
          pList.append(self.Location)
      elif  self.BType == TwoH :
          pList.append(self.Location);
          pList.append(Point(self.Location.X + 1, self.Location.Y))
      elif  self.BType == TwoV :
          pList.append(self.Location) 
          pList.append( Point(self.Location.X, self.Location.Y + 1)) 
      elif  self.BType == Four :
          pList.append(self.Location) 
          pList.append( Point(self.Location.X + 1, self.Location.Y)) 
          pList.append( Point(self.Location.X, self.Location.Y + 1)) 
          pList.append( Point(self.Location.X + 1, self.Location.Y + 1))
      return pList;

    '''块中是否包含某个点
    <param name="point">点</param>
    <returns>是否包含</returns>
    '''
    def Contains(self,point):
      pList=self.GetPoints() 
      for i in range(len(pList)):
          if  pList[i].x==point.x and pList[i].y==point.y :
              return True  
      return False
    '''是否和另一个块交叉
     <param name="block">另一个块</param>
     '''
    def Intersects(self,block):
        myPoints = self.GetPoints()          #List<Point>

        otherPoints = block.GetPoints()      #List<Point>

        for i in range(len(otherPoints)):    #foreach (Point p in otherPoints)
             p=otherPoints[i]
             for j in range(len(myPoints)):   #if  p in myPoints:
                if  p.X==myPoints[j].X and p.Y==myPoints[j].Y:    
                    return True
        return False


    def IsValid(self, width, height):#块是否在界限内
        points = self.GetPoints() 
        for i in range(len(points)):
            p=points[i]
            if (p.X < 0 or p.X >= width or p.Y < 0 or p.Y >= height):
                return False;
        return True;
#----------------------游戏控制类Game
class Game( ):   #游戏控制类
    #在华容道中宽度为4各，高度为5格
    Width = 4
    Height = 5
    WinFlag=False
    #Game类中包含一个块的集合，表示游戏中所有的方块：
    Blocks =[]
    #表示结束点（即要移出的方块左上角坐标最终要到达的位置）的属性
    finishPoint =Point(1, 3) 
    #Game类的GetBlockByPos方法获取p位置方块
    def GetBlockByPos(self, p ):
        for i in range(len(self.Blocks)): 
            if (self.Blocks[i].Location.X==p.X and self.Blocks[i].Location.Y==p.Y):
                return self.Blocks[i]
        return False
    #Game类的AddBlock方法和RemoveBlock方法用于向集合中添加和移除方块，可用于编辑游戏
    def AddBlock(self,block):
        if block in self.Blocks:
            return False
        if not block.IsValid(self.Width,self.Height):
            return False
        for i in range(len(self.Blocks)): 
            if (self.Blocks[i].Intersects(block)):
                return False
        self.Blocks.append(block)
        return True
    #Game类最重要的是移动方块的方法MoveBlock：
    def  MoveBlock(self,block, direction):
        if   block not in self.Blocks:
           print("非此游戏中的块！")
           return
        oldx = block.Location.X       #记录原来位置
        oldy = block.Location.Y
        
        #试移动
        if direction=="Up" :
            block.Location.Y -=1 
        elif  direction=="Down":
            block.Location.Y +=1 
        elif  direction=="Left":
            block.Location.X -=1
        elif  direction=="Right":
            block.Location.X +=1
        #判断是否需要回滚
        moveOK = True;                     #可以移动
        if ( not block.IsValid(self.Width,self.Height)):
            moveOK = False
        else:
            for i in range(len(self.Blocks)):  #foreach (Block b in self.Blocks)
                if (block is not self.Blocks[i] and block.Intersects(self.Blocks[i])):
                    moveOK = False;
                    break;
        if not moveOK  :
            print("不能移动！！！！！！！！")
            print(block.Location.X,block.Location.Y)
            block.Location = Point(oldx,oldy)   #恢复到原来位置
            print(block.Location.X,block.Location.Y) 
        if moveOK==True :
            print (block["text"],block.Location.X,block.Location.Y)
            if  block["text"]=="曹操" and block.Location.X==1 and block.Location.Y==3:
                self.WinFlag=True
        return moveOK
    def  GameWin(self):
          if self.WinFlag==True:
             return True
          else:
             return False

                    
oldx=0
oldy=0
BlockSize = 80             #游戏中块的显示大小
mouseDownPoint=Point(0,0)  #鼠标按下的位置
mouseDown=False            #标记鼠标是否按下


def CallBack():
   showinfo(title='',message='点我干嘛')
def btn_MouseDown(event):
   global mouseDownPoint,mouseDown
   mouseDownPoint = Point(event.x,event.y)
   mouseDown = True
   #event.x x轴坐标  event.y y轴坐标
   print(event.x,event.y)
   oldx=event.x
   oldy=event.y
   #print(b2["x"])
   #print(b2.place_info())#{'in': <tkinter.Tk object .>, 'relwidth': '', 'height': '32', 'anchor': 'nw', 'bordermode': 'inside', 'width': '32', 'y': '100', 'rely': '0', 'relheight': '', 'x': '100', 'relx': '0'}
   x= b2.place_info()["x"]
   print (x)
##def Move1(event):
##   #event.x x轴坐标  event.y y轴坐标
##   print(event.x,event.y)
   
def btn_Realse(event):
    global mouseDownPoint,mouseDown
    print(event.x,event.y)
    if  not mouseDown:
       return
    #Button btn = (Button)sender;
    #Block block = (Block)(btn.Tag);
    moveH = event.x - mouseDownPoint.X;
    moveV = event.y - mouseDownPoint.Y;
    x=int(event.widget.place_info()["x"])//80
    y=int(event.widget.place_info()["y"])//80
    block=game.GetBlockByPos(Point(x,y))    
    if (moveH >= BlockSize * 1 / 3):
        game.MoveBlock(block, "Right")
    elif (moveH <= -BlockSize * 1 / 3):
        game.MoveBlock(block, "Left")
    elif (moveV >= BlockSize * 1 / 3):
        game.MoveBlock(block, "Down")
    elif (moveV <= -BlockSize * 1 / 3):
        game.MoveBlock(block, "Up")
    else :
        return
    event.widget.place(x=block.Location.X*80,y=block.Location.Y*80) 
    #UpdateButtonLocation(btn);
    if (game.GameWin()):
        print("游戏胜利！") 
    mouseDown = False
    #b2.place(x=100+event.x-oldx,y=100+event.y-oldy,height=32,width=32)

   
win = Tk();#创建窗口对象
win.title("华容道游戏")#设置窗口标题
win.geometry("320x400")

game=Game()
bm = [PhotoImage(file = 'bmp\\曹操.gif'),
      PhotoImage(file = 'bmp\\关羽.gif'),
      PhotoImage(file = 'bmp\\黄忠.gif'),
      PhotoImage(file = 'bmp\\马超.gif'),
      PhotoImage(file = 'bmp\\张飞.gif'),
      PhotoImage(file = 'bmp\\赵云.gif'),
      PhotoImage(file = 'bmp\\兵.gif')]
#bm2 = PhotoImage(file = 'bmp\\worker.gif')
b0=Block(Point(1,0),Four ,win,"曹操",bm[0])
b1=Block(Point(1,2),TwoH ,win,"关羽",bm[1])
b2=Block(Point(3,2),TwoV ,win,"黄忠",bm[2])
b3=Block(Point(0,0),TwoV ,win,"马超",bm[3])
b4=Block(Point(0,2),TwoV ,win,"张飞",bm[4])
b5=Block(Point(3,0),TwoV ,win,"赵云",bm[5])
b6=Block(Point(0,4),One ,win,"兵",bm[6])
b7=Block(Point(1,3),One ,win,"兵",bm[6])
b8=Block(Point(2,3),One ,win,"兵",bm[6])
b9=Block(Point(3,4),One,win,"兵",bm[6])
game.AddBlock(b0);
game.AddBlock(b1);
game.AddBlock(b2);
game.AddBlock(b3);
game.AddBlock(b4);
game.AddBlock(b5);
game.AddBlock(b6);
game.AddBlock(b7);
game.AddBlock(b8);
game.AddBlock(b9);
win.mainloop();
