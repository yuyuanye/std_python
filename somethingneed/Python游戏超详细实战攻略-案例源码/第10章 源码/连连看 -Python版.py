from tkinter import *
from tkinter.messagebox import *
import string
import random
root = Tk()
root.title(" 第1章 python连连看 2016-2-23 晚上21:30---")

imgs= [PhotoImage(file='D:\\python\\我的书稿案例--2016年计划\\第1章 python连连看\\gif\\bar_0'+str(i)+'.gif') for i in range(0,10) ]

Select_first=False
firstSelectRectId=-1
SecondSelectRectId=-1
'''
判断选中的两个方块是否可以消除
'''
def IsLink(p1,p2): 
    if lineCheck(p1, p2):
        return True    
    if  secondLine(p1, p2):      #一个转弯（折点）的联通方式
        return True
    if  triLine(p1, p2):         #两个转弯（折点）的联通方式
        return True
    return False
#---------------------------
def IsSame(p1,p2):
     if map[p1.x][p1.y]==map[p2.x][p2.y]:
         print ("clicked at IsSame")
         return True
     return False

def callback(event):#走棋
    global Select_first,p1,p2
    global firstSelectRectId,SecondSelectRectId 
    #print ("clicked at", event.x, event.y,turn)
    x=(event.x)//40  #换算棋盘坐标
    y=(event.y)//40
    print ("clicked at", x, y)   
    if map[x][y]==" ":
       showinfo(title="提示",message="此处无方块")
    else:
       
       if Select_first==False:
            p1=Point(x,y)
            #画选定（x1,y1)处的框线
            firstSelectRectId=cv.create_rectangle(x*40,y*40,x*40+40,y*40+40,width=2,outline="blue")
            Select_first = True
       else:
            p2=Point(x,y)
            #判断第二次点击的方块是否已被第一次点击选取，如果是则返回。
            if (p1.x == p2.x) and (p1.y == p2.y):
                return
            #画选定（x2,y2)处的框线
            SecondSelectRectId=cv.create_rectangle(x*40,y*40,x*40+40,y*40+40,width=2,outline="yellow")

            #判断是否连通
            if IsSame(p1,p2) and IsLink(p1,p2):
                #画选中方块之间连接线 
                drawLinkLine(p1,p2)
                #延时0.5秒 
                 
                #清除第一个选定框线 
                cv.delete(firstSelectRectId)
                #清除第2个选定框线 
                cv.delete(SecondSelectRectId) 
                #清空记录方块的值
                map[p1.x][p1.y] = " "
                cv.delete(image_map[p1.x][p1.y])
                map[p2.x][p2.y] = " "
                cv.delete(image_map[p2.x][p2.y])
                Select_first = False
                
                undrawConnectLine()#清除选中方块之间连接线
                
                for y in range(0,Height):#0--14
                    for x in range(0,Width):#0--14
                        print (map[x][y],end=' ')
                    print(",",y)
            else:  #重新选定第一个方块  
                #清除第一个选定框线 
                cv.delete(firstSelectRectId)
                firstSelectRectId=SecondSelectRectId
                p1=Point(x,y)           #设置重新选定第一个方块的坐标
                Select_first = True
 


def drawQiPan( ):#画棋盘
    for i in range(0,15):
        cv.create_line(20,20+40*i,580,20+40*i,width=2)
    for i in range(0,15):
        cv.create_line(20+40*i,20,20+40*i,580,width=2)
    cv.pack()

    

def print_map( ):#输出map地图
    global image_map
    for x in range(0,Width):#0--14 
       for y in range(0,Height):#0--14
           if(map[x][y]!=' '):
               img1= imgs[int(map[x][y])]
               id=cv.create_image((x*40+20,y*40+20),image=img1)
               image_map[x][y]=id
    cv.pack()
    for y in range(0,Height):#0--14
        for x in range(0,Width):#0--14 
            print (map[x][y],end=' ')
        print(",",y)
