from tkinter import *
#2016-2-20  4小时 完后界面，走棋规则判断
#2016-2-21  上午1.5小时 完成判断选择棋子，选中标记显示
root = Tk()
# 创建一个Canvas，设置其背景色为白色 
cv = Canvas(root, bg = 'white', width = 720, height = 800)
chessname=["黑车","黑马","黑象","黑仕","黑将","黑仕","黑象","黑马","黑车","黑卒","黑炮",
           "红车","红马","红相","红仕","红帅","红仕","红相","红马","红车","红兵","红炮"]
imgs= [PhotoImage(file='D:\\python\\我的书稿案例--2016年计划\\第6章 中国象棋\\bmp\\'+chessname[i]+'.png')for i in range(0,22) ]
img1=PhotoImage(file='D:\\python\\我的书稿案例--2016年计划\\第6章 中国象棋\\bmp\\棋盘.png')
BlackPlayer=[]
RedPlayer=[]
map1=[]
chessmap =  [[" "," "," "," "," "," "," "," "," "," "]for y in range(10)]
#定义一个字典
dict_ChessName={}
#画棋盘
p1=cv.create_image((0,0),image=img1)
cv.coords(p1,(360,400))
selectedChessFlag=cv.create_rectangle(0,0,80,80,outline="red")
targetPosFlag=cv.create_rectangle(0,0,80,80,outline="yellow")
LocalPlayer="红"
first=True    #第一次选中的棋子
IsMyTurn = True
rect1=0
rect2=0
def IsAbleToPut(id, x, y,oldx,oldy):# 实现判断是否能走棋返回逻辑值，这代码最复杂。
    # oldx, oldy 棋子在棋盘原坐标          
    # x, y       棋子移动到棋盘的新坐标 
    qi_name = dict_ChessName[id][1]  #取字符串第二个字符，"黑将"变成"将"
    #"将" "帅"走棋判断
    if (qi_name == "将" or qi_name == "帅"):
        if ((x - oldx) * (y - oldy) != 0):
            return False;
        if (abs(x - oldx) > 1 or abs(y - oldy) > 1):
            return False;
        if (x < 3 or x > 5 or (y >= 3 and y <=6)):
            return False;
        return True;


    #"士"走棋判断
    if (qi_name == "士" or qi_name == "仕"):
        if ((x - oldx) * (y - oldy) == 0):
            return False;
        if (abs(x - oldx) > 1 or abs(y - oldy) > 1):
            return False;
        if (x < 3 or x > 5 or (y >= 3 and y <=6)):
            return False;
        return True;
    
    #"象"走棋判断
    if (qi_name == "象" or qi_name == "相"):
        if ((x - oldx) * (y - oldy) == 0):
            return False;
        if (abs(x - oldx) != 2 or abs(y - oldy) != 2):
            return False;
        if (y < 5 and qi_name == "相" ):#过河
            return False;
        if (y >= 5 and qi_name == "象" ):#过河
            return False;
        i = 0; j = 0;#i,j必须有初始值
        if (x - oldx == 2):
            i = x - 1;
        if (x - oldx == -2):
            i = x + 1;
        if (y - oldy == 2):
            j = y - 1;
        if (y - oldy == -2):
            j = y + 1;
        if (chessmap[i][j] != -1):
           return False;
        return True;

    #"马"走棋判断
    if (qi_name == "马" or qi_name == "马"):
        if (abs(x - oldx) * abs(y - oldy) != 2):
            return False;
        if (x - oldx == 2): 
            if (chessmap[x - 1][oldy] != -1):
                return False;
        if (x - oldx == -2):
            if (chessmap[x + 1][oldy] != -1):
                return False;
        if (y - oldy == 2):
            if (chessmap[oldx][y - 1] != -1):
                return False;
        if (y - oldy == -2):
            if (chessmap[oldx][y + 1] != -1):
                return False;
        return True;

    #"车"走棋判断                
    if (qi_name == "车" or qi_name == "车"):
        #判断是否直线
        if ((x - oldx) * (y - oldy) != 0):
           return False;
        #判断是否隔有棋子
        if (x != oldx):
            if (oldx > x):
                t = x;
                x = oldx;
                oldx = t; 
            for  i in range(oldx,x+1):
                if (i != x and i != oldx):
                    if (chessmap[i][y] != -1):
                        return False;
        if (y != oldy):
            if (oldy > y):
                t = y;
                y = oldy;
                oldy = t; 
            for  j in range(oldy,y+1): 
                if (j != y and j != oldy):
                    if (chessmap[x][j] != -1):
                        return False;
        return True;

    # "炮"走棋判断
    if (qi_name == "炮" or qi_name == "炮"):
        swapflagx = False;
        swapflagy = False;
        if ((x - oldx) * (y - oldy) != 0):
            return False;
        c = 0;
        if (x != oldx):
            if (oldx > x):
               t = x;
               x = oldx;
               oldx = t;
               swapflagx = True; 
            for  i in range(oldx,x+1): #for (i = oldx; i <= x; i += 1):
                if (i != x and i != oldx):
                    if (chessmap[i][y] != -1):
                        c = c + 1;

        if (y != oldy):
            if (oldy > y):
               t = y;
               y = oldy;
               oldy = t;
               swapflagy = True;                       
            for  j in range(oldy,y+1):#for (j = oldy; j <= y; j += 1):
                if (j != y and j != oldy):
                    if (chessmap[x][j] != -1):
                        c = c + 1;

        if (c > 1):
           return False; #与目标处间隔1个以上棋子
        if (c == 0): #与目标处无间隔棋子
            if (swapflagx == True):
               t = x;
               x = oldx;
               oldx = t;
            if (swapflagy == True):
               t = y;
               y = oldy;
               oldy = t;                
            if (chessmap[x][y] != -1):
                return False;
        if (c == 1):#与目标处间隔1个棋子
            if (swapflagx == True):
               t = x;
               x = oldx;
               oldx = t;
            if (swapflagy == True):
               t = y;
               y = oldy;
               oldy = t; 
            if ( chessmap[x][y] == -1):#如果目标处无棋子，则不能走此步
                return False;
        return True;
        
    # "卒" "兵"走棋判断
    if (qi_name == "卒" or qi_name == "兵"):
        if ((x - oldx) * (y - oldy) != 0):
            return False;
        if (abs(x - oldx) > 1 or abs(y - oldy) > 1):
            return False;
        if (y >= 5 and (x - oldx) != 0 and qi_name == "兵"):
            return False;
        if (y < 5 and (x - oldx) != 0 and qi_name == "卒"):
            return False;
        if (y - oldy > 0 and qi_name == "兵"):
            return False;
        if (y - oldy < 0 and qi_name == "卒"):
            return False;
        return True;
    return True;
