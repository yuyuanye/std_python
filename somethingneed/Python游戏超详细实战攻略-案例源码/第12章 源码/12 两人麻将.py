from tkinter import *
import random
from threading import Timer
import time
import operator
from tkinter.messagebox import *
#2016-3-19 18：00-19：00  设计Card麻将牌类（1小时）
#2016-3-19 20：30-23：00  设计发牌，显示麻功能（2.5小时）
#2016-3-20 8：30-9:30     按花色理玩家手中的牌（1小时）
#2016-3-20 10：10-11:50   胡牌计算（1.5小时）
#2016-3-20 20：30-11:30   4个按钮事件（3小时）
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
       return True
    return False

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
    paiArray = [[0,0,0,0,0,0,0,0,0,0],
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
            if(paiArray[i][j]>=3):#刻子
                    paiArray[i][j]-=3
            if(j<=7 and  paiArray[i][j]>=1 and  paiArray[i][j+1]>=1
               and  paiArray[i][j+2]>=1):#顺子
                    paiArray[i][j]-=1
                    paiArray[i][j+1]-=1
                    paiArray[i][j+2]-=1

    #3.判断单张非字牌（饼，条，万） ，有则找到
    for i in range(0,3):
        for j in range(1,10): 
            if(paiArray[i][j]==1):
                #获取在手中牌的位置下标
                k=ComputerSelectCard(cards,i+1,j)
                return k

    #4.判断两张牌（饼，条，万，包括字牌） ，有则找到,拆双牌
    for i in range(3,-1):
        for j in range(1,10): 
            if(paiArray[i][j]==2):
                #获取在手中牌的位置下标
                k=ComputerSelectCard(cards,i+1,j)
                return k
                        
    #5.如果以上情况均没出现则随机选出1张牌
    k=random.randint(0,13)	#随机选出1张牌
    return k	
#根据牌（花色nType，点数nNum）找在a数组索引位置
def   ComputerSelectCard(a, nType,nNum):
    for i in range(0,len(a)):
        card=a[i]
        if(card.m_nType==nType  and card.m_nNum==nNum):
                return i
    return -1
                        
#------------------------------------Card麻将牌类
#Card麻将牌类。
'''m_bFront表示是否显示牌正面的标志
   m_nType表示牌的类型 饼=1 条=2 万=3 字牌=4
   m_nNum表示牌的点数（一到九）
   FrontURL表示牌文件的URL路径  
   imageID表示牌自己图像编号ID
   cardID表示牌自己在数组索引ID
   x,y 表示牌的坐标
'''
#可以实现麻将牌正面，背面显示以及移动的功能   
class  Card(Button):
        
    #构造函数，参数type指定牌的类型，参数num指定牌的点数
    def __init__(self,cardtype,num,bm,master):
        Button.__init__(self,master)
        self.m_nType = cardtype      #牌的类型 饼=1 条=2 万=3 字牌=4
        self.m_nNum= num            #牌的点数（1到9）
        #根据牌的类型及编号来设置牌文件的路径及文件名
        if self.m_nType==1 :#桶（饼）
            FrontURL = "res/nan/1"
        elif self.m_nType== 2 :#条
            FrontURL = "res/nan/2"
        elif self.m_nType== 3 :#万
            FrontURL = "res/nan/3"
        elif self.m_nType== 4 :#字牌
            FrontURL = "res/nan/4"
        self.img=bm
        self.imageID = self.m_nType * 10 + self.m_nNum # 牌自己图像编号ID
        FrontURL = FrontURL + str(self.m_nNum)#URL地址
        FrontURL = FrontURL + ".png"
        #showPic(FrontURL)
        self["width"]=51       # 麻将牌方块的大小
        self["height"]=67      # 麻将牌方块的大小
        self["text"]=str(self.imageID)+ ".png"
        self.setFront(True)
        #self.MoveTo(100, 100)
        self.bind("<ButtonPress>",btn_MouseDown)
        self.cardID=0
        
    def __cmp__(self, other):
        return cmp(self.imageID, other.imageID)

    def setFront(self, b):#是否显示牌正面
        self.m_bFront = b
        if (b==True):
            self["image"]=self.img #显示牌正面图片
        else:
            self["image"]=back     #显示背面图片"bei.jpg"
            
    def MoveTo(self, x1, y1): #移到指定(x1, y1)位置
        self.place(x=x1, y=y1)
        self.x=x1             # 牌的坐标
        self.y=y1
            
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getImageID(self):# 牌自己图像编号ID
        return imageID
#------------------------------------

def ResetGame():    			#设置麻将牌的初始位置
        playersCard[0]=[] 	#玩家手中的牌
        playersCard[1]=[] 	#电脑手中的牌
        ExchangeCards()                 #完成洗牌功能
        #开始发牌
        #time1 =Timer(50,new TimerListener()) #50为50毫秒，数字越小速度越快
        #time1.start() 
        #time2 =new Timer(1000,new TimerListener2()) 
        m_LastCard = None  			#上次用户所选择的卡片
        JustOutCard = None    			#上家刚刚出的麻将牌	
 
         
        playersOutCard[0]=[]	#玩家出过的牌
        playersOutCard[1]=[]	#电脑出过的牌


#ExchangeCards()完成洗牌功能。并将136张麻将牌背面显示在舞台上。
def  ExchangeCards():			#洗牌，即随机交换两张牌
    global k
    for n in range(0,len(m_aCards)):  #重新设置136牌在场景中的位置
        m_aCards[n].x=90+20*(n%34) 
        m_aCards[n].y=170+55*(n-n%34)/34 
        m_aCards[n].MoveTo(m_aCards[n].x, m_aCards[n].y) 
        #m_aCards[n].setComponentZOrder(m_aCards[n], n) 
        m_aCards[n].setFront(True) #显示麻将牌背面
    #time1=Timer(1,Shift)
    #time1.start()
    for  k in range(0,26):  #while(k<26):
          Shift(k)
          #k=k+1
          #time1=Timer(0.1,Shift,args=(k))
          #time1.start()
          #time1.join()
          #time.sleep(0.1) # 休眠0.1秒
    #玩家按花色理手中的牌
    print("玩家按花色理手中的牌")
    sortPoker2(playersCard[0])
    print("电脑按花色理手中的牌")
    #电脑按花色理手中的牌
    sortPoker2(playersCard[1]) 
    #Get_btn.setVisible(true) 	#出牌按钮可见
    #time2.start() #开始游戏逻辑
    OuterPlayerNum = 0      #出牌人数为0
    k=26                    #

#发牌，设置最初发的26张的麻将牌的位置
def  Shift(k): 	#设置最初发的26张的麻将牌的位置，每人13张麻将牌位置
    #global k
    #print ('running',k) 
    i = k%2 
    j = (k-k%2)/2 
    if i==0 :#玩家自己 
        m_aCards[k].setFront( True ) #显示麻将牌正面
        m_aCards[k].MoveTo(80 + 55 * j, 500) 
        #监听每张麻将牌，当鼠标单击麻将牌时，系统将调用mouseClicked
        #m_aCards[k].addMouseListener(this)  

    elif i==1 :#玩家的对家(电脑)
        m_aCards[k].MoveTo(80 + 55 * j, 80) 
        m_aCards[k].setFront(True) #显示麻将牌背面
        #m_aCards[k].rotation=180 #180度旋转牌				

    playersCard[(k%2)].append(m_aCards[k]) #按顺序存储到记录2个牌手的牌的数组
    #print(playersCard[(k%2)])
    #k=k+1
    

    #if(k<26):
    #    time1=Timer(1,Shift)
    #    time1.start()
    #结束发牌
    #time1.stop() 


#sortPoker2(ArrayList cards)按花色理玩家手中的牌cards。
#由于imageID按照花色编号的，所以可以按照imageID大小排序就可以了。
def  sortPoker2(cards):        #按花色理牌手手中的牌
    n=len(cards)               #元素（牌）的个数
    for  index  in range(0,n): #重新设置各张牌在场景中的位置
        print(cards[index].imageID)
    #排序
    #sorted(cards, key=lambda card: card.imageID)   # sort by age
    cards.sort(key=operator.attrgetter('imageID'))
    #Collections.sort(cards, new SortByImageID()) 
    print("排序后2222") 
    for  index  in range(0,n): #重新设置各张牌在场景中的位置
        print(cards[index].imageID)
        newx=90 + 55 * index
        y=cards[index].getY()
        cards[index].MoveTo(newx, y)
        cards[index].cardID=index

        
#当用户点选麻将牌时，系统自动调用此函数
def btn_MouseDown(event): #鼠标单击按下事件函数
    global m_LastCard,PlayerSelectCard
    if event.widget["state"]==DISABLED:
       return
    #找到相应的麻将牌对象
    #event.widget获取触发事件的对象
    card=event.widget
    card.y-=20
    card["text"]="aaa"
    card.place(x=event.widget.x,y=event.widget.y)
    if(m_LastCard==None):  #未选过的牌
        m_LastCard=card
        PlayerSelectCard=card
    else:		   #已经选过的牌
        m_LastCard.MoveTo(m_LastCard.getX(), m_LastCard.getY()+20)
        m_LastCard.y+=20    #下移20像素
        m_LastCard=card 
        PlayerSelectCard=card   

#-----------------------------

win = Tk()#创建窗口对象
win.title("两人麻将--夏敏捷")#设置窗口标题
win.geometry("995x750")
#52张扑克牌的正面图片
imgs= []
#扑克牌背面图片
back=PhotoImage(file='D:\\python\\res\\bei.png')
m_aCards=[]
playersCard=[[],[]]                    #记录2个牌手拿到的牌
playersOutCard=[[],[]]                 #记录2个牌手出过的牌
k=0                                    #记录已发出牌的个数
m_LastCard=None                        #用户是否选过牌


def BeginGame():                        #开始游戏，玩家先出牌
        MyTurn = True	
        LoadCards()			#加载136张麻将牌到舞台
        random.shuffle(m_aCards)        #洗牌操作，将列表中元素打乱，洗牌目的
        ResetGame()			#发初始26张牌给玩家和电脑


def  LoadCards():                       #加载136张麻将牌到舞台
    for  m_nType in range(1,4):         #1--3代表饼条万 
        for num in range(1,10):         #1--9
            #根据牌的类型及编号来设置牌文件的路径及文件名
            if m_nType==1 :#桶（饼）
                FrontURL = "res/nan/1"
            elif m_nType== 2 :#条
                FrontURL = "res/nan/2"
            elif m_nType== 3 :#万
                FrontURL = "res/nan/3"
            
            FrontURL = FrontURL + str(num)#URL地址
            FrontURL = FrontURL + ".png"        
            imgs.append(PhotoImage(file=FrontURL))
            for n in range(1,5):            #每种牌4张	
                card= Card(m_nType, num,imgs[len(imgs)-1],win)  #创建“饼条万”牌
                #card.MoveTo(100+num*60,100+m_nType*80)
                m_aCards.append(card) 	#将牌添加到数组
                
                
    cardtype = 4 #字牌
    for num in range(1,8):                  #1--7
        FrontURL = "res/nan/4"
        FrontURL = FrontURL + str(num)   #URL地址
        FrontURL = FrontURL + ".png"
        imgs.append(PhotoImage(file=FrontURL))
        for n in range(1,5):                #每种牌4张	
            card= Card(cardtype, num,imgs[len(imgs)-1],win)    #创建字牌
            #card.MoveTo(100+num*60,100+4*80)
            #card["state"]=DISABLED
            m_aCards.append(card)  	        #将牌添加到数组
#------------
def fun2():# 出牌顺序控制
    MyTurn = True     #轮到玩家出牌
    Get_btn["state"]=NORMAL #摸牌可见
    if(len(playersOutCard[1])>0):
            #取电脑出的牌,即最后一张
            card=playersOutCard[1][len(playersOutCard[1])-1]
            #判断电脑出的牌玩家是否可以吃碰 
            if(canPeng(playersCard[0],card)):#玩家是否可以碰牌
                Peng_btn["state"]=NORMAL #碰牌可见
            if (canChi(playersCard[0],card)):#玩家是否可以吃牌
                Chi_btn["state"]=NORMAL #吃牌可见                                            
            #不能吃碰则只能直接摸牌
            if ( not canChi(playersCard[0],card)and not canPeng(playersCard[0],card)):
                Peng_btn["state"]=DISABLED
                Chi_btn["state"]=DISABLED
                #OnBtnGetClick();#直接摸牌
    else: #电脑没出过牌直接摸牌
        Get_btn["state"]=NORMAL #摸牌可见

#4个按钮事件代码
#“出牌”按钮单击事件中，将被选中的牌PlayerSelectCard移到左侧，并从playersCard[0] 中删除被选中的牌PlayerSelectCard。Order++则可以轮到电脑出牌。
def OnBtnOutClick(event):
    global MyTurn
    global PlayerSelectCard,m_LastCard,MyTurn
    print("出牌")
    if(MyTurn == False):        #没轮到自己出牌
        return
    print(PlayerSelectCard)
    if not(PlayerSelectCard==None):
        Out_btn["state"]=DISABLED			   #出牌按钮不可见
        playersOutCard[0].append(PlayerSelectCard);					
        PlayerSelectCard.x=len(playersOutCard[0])*25-25; #移动被选中的牌
        PlayerSelectCard.y=420;
        PlayerSelectCard.MoveTo(PlayerSelectCard.x, PlayerSelectCard.y);
        #outCardOrder(playersOutCard[0]);#整理玩家出的牌Z轴深度
        #玩家牌减少
        print(PlayerSelectCard.cardID)
        del(playersCard[0][PlayerSelectCard.cardID])
        #playersCard[0].remove(PlayerSelectCard);
        m_LastCard=None
        PlayerSelectCard=None				
        MyTurn = False
        Out_btn["state"]=DISABLED
        ComputerOut( ) #电脑智能出牌
        fun2()

        
#对于碰吃牌，这里不再区分处理
def  Chi_btn(event):#吃牌按钮单击事件
    global MyTurn
    card=playersOutCard[1].get(len(playersOutCard[1])-1);
    card.MoveTo(90 + 55 * 13, 500);
    card.setFront( true );#显示麻将牌正面
    playersCard[0].append(card);#第14张牌
    
    sortPoker2(playersCard[0]);#按顺序存储到记录玩家牌手的牌的数组	
    result1=ComputerCardNum(playersCard[0]);#计算手中各种牌型的数量,判断胡牌
    if(result1):#胡牌了
        Win_btn["state"]=NORMAL
        showinfo(title="恭喜",message="玩家Win!")
        return #玩家不需要再出牌
    Out_btn["state"]=NORMAL	#出牌按钮可见
    MyTurn=True
    

#“摸牌”按钮单击事件中，将m_aCards[k]牌移动到玩家牌所在位置，并按花色排序理牌。
#调用ComputerCardNum(playersCard[0])计算手中各种牌型的数量并判断出是否胡牌。如果胡牌则游戏结束。
def OnBtnGetClick(event):               #摸牌按钮事件
    global k
    global playersCard,MyTurn
    #玩家按花色理手中的牌
    m_aCards[k].MoveTo(90 + 55 * 13, 500) 
    m_aCards[k].setFront(True)         #显示麻将牌正面
    print("玩家手中牌1111",len(playersCard[0]))
    playersCard[0].append(m_aCards[k])    #第14张牌
    #监听第14张牌
    #m_aCards[k].addMouseListener(this) #错误
    #cardAddMouseListener(m_aCards[k])
    print("玩家手中牌2222",len(playersCard[0]))
    sortPoker2(playersCard[0]) #按顺序存储到记录牌手的牌的数组
    result1=ComputerCardNum(playersCard[0]) #计算手中各种牌型的数量,判断胡牌
    if(result1):#胡牌了
        Win_btn["state"]=NORMAL
        showinfo(title="恭喜",message="玩家Win!")
        return #玩家不需要再出牌
    k=k+1  #下一张要摸的牌在m_aCards索引号
    Out_btn["state"]=NORMAL 	#出牌按钮可见
    MyTurn=True


#ComputerOut()实现电脑智能出牌，首先将m_aCards[k]牌移动到对家（电脑）牌所在位置，并按花色排序理牌。
#调用ComputerCardNum(playersCard[0])计算电脑手中各种牌型的数量并判断出是否胡牌。
#如果胡牌则游戏结束，否则调用ComputerCard(playersCard[1])智能出牌。	
def ComputerOut( ): #电脑智能出牌
    global k,MyTurn
    #对家（电脑）摸牌
    m_aCards[k].MoveTo(90 + 55 * 13, 80);			
    m_aCards[k].setFront( False );#显示麻将牌背面
    playersCard[1].append(m_aCards[k]);#第14张牌
    
    result1=ComputerCardNum(playersCard[1]);# 计算电脑手中各种牌型的数量,判断胡牌
    if(result1):#胡牌了
        showinfo(title="遗憾",message="电脑Win!")
        return;#对家（电脑）不需要再出牌
       
    i = ComputerCard(playersCard[1]);#智能出牌
    #i=0;#总是出第一张牌，没有智能出牌
    card= playersCard[1][i]
    del(playersCard[1][i])
    #加到电脑出过牌的数组			
    playersOutCard[1].append(card)
    #outCardOrder(playersOutCard[1]);#整理出过的牌，Z轴深度问题
    card.setFront( True );#显示麻将牌正面

    #电脑按花色理手中的牌
    sortPoker2(playersCard[1]);
    card.x=len(playersOutCard[1])*25-25;
    card.y=10;
    card.MoveTo(card.x, card.y);
    k=k+1 #发过牌的总数
    MyTurn=True  #轮到玩家
	

#计算玩家手中各种牌型的数量
def ComputerCardNum(cards):     #玩家手中牌playersCard[0]
    #计算手中各种牌型的数量
    paiArray = [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]
    print("玩家手中牌",len(cards))
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
    hu =huMain()		        #胡牌算法类
    result=hu.Win(paiArray)		#是否胡牌判断
    return result
	



#功能按钮
Get_btn=Button(win,text="摸牌",width=70,height=27)
Peng_btn=Button(win,text="碰牌",width=70,height=27)
Chi_btn=Button(win,text="吃牌",width=70,height=27)
Out_btn=Button(win,text="出牌",width=70,height=27)
Win_btn=Button(win,text="胡牌",width=70,height=27)

Win_btn.place(x=500,y=600,width=70,height=27)
Chi_btn.place(x=600,y=600,width=70,height=27)
Peng_btn.place(x=700,y=600,width=70,height=27)
Out_btn.place(x=800,y=600,width=70,height=27)
Get_btn.place(x=900,y=600,width=70,height=27)
#Get_btn.pack_forget() #隐藏button
#Get_btn["state"]=DISABLED
Peng_btn["state"]=DISABLED
Chi_btn["state"]=DISABLED
Out_btn["state"]=DISABLED
Win_btn["state"]=DISABLED
Get_btn.bind("<ButtonPress>",OnBtnGetClick)
Out_btn.bind("<ButtonPress>",OnBtnOutClick)
Chi_btn.bind("<ButtonPress>",OnBtnGetClick)
BeginGame()                      #开始游戏，玩家先出牌
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