'''
* 同行同列情况消除方法 原理：如果两个相同的被消除元素之间的 空格数
spaceCount等于他们的（行/列差-1）则 两者可以联通消除
* x代表行，y代表列
*@param p1 第一个保存上次选中点坐标的点对象
*@param p2 第二个保存上次选中点坐标的点对象
'''
class Point:
     #点类
     def __init__(self,x,y):
        self.x=x
        self.y=y
#--------------------------------------
#直接连通
def lineCheck(p1, p2):
    absDistance = 0 
    spaceCount = 0
    if (p1.x == p2.x or p1.y == p2.y) : # 同行同列的情况吗？
       print("同行同列的情况------")
       #同列的情况
       if (p1.x == p2.x and p1.y != p2.y) :
           print("同列的情况")
           #绝对距离(中间隔着的空格数)
           absDistance = abs(p1.y - p2.y) - 1
           #正负值
           if  p1.y - p2.y > 0 :
               zf=-1
           else:
               zf=1
           for i in range(1,absDistance+1):
               if (map[p1.x][p1.y + i * zf]==" "):
                   # 空格数加1
                   spaceCount += 1
               else:
                   break;#遇到阻碍就不用再探测了
            
       #同行的情况
       elif (p1.y == p2.y and p1.x != p2.x):
            print(" 同行的情况")
            absDistance = abs(p1.x - p2.x) - 1
            #正负值
            if  p1.x - p2.x > 0 :
               zf=-1
            else:
               zf=1
            for i in range(1,absDistance+1):
                if (map[p1.x + i * zf][p1.y]==" "):
                    # 空格数加1
                    spaceCount += 1
                else:
                    break;#遇到阻碍就不用再探测了
       if (spaceCount == absDistance) :
           #可联通
           print(absDistance,spaceCount)
           print("行/列可直接联通")
           return True
       else:
           print("行/列不能消除！")
           return False
    else:
       #不是同行同列的情况所以直接返回false
       return False; 
   
#--------------------------------------
#第二种，直角连通
'''
直角连接，即X,Y坐标都不同的，可以用这个方法尝试连接
@param first:选中的第一个点
@param second:选中的第二个点
'''
def secondLine(p1, p2):
    #第一个直角检查点，如果这里为空则赋予相同值供检查
    checkP = Point(p1.x, p2.y)
    #第二个直角检查点，如果这里为空则赋予相同值供检查
    checkP2 = Point(p2.x, p1.y);
    #第一个直角点检测
    if (map[checkP.x][checkP.y]==" "):
        if (lineCheck(p1, checkP) and lineCheck(checkP, p2)):
            linePointStack.append(checkP)
            print("直角消除ok",checkP.x,checkP.y)
            return True
    #第二个直角点检测
    if (map[checkP2.x][checkP2.y]==" "):
        if (lineCheck(p1, checkP2) and lineCheck(checkP2, p2)):
            linePointStack.append(checkP2)
            print("直角消除ok",checkP2.x,checkP2.y)
            return True
    print("不能直角消除" )
    return False;
