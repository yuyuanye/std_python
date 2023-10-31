from tkinter import *

#2016-3-18 18：00-19：00  设计Card麻将牌类
import random
class huMain():

    def __init__(self):#构造函数
        #定义手中的牌int allPai[4][10]
        self.allPai = [[6,1,4,1,0,0,0,0,0,0], #桶
                       [3,1,1,1,0,0,0,0,0,0], #条
                       [0,0,0,0,0,0,0,0,0,0], #万
                       [5,2,3,0,0,0,0,0,0,0]] #字
        
        if  self.Win(self.allPai):
            print("Hu!\n")
        else:
            print("Not Hu!\n")
    #判断是否胡牌的函数
    def  Win(self,allPai):
        jiangPos=0	#“将”的位置
	#yuShu		#余数
        jiangExisted=False
	#第一步 是否满足3,3,3,3,2模型
        for i in range(0,4): 
            yuShu=allPai[i][0]%3 
            if  yuShu==1 :
     	       return False
            if  yuShu==2 :
     	       if  jiangExisted==True:
     	           return False
     	       jiangPos=i#“将”在那行
     	       jiangExisted=True

        #不含将处理
        for i in range(0,4):
            if  i!=jiangPos :
                if  not self.Analyze(allPai[i],i==3):
                    return False

        #该类牌中要包含将,因为要对将进行轮询,效率较低,放在最后
        success=False              #指示除掉“将”后能否通过
        for j in range(1,10):         #对列进行操作,用j表示
            if (allPai[jiangPos][j]>=2):
                #除去这2张将牌
                allPai[jiangPos][j]-=2
                allPai[jiangPos][0]-=2
                if self.Analyze(allPai[jiangPos],jiangPos==3) :
                        success=True
                #还原这2张将牌
                allPai[jiangPos][j]+=2
                allPai[jiangPos][0]+=2
                if success==True :
                    break               
        return success

    #分解成“刻”“顺”组合
    def  Analyze(self,aKindPai,ziPai):  #(int []aKindPai,Boolean ziPai)
        if aKindPai[0]==0 :
             return True
        #寻找第一张牌
        for j in range(1,10):
            if aKindPai[j]!=0:
               break
        if aKindPai[j]>=3:#作为刻牌
            #除去这3张刻牌
            aKindPai[j]-=3
            aKindPai[0]-=3
            result=self.Analyze(aKindPai,ziPai)
            #还原这3张刻牌
            aKindPai[j]+=3
            aKindPai[0]+=3
            return result
        #作为顺牌
        if  (not ziPai)and(j<8) and(aKindPai[j+1]>0) and(aKindPai[j+2]>0):
            #除去这3张顺牌
            aKindPai[j]-=1
            aKindPai[j+1]-=1
            aKindPai[j+2]-=1
            aKindPai[0]-=3
            result=self.Analyze(aKindPai,ziPai)
            #还原这3张顺牌
            aKindPai[j]+=1
            aKindPai[j+1]+=1
            aKindPai[j+2]+=1
            aKindPai[0]+=3
            return result

        return False
#----------------------------------class huMain() end

#是否可以碰牌15-8-1
def canPeng(a,card):  #(ArrayList a,Card card)
    n=0
    for i in range(0,len(a)):
        c=a[i]
        if (c.imageID ==card.imageID):
            n+=1
    if n>=2:
       return true
    return false

#是否可以吃牌15-8-1
def canChi(a,card): 
    n=0
    for i in range(0,len(a)-1):	#1**
        c1=a[i]
        c2=a[i+1]
        if(c1.m_nNum ==card.m_nNum+1 and c1.m_nType==card.m_nType
          and c2.m_nNum ==card.m_nNum+2 and c2.m_nType==card.m_nType):
            return True
    for i in range(0,len(a)-1):	#*1*
        c1=a[i]
        c2=a[i+1]		
        if(c1.m_nNum ==card.m_nNum-1 and c1.m_nType==card.m_nType
          and c2.m_nNum ==card.m_nNum+1 and c2.m_nType==card.m_nType):
            return True
    for i in range(0,len(a)-1):	#**1
        c1=a[i]
        c2=a[i+1]
        if(c1.m_nNum ==card.m_nNum-2 and c1.m_nType==card.m_nType
          and c2.m_nNum ==card.m_nNum-1 and c2.m_nType==card.m_nType):
            return True
    return False

