from tkinter import *
from tkinter.messagebox import *
One=1
TwoH=2
TwoV=3
Four=4
class Point:     #点类
     def __init__(self,x,y):
        self.X=x
        self.Y=y  
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
        print(p)
        self.BType=blockType
        self["text"]=r
        self["image"]=bm
        self.bind("<ButtonPress>",btn_MouseDown);
        #self.place(x=p.X*50,y=p.Y*50,height=32,width=32)
        self.place(x=p.X*110,y=p.Y*110)
def CallBack():
   showinfo(title='',message='点我干嘛')
def btn_MouseDown(event):
   showinfo(title='',message='MouseDown')
   event.widget["image"]=bm2
   event.widget.place(x=0,y=120)


 
win = Tk();#创建窗口对象
win.title("使用Button组件的简单例子")#设置窗口标题
win.geometry("440x550")
bm = PhotoImage(file = 'D:\\python\\bmp\\worker.gif')
b = Button (win,text = '点我啊', command=CallBack,image = bm)#创建Button组件
b.bm = bm
b.place(x=0,y=100,height=32,width=32)
bm = PhotoImage(file = 'D:\\python\\bmp\\worker.gif')
bm2 = PhotoImage(file = 'D:\\python\\bmp\\曹操.png')
b2 = Button (win,text = '点我啊', command=CallBack,image = bm)#创建Button组件
#b2.bm = bm
b2.place(x=100,y=100,height=32,width=32)
#b.pack()#显示Button组件
print (Button().keys())#获得以下按钮属性['activebackground', 'activeforeground', 'anchor', 'background', 'bd', 'bg', 'bitmap', 'borderwidth', 'command', 'compound', 'cursor', 'default', 'disabledforeground', 'fg', 'font', 'foreground', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'image', 'justify', 'overrelief', 'padx', 'pady', 'relief', 'repeatdelay', 'repeatinterval', 'state', 'takefocus', 'text', 'textvariable', 'underline', 'width', 'wraplength']
b2.bind("<ButtonPress>",btn_MouseDown);

#b=Block(1,1,win,"aaa",bm)
#b["image"]=bm
#b.place(x=150,y=100,height=32,width=32)
bm = [PhotoImage(file = 'D:\\python\\bmp\\曹操.png'),
      PhotoImage(file = 'D:\\python\\bmp\\关羽.png'),
      PhotoImage(file = 'D:\\python\\bmp\\黄忠.png'),
      PhotoImage(file = 'D:\\python\\bmp\\马超.png'),
      PhotoImage(file = 'D:\\python\\bmp\\张飞.png'),
      PhotoImage(file = 'D:\\python\\bmp\\赵云.png'),
      PhotoImage(file = 'D:\\python\\bmp\\兵.png')]
bm2 = PhotoImage(file = 'D:\\python\\bmp\\worker.gif')
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
win.mainloop();