#-----------------------------------------
'''
#第三种，双直角连通
双直角联通判定可分两步走：
1. 在p1点周围4个方向寻找空格checkP
2. 调用secondLine(checkP, p2)
3. 即遍历 p1 4 个方向的空格，使之成为 checkP,然后调用 secondLine(checkP, 
p2)判定是否为真，如果为真则可以双直角连同，否则当所有的空格都遍历完而没有找
到一个checkP使secondLine(checkP, p2)为真，则两点不能连同
具体代码：
'''
'''
两直角连接方法 以secendLine为基础
@param p1 第一个点
@param p2 第二个点
'''
def triLine(p1, p2):
    checkP = Point(p1.x, p1.y)
    #四向探测开始
    for i in range(0,4):
        checkP.x=p1.x
        checkP.y=p1.y
        # 向下
        if (i == 3):
           checkP.y+=1
           while (( checkP.y < Height) and  map[checkP.x][checkP.y]==" "):
               linePointStack.append(checkP)
               if (secondLine(checkP, p2)):
                  print("下探测OK")
                  return True
               else:
                  linePointStack.pop()
               checkP.y+=1
        # 向右
        elif (i == 2):
           checkP.x+=1
           while (( checkP.x < Width) and  map[checkP.x][checkP.y]==" "):
               linePointStack.append(checkP)
               if (secondLine(checkP, p2)):
                  print("右探测OK")
                  return True
               else:
                  linePointStack.pop()
               checkP.x+=1
        # 向左
        elif (i == 1):
           checkP.x-=1
           while (( checkP.x >=0) and  map[checkP.x][checkP.y]==" "):
               linePointStack.append(checkP)
               if (secondLine(checkP, p2)):
                  print("左探测OK")
                  return True
               else:
                  linePointStack.pop()
               checkP.x-=1
        # 向上
        elif (i == 0):
           checkP.y -=1 
           while ((checkP.y >=0) and  map[checkP.x][checkP.y]==" "):
               linePointStack.append(checkP)
               if (secondLine(checkP, p2)):
                  print("上探测OK")
                  return True
               else:
                  linePointStack.pop()
               checkP.y-=1
        
    #四个方向都寻完都没找到适合的checkP点
    print( "两直角连接没找到适合的checkP点")
    return False;


#---------------------------
#画连接线
def drawLinkLine(p1,p2):
    if ( len(linePointStack)==0 ):
        Line_id.append(drawLine(p1,p2))
    else:
        print(linePointStack,len(linePointStack))
    if ( len(linePointStack)==1 ):
        z=linePointStack.pop()
        print("一折连通点z",z.x,z.y)
        Line_id.append(drawLine(p1,z))
        Line_id.append(drawLine(p2,z))
    if ( len(linePointStack)==2 ):
        z1=linePointStack.pop()
        print("2折连通点z1",z1.x,z1.y)
        Line_id.append(drawLine(p2,z1))
        z2=linePointStack.pop()
        print("2折连通点z2",z2.x,z2.y)
        Line_id.append(drawLine(z1,z2)) 
        Line_id.append(drawLine(p1,z2))
#删除连接线 
def undrawConnectLine():    
    while len(Line_id)>0:
        idpop=Line_id.pop()
        cv.delete(idpop)
    
def  drawLine(p1,p2):
    print("drawLine p1,p2",p1.x,p1.y,p2.x,p2.y)
    #cv.create_line( 40+20, 40+20,200,200,width=5,fill='red')
    id=cv.create_line(p1.x*40+20,p1.y*40+20,p2.x*40+20,p2.y*40+20,width=5,fill='red')
    cv.pack()
    return id
#--------------------------------------
def create_map( ):#产生map地图
    global map
    #生成随机地图
    #将所有匹配成对的动物物种放进一个临时的地图中
    tmpMap = []
    m=(Width)*(Height)//10
    print('m=',m)
    for x in range(0,m):
       for i in range(0,10):
          tmpMap.append(x)
    random.shuffle(tmpMap)
    for x in range(0,Width):#0--14 
       for y in range(0,Height):#0--14
           map[x][y]=tmpMap[x*Height+y]
#--------------------------------------     

linePointStack=[]
Line_id=[]
Height=9
Width=10
map =  [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]for x in range(Width)]
image_map =  [[" " for y in range(Height)]for x in range(Width)]
cv = Canvas(root, bg = 'green', width = 610, height = 610)
#drawQiPan( )
cv.bind("<Button-1>", callback)
cv.pack()
create_map( ) #产生map地图
print_map( ) # 打印map地图
p1=Point(0,0)
p2=Point(1,2)

lineCheck(p1, p2)
secondLine(p1, p2)
triLine(p1, p2)
root.mainloop()