#——————————————————————
#——————————————————————
def callback(event):#走棋
    global LocalPlayer
    global chessmap,rect1,rect2
    print ("clicked at", event.x, event.y,LocalPlayer)
    x=(event.x-14)//76  #换算棋盘坐标
    y=(event.y-14)//76
    id=chessmap[x][y]
    if(rect1!=0):
        cv.delete(rect1);#删除原来的选中标记
    rect1=cv.create_rectangle(60+76*x-40,54+y*76-38,60+76*x+80-40,54+y*76+80-38,outline="red")
    #cv.scale(id,0,0,1.5,1.5)
    print ("clicked at", x, y,LocalPlayer)
    print ("clicked at", x, y,id)
    x1=x+1
    y1=y+1
    #判断是否可以走棋
    if IsAbleToPut(id,x1,y1, x, y)==True:
         print ("can",x1,y1)
         cv.move(id,76,76);
         chessmap[x][y]=-1;
         chessmap[x1][y1]=id
    print (dict_ChessName[id])
    
    
    
    for  y in range(0,10):
        for x in range(0,9) :
            print (chessmap[x][y],end=",")
        print ("---")

#——————————————————————        
def LoadChess():        #加载棋子
    global chessmap
    #黑方16个棋子
    for i in range(0,9):
       img=imgs[i]
       id=cv.create_image((60+76*i,54),image=img)#76*76棋盘格子大小

       dict_ChessName[id]=chessname[i];  #图像对应的是那种棋子
       map1.append((i,0))                   #记录棋子x,y棋盘坐标
       chessmap[i][0]=id                    #图像id
       BlackPlayer.append(id);
    for i in range(0,5):
       img=imgs[9]          #卒
       id=cv.create_image((60+76*2*i,54+3*76),image=img)#76*76棋盘格子大小
       chessmap[i*2][3]=id
       dict_ChessName[id]="黑卒";  #图像对应的是那种棋子

       map1.append((i*2,3))
       BlackPlayer.append(id);
    img=imgs[10]         #黑方炮
    id=cv.create_image((60+76*1,54+2*76),image=img)#76*76棋盘格子大小
    chessmap[1][2]=id
    dict_ChessName[id]="黑炮";  #图像对应的是那种棋子
    map1.append((1,2))
    BlackPlayer.append(id);
    id=cv.create_image((60+76*7,54+2*76),image=img)#76*76棋盘格子大小
    chessmap[7][2]=id
    dict_ChessName[id]="黑炮";  #图像对应的是那种棋子
    map1.append((1,3))
    BlackPlayer.append(id);
    #红方16个棋子
    for i in range(0,9):
       img=imgs[i+11]
       id=cv.create_image((60+76*i,54+9*76),image=img)#76*76棋盘格子大小
     
       dict_ChessName[id]=chessname[i+11];  #图像对应的是那种棋子
       map1.append((i,9))                   #记录棋子x,y棋盘坐标
       chessmap[i][9]=id                    #图像id
       RedPlayer.append(id);
    for i in range(0,5):
       img=imgs[20]          #兵
       id=cv.create_image((60+76*2*i,54+6*76),image=img)#76*76棋盘格子大小
       chessmap[i*2][6]=id                    #图像id
       dict_ChessName[id]=chessname[20];  #图像对应的是那种棋子
       map1.append((i*2,6))
       RedPlayer.append(id);
    img=imgs[21]         #红方炮
    id=cv.create_image((60+76*1,54+7*76),image=img)#76*76棋盘格子大小
    chessmap[1][7]=id
    dict_ChessName[id]="红炮";  #图像对应的是那种棋子
    map1.append((1,7))
    BlackPlayer.append(id);
    id=cv.create_image((60+76*7,54+7*76),image=img)#76*76棋盘格子大小
    chessmap[7][7]=id
    dict_ChessName[id]="红炮";  #图像对应的是那种棋子
    map1.append((7,7))
#——————————————————————

LoadChess()
for  y in range(0,10):
    for x in range(0,9) :
        print (chessmap[x][y],end=",")
    print ("---")
#print (BlackPlayer)
#print (map1)
print(dict_ChessName)
if  not (0,0) in map1:
   print ("not exist")
else:
   print (" exist") 
cv.bind("<Button-1>", callback)
cv.pack()
root.mainloop() 