#电脑智能出牌V1.0，计算出牌的索引号
def  ComputerCard(cards):
    #计算手中各种牌型的数量
    int [][]paiArray = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]
    for i in range(0,14):
        card=cards[i]
        if(card.imageID>10 and card.imageID<20):#桶
                paiArray[0][0]+=1
                paiArray[0][card.imageID-10]+=1	
        if(card.imageID>20 and card.imageID<30):#条
                paiArray[1][0]+=1
                paiArray[1][card.imageID-20]+=1
        if(card.imageID>30 and card.imageID<40):#万
                paiArray[2][0]+=1
                paiArray[2][card.imageID-30]+=1	
        if(card.imageID>40 and card.imageID<50):#字
                paiArray[3][0]+=1
                paiArray[3][card.imageID-40]+=1	
    print(paiArray)
    #电脑智能选牌
    #1.判断字牌的单张 ，有则找到
    for j in range(1,10):
        if(paiArray[3][j]==1):
            #获取在手中牌的位置下标
            k=ComputerSelectCard(cards,3+1,j)
            return k

    #2.判断顺子，刻子（三张相同的）
    for i in range(0,3):
        for j in range(1,10): 
            if(paiArray[i][j]>=3)#刻子
                    paiArray[i][j]-=3
            if(j<=7 and  paiArray[i][j]>=1 and  paiArray[i][j+1]>=1
               and  paiArray[i][j+2]>=1):#顺子
                    paiArray[i][j]-=1
                    paiArray[i][j+1]-=1
                    paiArray[i][j+2]-=1

    #3.判断单张非字牌（饼，条，万） ，有则找到
    for i in range(0,3):
        for j in range(1,10): 
            if(paiArray[i][j]==1){
                #获取在手中牌的位置下标
                k=ComputerSelectCard(cards,i+1,j)
                return k

    #4.判断两张牌（饼，条，万，包括字牌） ，有则找到,拆双牌
    for i in range(3,-1):
        for j in range(1,10): 
            for (j = 1 j < 10 j++)	{
                    if(paiArray[i][j]==2){
                        #获取在手中牌的位置下标
                        k=ComputerSelectCard(cards,i+1,j)
                        return k
                        
    #5.如果以上情况均没出现则随机选出1张牌
    k=random.randint(0,13)	#随机选出1张牌
    return k	



#Card麻将牌类可以实现麻将牌正面，背面显示以及移动的功能。
'''m_bFront表示是否显示牌正面的标志
   m_nType表示牌的类型 饼=1 条=2 万=3 字牌=4
   m_nNum表示牌的点数（一到九）
   FrontURL表示牌文件的URL路径  
   imageID表示牌自己图像编号ID
   cardID表示牌自己在数组索引ID
   x,y 表示牌的坐标
'''

class  Card(Button):
    #构造函数，参数type指定牌的类型，参数num指定牌的点数
    def __init__(self,cardtype ,num,bm):
            m_nType = cardtype      #牌的类型 饼=1 条=2 万=3 字牌=4
            m_nNum= num            #牌的点数（1到9）
            #根据牌的类型及编号来设置牌文件的路径及文件名
            if m_nType==1 :#桶（饼）
                FrontURL = "res/nan/1"
            elif m_nType== 2 :#条
                FrontURL = "res/nan/2"
            elif m_nType== 3 :#万
                FrontURL = "res/nan/3"
            elif m_nType== 4 :#字牌
                FrontURL = "res/nan/4"
            self.img=bm
            imageID = m_nType * 10 + num # 牌自己图像编号ID
            FrontURL = FrontURL + str(m_nNum)#URL地址
            FrontURL = FrontURL + ".jpg"
            showPic(FrontURL)
            self.m_bFront = true
            self.setSize(51, 67)# 麻将牌方块的大小
            self.x=getX()       # 牌的坐标
            self.y=getY()
            

    def setFront(self, b ):#是否显示牌正面
        self.m_bFront = b
        if (b==true):
            self.img=bm       #显示牌正面图片
        else:
            self.img=back     #显示背面图片"bei.jpg"
    def MoveTo(self, x1, y1): #移到指定(x1, y1)位置
        self.place(x1, y1)
            
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getImageID(self):# 牌自己图像编号ID
        return imageID
#------------------------------------


win = Tk()#创建窗口对象
win.title("两人麻将--夏敏捷")#设置窗口标题
win.geometry("995x550")
#52张扑克牌的正面图片
imgs= []
h=huMain()
print(h.Win(h.allPai))
win.mainloop()




'''
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.button = Button(self, text="<Enter>",width=100,height=200)
        self.button.bind("<Enter>", self.turnRed)
        self.button.pack( )
        #self.button.place(x=100,y=100)
        self.pack({"side": "left"})
    def turnRed(self, event):
        event.widget["activeforeground"] = "red"
        event.widget.place(x=100,y=100)
        print(event.widget["anchor"],event.widget["cursor"])

    
root = Tk()
# create the application
myapp = App(master=root)

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)
b=Button()
print (b.keys())
# start the program
myapp.mainloop()

'''
