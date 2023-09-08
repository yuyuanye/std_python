
#==========================  2023-09-02    ===================================================
from tkinter import *
from random import *
from tkinter.ttk import  *
from tkinter.messagebox import *
testcode = '12.7'
if testcode == '3.1':
    #set window title
    win = Tk()
    win.title('tkinter base useage study')
    txt = Label(win, text='\ngame over\n').pack()
    win.mainloop()
elif testcode == '3.2':
    #set window porperty
    win = Tk()
    win.title('tkinter base property')
    win.geometry('300x150')
    win.configure(bg='yellow')
    win.maxsize(500,500)
    couple = '\n上联：足不出户一台电脑打天下\n\n下联：窝宅在家一双巧手定乾坤\n'
    txt= Label(win, text=couple,bg='yellow').pack()
    win.mainloop()
elif testcode == '3.3':
    #set window size and positon
    win = Tk()
    win.title('tkinter window positon')
    win.configure(bg='#a7ea90')
    winw = 300
    winh = 220
    scrw = win.winfo_screenwidth()
    scrh = win.winfo_screenheight()
    x = (scrw - winw)/2
    y = (scrh - winh)/2
    win.geometry('%dx%d+%d+%d' % (winw,winh,x,y))
    str  = 'bi shi lian'
    #txt = Label(win,text=str,bg='#a7ea90').pack()
    txt = Label(win, text=str, bg='#c3deef').pack()
    win.mainloop()
elif testcode == '3.4':
    # set window size and font
    '''
    pass
    win = Tk()
    win.geometry('300x200')
    win.configure(bg='black')
    #Label(win, text='xiao kou chai fei jiu bu kai',foreground='red',background='#c3deef').pack() \
    #Label(win, text='和', fg='red', bg='#c3deef',width=20,height=3,anchor='nw').pack()
    #Label(win, text='和', fg='red', bg='#c3deef', width=20, height=3, anchor='se').pack()
    #Label(win, text='以和为贵', fg='red', bg='#c3deef', width=20, height=3, anchor='center').pack()
    #Label(win, text='以和为贵', fg='red', bg='#c3deef', padx=2,pady=2).pack()
    Label(win, text='以和为贵', fg='red', bg='#c3deef').pack()
    win.mainloop()
    '''
    win = Tk()
    lable = Label(win,text='昨日重现',bg='#63a4eb',relief='groove',cursor='spider',width=30,height=2,font='华文新魏 28 bold')
    lable.pack(padx=5,pady=5,side=LEFT)
    win.mainloop()
elif testcode == '3.5':
    '''
    # set window size and font
    win = Tk()
    win.title('充值成功')
    win.geometry('300x240')
    str = "1、一级vip 30天\n\n2、每天额外赠送300金币\n\n3、全英雄限免30天"
    text = Label(win,text='\n充值成功',font='Times 18 bold').pack()
    text1 = Label(win,text='\n恭喜获得',font='16').pack(anchor=W,padx=45)
    text2 = Label(win,text=str,font='18',fg='red',justify='left').pack()
    win.mainloop()
    '''
    win = Tk()
    label=Label(win,text='hello world')
    label.config(bg='#def1ef',fg='red',font=14)
    label.pack()
    win.mainloop()
elif testcode == '4.1':
    #==============================2023 09 02 ==================================
    win = Tk()
    txt1 = '魔动士考学'
    txt2 = '迟夏写长信'
    txt3 = '早春不过一棵树'
    '''
    Label(win, text=txt1,bg='#f5dfcc').pack(side='left')
    Label(win,text=txt2,bg='#edb584').pack(side='left')
    Label(win,text=txt3,bg='#ef994c').pack(side='left')
    
    Label(win, text=txt1,bg='#f5dfcc').pack(side='bottom')
    Label(win,text=txt2,bg='#edb584').pack(side='bottom')
    Label(win,text=txt3,bg='#ef994c').pack(side='bottom')

    Label(win, text=txt1, bg='#f5dfcc',width=20).pack(side='bottom',padx=20,pady=5)
    Label(win, text=txt2, bg='#edb584',width=20).pack(side='bottom',padx=20,pady=5)
    Label(win, text=txt3, bg='#ef994c',width=20).pack(side='bottom',padx=20,pady=5)
    '''
    Label(win, text=txt1, bg='#f5dfcc', width=20).pack(side='bottom', padx=20, pady=5,ipadx=10,ipady=5)
    Label(win, text=txt2, bg='#edb584', width=20).pack(side='bottom', padx=20, pady=5,ipadx=10,ipady=5)
    Label(win, text=txt3, bg='#ef994c', width=20).pack(side='bottom', padx=20, pady=5,ipadx=10,ipady=5)
    win.mainloop()
elif testcode == '4.2':

    win=Tk()
    win.title('tkinter 初使用')
    txt1 = Label(win, text='象吃狮', bg='#ba55d3', font=14)
    txt2 = Label(win, text='狮吃虎', bg='#c1ffc1', font=14)
    txt3 = Label(win, text='虎吃豹', bg='#cdb5cd', font=14)
    txt4 = Label(win, text='豹吃狼', bg='#c1ffc1', font=14)
    txt5 = Label(win, text='狼吃狗', bg='#cdb5cd', font=14)
    txt6 = Label(win, text='狗吃猫', bg='#ba55d3', font=14)
    txt7 = Label(win, text='猫吃鼠', bg='#cdb5cd', font=14)
    txt8 = Label(win, text='鼠吃象', bg='#c1ffc1', font=14)
    txt1.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
    txt2.pack(side='left', padx=10, pady=5, ipadx=6, ipady=4)
    txt3.pack(side='left', padx=10, pady=5, ipadx=6, ipady=4)
    txt4.pack(side='left', padx=10, pady=5, ipadx=6, ipady=4)
    txt5.pack(side='left', padx=10, pady=5, ipadx=6, ipady=4)
    txt6.pack(side='left', padx=10, pady=5, ipadx=6, ipady=4)
    txt7.pack(side='left', padx=10, pady=5, ipadx=6, ipady=4)
    txt8.pack(side='left', padx=10, pady=5, ipadx=6, ipady=4)
    win.mainloop()

    '''
    win=Tk()
    txt='枯藤老树昏鸦，小桥流水人家'
    txt1=Label(win,text=txt,bg='#e6f5c8',fg='red',font=14).pack(side='left',fill='y')
    win.mainloop()
    '''
elif testcode == '4.3':
    win = Tk()
    win.title('tkinter 初使用')
    txt1 = Label(win, text='象吃狮', bg='#ba55d3', font=14)
    txt2 = Label(win, text='狮吃虎', bg='#c1ffc1', font=14)
    txt3 = Label(win, text='虎吃豹', bg='#cdb5cd', font=14)
    txt4 = Label(win, text='豹吃狼', bg='#c1ffc1', font=14)
    txt5 = Label(win, text='狼吃狗', bg='#cdb5cd', font=14)
    txt6 = Label(win, text='狗吃猫', bg='#ba55d3', font=14)
    txt7 = Label(win, text='猫吃鼠', bg='#cdb5cd', font=14)
    txt8 = Label(win, text='鼠吃象', bg='#c1ffc1', font=14)
    txt1.pack(side='left', padx=10, ipadx=6, fill='y')
    txt2.pack(side='left', padx=10, ipadx=6, fill='y')
    txt3.pack(side='left', padx=10, ipadx=6, fill='y')
    txt4.pack(side='left', padx=10, ipadx=6, fill='y')
    txt5.pack(side='left', padx=10, ipadx=6, fill='y')
    txt6.pack(side='left', padx=10, ipadx=6, fill='y')
    txt7.pack(side='left', padx=10, ipadx=6, fill='y')
    txt8.pack(side='left', padx=10, ipadx=6, fill='y')
    win.mainloop()
elif testcode == '4.4':
    win = Tk()
    win.title('tkinter 初使用')
    txt1 = Label(win, text='象吃狮', bg='#ba55d3', font=14)
    txt2 = Label(win, text='狮吃虎', bg='#c1ffc1', font=14)
    txt3 = Label(win, text='虎吃豹', bg='#cdb5cd', font=14)
    txt4 = Label(win, text='豹吃狼', bg='#c1ffc1', font=14)
    txt5 = Label(win, text='狼吃狗', bg='#cdb5cd', font=14)
    txt6 = Label(win, text='狗吃猫', bg='#ba55d3', font=14)
    txt7 = Label(win, text='猫吃鼠', bg='#cdb5cd', font=14)
    txt8 = Label(win, text='鼠吃象', bg='#c1ffc1', font=14)
    txt1.pack(side='left', padx=10, ipadx=6, fill='y',expand=1)
    txt2.pack(side='left', padx=10, ipadx=6, fill='y',expand=1)
    txt3.pack(side='left', padx=10, ipadx=6, fill='y',expand=1)
    txt4.pack(side='left', padx=10, ipadx=6, fill='y',expand=1)
    txt5.pack(side='left', padx=10, ipadx=6, fill='y',expand=1)
    txt6.pack(side='left', padx=10, ipadx=6, fill='y',expand=1)
    txt7.pack(side='left', padx=10, ipadx=6, fill='y',expand=1)
    txt8.pack(side='left', padx=10, ipadx=6, fill='y',expand=1)
    win.mainloop()
elif testcode == '4.5':
    win =Tk()
    win.geometry('350x150')
    win.title('tkinter 使用')
    txt1 = Label(win, text='确定退出本窗口吗？')
    txt2 = Label(win, text='果断退出',bg='#c1ffc1')
    txt3 = Label(win,text='我在想想',bg='#cdb5cd')
    txt1.pack(fill='x',pady=20)
    txt2.pack(side='right',padx=10,ipadx=6,pady=20,anchor='se')
    txt3.pack(side='right', padx=10, ipadx=6, pady=20, anchor='se')
    win.mainloop()
elif testcode == '4.6':
    win = Tk()
    win.title('tkinter 初使用')
    txt1 = Label(win, text='象吃狮', bg='#ba55d3', font=14)
    txt2 = Label(win, text='狮吃虎', bg='#c1ffc1', font=14)
    txt3 = Label(win, text='虎吃豹', bg='#cdb5cd', font=14)
    txt4 = Label(win, text='豹吃狼', bg='#c1ffc1', font=14)
    txt5 = Label(win, text='狼吃狗', bg='#cdb5cd', font=14)
    txt6 = Label(win, text='狗吃猫', bg='#ba55d3', font=14)
    txt7 = Label(win, text='猫吃鼠', bg='#cdb5cd', font=14)
    txt8 = Label(win, text='鼠吃象', bg='#c1ffc1', font=14)
    txt1.pack(side='left', padx=10, ipadx=6, fill='y', expand=1)
    txt2.pack(side='left', padx=10, ipadx=6, fill='y', expand=1,before=txt1)
    txt3.pack(side='left', padx=10, ipadx=6, fill='y', expand=1,before=txt2)
    txt4.pack(side='left', padx=10, ipadx=6, fill='y', expand=1,before=txt3)
    txt5.pack(side='left', padx=10, ipadx=6, fill='y', expand=1,before=txt4)
    txt6.pack(side='left', padx=10, ipadx=6, fill='y', expand=1,before=txt5)
    txt7.pack(side='left', padx=10, ipadx=6, fill='y', expand=1,before=txt6)
    txt8.pack(side='left', padx=10, ipadx=6, fill='y', expand=1,before=txt7)
    win.mainloop()
elif testcode == '4.7':
    subtest = 3
    if subtest == 1:
        win = Tk()
        win.title('tkinter 初使用')
        Label(win, text='1x1=1', bg='#e0ffff').grid(row=0, column=0, padx=10)
        Label(win, text='1x2=2', bg='#e0ffff').grid(row=1, column=0, padx=10)
        Label(win, text='1x3=3', bg='#e0ffff').grid(row=2, column=0, padx=10)
        Label(win, text='1x4=4', bg='#e0ffff').grid(row=3, column=0, padx=10)
        Label(win, text='2x2=4', bg='#e0ffff').grid(row=1, column=1, padx=10)
        Label(win, text='3x2=6', bg='#e0ffff').grid(row=2, column=1, padx=10)
        Label(win, text='4x2=8', bg='#e0ffff').grid(row=3, column=1, padx=10)
        Label(win, text='3x3=9', bg='#e0ffff').grid(row=2, column=2, padx=10)
        Label(win, text='3x4=12', bg='#e0ffff').grid(row=3, column=2, padx=10)
        Label(win, text='4x4=16', bg='#e0ffff').grid(row=3, column=3, padx=10)
        win.mainloop()
    elif subtest == 2:
        win = Tk()
        label = Label(win,text = 'columnspan=4', width=15,height = 1,relief='groove',bg='#ede19a')
        label21 = Label(win, text='columnspan=2', width=15, height=1, relief='groove', bg='#edbe9a')
        label22 = Label(win, text='columnspan=2', width=15, height=1, relief='groove', bg='#ede19a')
        label.grid(row=0,column=0,columnspan=4)
        label21.grid(row=1, column=0, columnspan=2)
        label22.grid(row=1, column=2, columnspan=2)
        label31 = Label(win, width=15, height=1, relief='groove', bg='#e5aeae').grid(row=3,column=0)
        label32 = Label(win, width=15, height=1, relief='groove', bg='#e5aeae').grid(row=3, column=1)
        label33 = Label(win, width=15, height=1, relief='groove', bg='#e5aeae').grid(row=3, column=2)
        label34 = Label(win, width=15, height=1, relief='groove', bg='#e5aeae').grid(row=3, column=3)
        win.mainloop()
    elif subtest == 3:
        win = Tk()
        Label(win,text='春花秋月何时了', bg='#EBC7c7',relief='groove').grid(row=0,column=0)
        #Label(win, text='往事知多少', bg='#dfc7eb', relief='groove').grid(row=1, column=0)
        Label(win, text='往事知多少', bg='#dfc7eb', relief='groove').grid(row=1, column=0,sticky=W)
        win.mainloop()
    else:
        pass
elif testcode == '4.8':
    win = Tk()
    win.rowconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    txt1 = Label(win, width=15,text='1',height=2, relief='groove',bg='#e0ffff')
    txt1.grid(row=0,column=0, sticky=N+W)
    txt2 = Label(win, width=15,text='2', height=2, relief='groove', bg='#99ffcc')
    txt2.grid(row=0, column=1, sticky=N + E)
    txt3 = Label(win, width=15,text='3', height=2, relief='groove', bg='#e0ffff')
    txt3.grid(row=1, column=0, sticky=S + W)
    txt4 = Label(win, width=15,text='4',height=2, relief='groove', bg='#99ffcc')
    txt4.grid(row=1, column=1, sticky=S + E)
    win.mainloop()
elif testcode == '4.9':
    win = Tk()
    txt1 = Label(win, text='赵云', bg='#93edd4',relief='groove', font=14)
    txt2 = Label(win, text='曹操', bg='#a6e3a8',relief='groove', font=14)
    txt3 = Label(win, text='黄忠', bg='#93edd4',relief='groove', font=14)
    txt4 = Label(win, text='张飞', bg='#93edd4',relief='groove', font=14)
    txt5 = Label(win, text='关羽', bg='#93edd4',relief='groove', font=14)
    txt6 = Label(win, text='马超', bg='#93edd4',relief='groove', font=14)
    txt7 = Label(win, text='卒', bg='#f3f4c4',relief='groove', font=14)
    txt8 = Label(win, text='卒', bg='#f3f4c4', relief='groove', font=14)
    txt9 = Label(win, text='卒', bg='#f3f4c4', relief='groove', font=14)
    txt0 = Label(win, text='卒', bg='#f3f4c4', relief='groove', font=14)
    txt1.place(width=60, height=120,x=0,y=0)
    txt2.place(width=120, height=120, x=60, y=0)
    txt3.place(width=60, height=120, x=180, y=0)
    txt4.place(width=60, height=120, x=0, y=120)
    txt5.place(width=120, height=60, x=60, y=120)
    txt6.place(width=60, height=120, x=180, y=120)
    txt7.place(width=60, height=60, x=60, y=180)
    txt8.place(width=60, height=60, x=120, y=180)
    txt9.place(width=60, height=60, x=0, y=240)
    txt0.place(width=60, height=60, x=180, y=240)
    win.mainloop()
elif testcode == '4.10':
    win = Tk()
    txt1 = Label(win, text='赵云', bg='#93edd4', relief='groove', font=14)
    txt2 = Label(win, text='曹操', bg='#a6e3a8', relief='groove', font=14)
    txt3 = Label(win, text='黄忠', bg='#93edd4', relief='groove', font=14)
    txt4 = Label(win, text='张飞', bg='#93edd4', relief='groove', font=14)
    txt5 = Label(win, text='关羽', bg='#93edd4', relief='groove', font=14)
    txt6 = Label(win, text='马超', bg='#93edd4', relief='groove', font=14)
    txt7 = Label(win, text='卒', bg='#f3f4c4', relief='groove', font=14)
    txt8 = Label(win, text='卒', bg='#f3f4c4', relief='groove', font=14)
    txt9 = Label(win, text='卒', bg='#f3f4c4', relief='groove', font=14)
    txt0 = Label(win, text='卒', bg='#f3f4c4', relief='groove', font=14)

    txt1.place(relwidth=0.25, relheight=0.4,relx=0,rely=0)
    txt2.place(relwidth=0.5, relheight=0.4,relx=0.25,rely=0)
    txt3.place(relwidth=0.25, relheight=0.4,relx=0.75,rely=0)
    txt4.place(relwidth=0.25, relheight=0.4,relx=0,rely=0.4)
    txt5.place(relwidth=0.5, relheight=0.2,relx=0.25,rely=0.4)
    txt6.place(relwidth=0.25, relheight=0.4,relx=0.75,rely=0.4)
    txt7.place(relwidth=0.25, relheight=0.2,relx=0.25,rely=0.6)
    txt8.place(relwidth=0.25, relheight=0.2,relx=0.5,rely=0.6)
    txt9.place(relwidth=0.25, relheight=0.2,relx=0,rely=0.8)
    txt0.place(relwidth=0.25, relheight=0.2,relx=0.75,rely=0.8)
    win.mainloop()
elif testcode == '5.1':
    win = Tk()
    txt1 = Label(win, text='象', bg='#ffebcd', width=5, padx=4, pady=4, font=14)
    txt2 = Label(win, text='狮', bg='#c1ffc1', width=5, padx=4, pady=4, font=14)
    txt3 = Label(win, text='虎', bg='#ffebcd', width=5, padx=4, pady=4, font=14)
    txt4 = Label(win, text='豹', bg='#c1ffc1', width=5, padx=4, pady=4, font=14)
    txt5 = Label(win, text='狼', bg='#ffebcd', width=5, padx=4, pady=4, font=14)
    txt6 = Label(win, text='狗', bg='#c1ffc1', width=5, padx=4, pady=4, font=14)
    txt7 = Label(win, text='猫', bg='#ffebcd', width=5, padx=4, pady=4, font=14)
    txt8 = Label(win, text='鼠', bg='#c1ffc1', width=5, padx=4, pady=4, font=14)
    txtr1= Label(win, text='→', fg='#b22222', padx=2, pady=2).grid(row=1, column=2)
    txtr2 = Label(win, text='→', fg='#b22222', padx=2, pady=2).grid(row=1, column=4)
    txtb1 = Label(win, text='↓', fg='#b22222', padx=2, pady=2).grid(row=2, column=5)
    txtb2 = Label(win, text='↓', fg='#b22222', padx=2, pady=2).grid(row=4, column=5)
    txtl1 = Label(win, text='←', fg='#b22222', padx=2, pady=2).grid(row=5, column=4)
    txtl2 = Label(win, text='←', fg='#b22222', padx=2, pady=2).grid(row=5, column=2)
    txtt1 = Label(win, text='↑', fg='#b22222', padx=2, pady=2).grid(row=4, column=1)
    txtt2 = Label(win, text='↑', fg='#b22222', padx=2, pady=2).grid(row=2, column=1)
    txt1.grid(row=1, column=1)
    txt2.grid(row=1, column=3)
    txt3.grid(row=1, column=5)
    txt4.grid(row=3, column=5)
    txt5.grid(row=5, column=5)
    txt6.grid(row=5, column=3)
    txt7.grid(row=5, column=1)
    txt8.grid(row=3, column=1)
    win.mainloop()
elif testcode == '5.2':
    subtest = 4
    if subtest == 1:
        from tkinter import *
        win = Tk()
        win.title('快乐写数字')
        win.configure(bg='#eef3c3')
        img = PhotoImage(file="start.png")
        game = Label(win, image=img, text='快乐写数字', compound='bottom', font='楷体 20 bold', fg='#d25fed', bg='#eef3c3')
        game.grid(row=2, column=0, columnspan=2)
        Label(win, text='输入兑奖码领取稀有道具', bg='#eef3c3').grid(row=4, column=0, columnspan=2)
        Label(win, text='兑奖码：', font=14, bg='#eef3c3').grid(row=4, column=0, sticky=E, pady=10)
        Label(win, width=15, bg='#fff', relief='groove').grid(row=4, column=1, pady=10)
        Label(win, text='确认兑换', width=20, relief='groove', bg='#0996ed').grid(row=5, column=0, columnspan=2, pady=5)
        win.mainloop()
    elif subtest == 2:
        from tkinter import *
        win=Tk()
        win.title("欢乐写数字")
        win.configure(bg="#EEF3C3")   #设置窗口的背景颜色
        img=PhotoImage(file="game.png")  #创建图片对象
        #在Label中添加图片和文字，compound表示图片在文字下方
        game=Label(win,image=img,text="欢乐写数字",compound="bottom",font="楷体 20 bold",fg="#D25EED",bg="#EEF3C3")
        game.grid(row=2,column=0,columnspan=2)
        # 添加文字
        Label(win,text="输入兑奖码领取稀有道具",bg="#EEF3C3").grid(row=3,column=0,columnspan=2)
        Label(win,text="兑奖码：",font=14,bg="#EEF3C3").grid(row=4,column=0,sticky=E,pady=10)
        Label(win,width=15,bg="#fff",relief="groove").grid(row=4,column=1,pady=10)
        Label(win,text="确认兑换",width=20,relief="groove",bg="#0996ED").grid(row=5,column=0,columnspan=2,pady=5)
        win.mainloop()
    elif subtest == 3:
        win = Tk()
        win.configure(bg='#c9edeb')
        win.maxsize(500,500)
        couple = '上联：足不出户一台电脑打天下 下联：窝宅在家一双巧手定乾坤横批：量我风采'
        #txt = Label(win, text=couple, bg='#c9edeb',font=14, wraplength=230, justify='left')
        txt = Label(win, text=couple, bg='#c9edeb', font=14, justify='left')
        txt.pack(padx=20,pady=20)
        win.mainloop()
    elif subtest == 4:
        win = Tk()
        Label(win, text='出发地：',font=14).grid(pady=10, row=0,column=0)
        Entry(win).grid(row=0, column=1)
        Label(win, text='目的地：', font=14).grid(pady=10, row=1,column=0)
        Entry(win).grid(row=1, column=1)
        win.mainloop()
    else:
        pass
elif testcode == '5.3':
    subtest = 3
    if subtest == 1:
        win = Tk()
        win.configure(bg='#efe5d2')
        user=PhotoImage(file='user.png')
        psw=PhotoImage(file='psw.png')
        Label(win, image=user, bg='#fff').grid(row=0)
        Entry(win).grid(row=0, column=1,padx=10,pady=10)
        Label(win, image=psw, bg='#fff').grid(row=1)
        Entry(win, show='*').grid(row=1, column=1,padx=10, pady=10)
        Label(win, text='确定', relief='groove').grid(row=2, columnspan=2, pady=10)
        win.mainloop()
    elif subtest == 2:
        win=Tk()
        def show():
            str=entry.get()
            print(str)
        entry = Entry(win)
        entry.grid(row=0)
        Button(win, text='显示', command=show).grid(row=0,column=1)
        win.mainloop()
    elif subtest ==3:
        win = Tk()
        Label(win, text='用户名').grid(row=0, column=0)
        entry= Entry(win, relief='groove')
        entry.insert(0, 'admin')
        entry.grid(row=0, column=1)
        win.mainloop()
    else:
        pass
elif testcode == '5.4':
    win = Tk()
    win.configure(bg='#f3e4a4')
    def add():
        re.delete(0,END)
        add1 = int(op1.get())
        add2 = int(op2.get())
        re.insert(INSERT, add1+add2)
    op1=Entry(win, width=5,relief='groove')
    op1.grid(row=0, pady=20)
    Label(win, text='+', bg='#f3e4a4').grid(row=0, column=1)
    op2 = Entry(win, width=5, relief='groove')
    op2.grid(row=0, column=2)
    Label(win, text='=', bg='#f3e4a4').grid(row=0, column=3)
    re = Entry(win, width=5, relief='groove')
    re.grid(row=0, column=4)
    Button(win, text='计算', command=add, relief='groove', bg='#10c9f5').grid(row=1,columnspan=5,ipadx=10)
    win.mainloop()
#==========================  2023-09-03    ===================================================
elif testcode == '5.5':
    subtest = 3
    if subtest == 1:
        i=0
        def show():
            global i
            i+=1
            label.config(text='你点了我\t'+str(i)+'下')
        root=Tk()
        text = Text(root, width=45,height=10,bg='#cae1ff',relief='solid')
        photo = PhotoImage(file='ico.png')
        text.image_create(END,imag=photo)
        text.insert(INSERT, '在这里添加文本：\n')
        text.pack()
        bt = Button(root,text='你点我试试',command=show,padx=10)
        text.window_create('2.end', window=bt)
        label = Label(root, padx=10, text='你点了我0下')
        text.window_create('3.end',window=label)
        root.mainloop()
    elif subtest == 2:
        win=Tk()
        text=Text(win)
        text.insert(INSERT,'I love python')
        text.pack()
        print(text.get(1.2,1.6))
        win.mainloop()
    elif subtest ==3:
        def undo1(event):
            text.edit_undo()
        def redo1(event):
            text.edit_redo()
        def callback(event):
            text.edit_separator()
        root = Tk()
        text = Text(root, width=50, height=30, undo=True, autoseparators=False)
        text.pack()
        text.insert(INSERT, '在下方添加文本，通过键盘<Ctrl+Z>撤销操作和<Ctrl+Y>键恢复操作')
        text.bind('<Key>',callback)
        text.bind('Control-Z',undo1)
        text.bind('Control-Y', redo1)
        root.mainloop()
    else:
        pass
elif testcode == '5.6':
    win = Tk()
    win.title('购买道具')
    Label(win, text ='购买道具：').grid(row=0, column=0,pady=10)
    Spinbox(win,values=('绿水晶','红宝石','生命水')).grid(row=0, column=1,pady=10)
    Label(win, text='购买数量：').grid(row=1, column=0, pady=10)
    Spinbox(win, from_=1,to=5).grid(row=1, column=1,pady=10)
    Label(win, text='限购5件').grid(row=1, column=2, pady=10)
    Label(win, text='支付方式').grid(row=2, column=0, pady=10)
    Spinbox(win, values=('金币','钻石','点券')).grid(row=2, column=1,pady=10)
    win.mainloop()
    pass
elif testcode == '5.7':
    def pay():
        number = int(num.get())
        total = number * mon
        text1='选购'+ val.get()+'总价'+str(total)+'金币'
        label.config(text=text1)
    def typ():
        global mon
        if val.get() == '绿水晶':
            mon=5
        elif val.get() =='红宝石':
            mon=10
        else:
            mon = 15
        pay()

    win = Tk()
    win.title('购买道具')
    Label(win, text='购买道具：').grid(row=0,column=0,pady=10)
    val = StringVar()
    val.set('绿水晶')
    Spinbox(win, values=('绿水晶','红宝石','生命水'), textvariable=val,command=typ).grid(row=0, column=1,pady=10)
    Label(win, text='购买数量').grid(row=1,column=0,pady=10)
    num=Spinbox(win, from_=1,to=5,command=pay)
    num.grid(row=1, column=1,pady=10)
    Label(win, text='限购5件').grid(row=1, column=2,pady=10)
    label=Label(win)
    label.grid(row=3,column=0,columnspan=3,pady=10)
    mon = 5
    win.mainloop()
elif testcode == '5.8':
    def show():
        info.insert('insert','\t时间：%s月%s日 %s\n' %(spmon.get(), spdat.get(),spwek.get()))
        pass
    win = Tk()
    win.title('留言本')
    mess = Label(win, text='请添加你的留言：').grid(row=0, column=0,columnspan=5,pady=10)
    spmon=Spinbox(win, from_=1, to=12, width=10)
    spmon.grid(row=1,column=0,pady=10)
    mon = Label(win, text='月').grid(row=1, column=1,pady=10)
    spdat=Spinbox(win, from_=1,to= 30 ,width=10)
    spdat.grid(row=1,column=2,pady=10)
    dat=Label(win, text='日').grid(row=1, column=3,pady=10)
    spwek=Spinbox(win,values=('星期一','星期二','星期三','星期四','星期五','星期六','星期日'),width=10)
    spwek.grid(row=1,column=5,columnspan=3,pady=10)
    info = Text(win, bg='#bfefff',width=50,height=10)
    get1=Button(win,text='提交',width=30,bg='#edb89e',command=show).grid(row=3,columnspan=10,pady=10)
    info.grid(row=2,columnspan=10)
    win.mainloop()
elif testcode == '5.9':
    subtest =2
    if subtest == 1:
        win = Tk()
        Scale(win, from_=1,to=12, resolution=1,orient=HORIZONTAL).pack()
        win.mainloop()
    elif subtest == 2:
        pass
        num = 0
        def up1():
            if scale1.get() < 50:
                val = scale1.get() +1
                scale1.set(val)
                num = val *5
                txt.config(text='爱心暴击'+str(num))
            pass
        def down1():
            if scale1.get() > 0:
                val = scale1.get() -1
                scale1.set(val)
                num = val *5
                txt.config(text='爱心暴击' + str(num))
            pass
        def hit(widget):
            num = scale1.get() * 5
            txt.config(text='爱心暴击' + str(num))
            pass
        win = Tk()
        win.title('爱心暴击')
        txt=Label(text='爱心暴击+0')
        txt.pack(side=TOP)
        btndonw = Button(win, text='-',command=down1, width=2).pack(side='left')
        scale1 = Scale(win, from_=0,to=50,resolution=1,orient=HORIZONTAL,showvalue=0,command=hit, troughcolor='#22ebbb')
        scale1.pack(side='left')
        num = Entry()
        btnup = Button(win, text='+', command=up1,width=2).pack(side='left')
        win.mainloop()
    else:
        pass
elif testcode == '6.1':
    subtest = 1
    if subtest == 1:
        def show():
            Label(win, image=img).pack()
            pass
        win = Tk()
        img = PhotoImage(file='laugth.png')
        but1 = Button(win, text='添加图片',command=show).pack()
        win.mainloop()
    elif subtest == 2:
        pass
    else:
        pass
elif testcode == '6.2':
    def num(a):
        val = pswshow.get()
        if len(val)< 13:
            pswshow.delete(0,END)
            pswshow.insert(0, val+' '+ a)
    def back():
        val = pswshow.get()
        if len(val) >= 1:
            pswshow.delete(len(val)-2,END)
            pswshow.config(text=val[0: len(val)-2])
    def enter():
        val = pswshow.get()
        win2 = Toplevel()
        if len(val) == 12:
            Label(win2, text='\n\n密码正确，请等待').pack()
        else:
            Label(win2, text='\n\n密码为6位数的数字').pack()
    win = Tk()
    win.title('密码输入器')
    pswshow = Entry(win, relief='solid',justify='center')
    but1 = Button(win, text='1', command=lambda :num('1'))
    but2 = Button(win, text='2', command=lambda: num('2'))
    but3 = Button(win, text='3', command=lambda: num('3'))
    but4 = Button(win, text='4', command=lambda: num('4'))
    but5 = Button(win, text='5', command=lambda: num('5'))
    but6 = Button(win, text='6', command=lambda: num('6'))
    but7 = Button(win, text='7', command=lambda: num('7'))
    but8 = Button(win, text='8', command=lambda: num('8'))
    but9 = Button(win, text='9', command=lambda: num('9'))
    but0 = Button(win, text='0', command=lambda: num('0'))
    back1 = PhotoImage(file='back.png')
    enter2 = PhotoImage(file='enter.png')
    butback=Button(win, image=back1, command=back)
    butok = Button(win, image=enter2, command=enter)
    pswshow.grid(row=1, columnspan=3)

    but1.grid(row=5,sticky=W+E)
    but2.grid(row=5, column=1,sticky=W + E)
    but3.grid(row=5, column=2,sticky=W + E)
    but4.grid(row=6, column=0,sticky=W + E)
    but5.grid(row=6, column=1, sticky=W + E)
    but6.grid(row=6, column=2, sticky=W + E)
    but7.grid(row=7, column=0, sticky=W + E)
    but8.grid(row=7, column=1, sticky=W + E)
    but9.grid(row=7, column=2, sticky=W + E)
    but0.grid(row=8, column=1, sticky=W + E)
    butback.grid(row=8, column=0, sticky=W + E,ipady=3)
    butok.grid(row=8, column=2, sticky=W + E,pady=3)
    win.mainloop()
elif testcode == '6.3':
# ==========================  2023-09-04    ===================================================
    subtest = 2
    if subtest == 1:
        win = Tk()
        vali = IntVar()
        vali.set('male')
        radio1 = Radiobutton(win, variable=vali, value='male',text='男').pack()
        radio2 = Radiobutton(win, variable=vali, value='famale',text='女').pack()
        win.mainloop()
    elif subtest == 2:
        def result1():
            if v.get() == 1:
                re.config(text='答错了，答案是小狗，因为旺旺仙贝')
            else:
                re.config(text='答对了，答案是小狗，因为旺旺仙贝')
            pass
        win = Tk()
        win.title('脑筋急转弯')
        win.geometry('300x150')
        text = Label(win, text='老师让小猫和小狗去背书，请问谁先背书呢？', font=14).pack(anchor = W)
        v = IntVar()
        ans1 = Radiobutton(win, text='小猫', variable=v,value=1, selectcolor='#f1d4c9')
        ans1.pack(anchor=W)
        ans2 = Radiobutton(win, text='小狗', variable=v, value=2, selectcolor='#f1d4c9')
        ans2.pack(anchor=W)
        button = Button(win, text='提交',command=result1, font=14,bg ='#f1c57e', relief='groove').pack()
        re = Label(win)
        re.pack()
        win.mainloop()
    else:
        pass
elif testcode == '6.4':
    def result1():
        print(v.get())
        if v.get() == 0:
            str = '答案：\n你自始至终就一副面孔，你讨厌两面派，也讨厌伪装，你觉得无论何时，做真实的自己最重要，所以你很少在乎别人的想法'
        elif v.get()==1:
            str = '答案：\n你有两副面孔，你很擅长伪装，在别人面前，你总是善良懂事，而人后缺不停的打着自己的小算盘'
        elif v.get() == 2:
            str = '答案：\n你有三幅面孔，在不同的时间段，你会展示不同的面孔，早上的时候心情美美，自然体贴善良，而中午遇到问题时，就冷脸相对，晚上时，你会彻底放松自己'
        else:
            str = '答案：\n你有四副面孔，面对不同的人就会有不同的面孔，例如在亲人、朋友、爱人面前，你给他们的印象都是不同的'
        re.config(text = str)
        pass
    win = Tk()
    win.title('心理测试题')
    str1 = ['一定会','很可能会','偶尔会','绝不会']
    Label(win, text='测试你的性格有几面',font=14).pack(anchor=W)
    text = Label(win, text='当你看不惯别人的某些行为时，你会直接指出吗？', font=14).pack(anchor = W)
    v =IntVar()
    for i in range(len(str1)):
        radio = Radiobutton(win, text=str1[i], variable=v, value=i, font=12, indicatoron=0, selectcolor='#00ffff')
        radio.pack(side=TOP, fill = X, padx=20,pady=3)
    button = Button(win, text='提交', command=result1, font=14,bg='#4cc6e3')
    button.pack(side=TOP, fill =X, padx=40,pady=20)
    re = Label(win, font=14,height=10, width=40, justify='left', wraplength=320)
    re.pack(side=TOP, pady=10)
    win.mainloop()
elif testcode =='6.5':
    subtest = 3
    if subtest == 1:
        win = Tk()
        val1 = IntVar()
        checkbox1 = Checkbutton(win, variable=val1, text='苹果').pack()
        val2 = IntVar()
        checkbox1 = Checkbutton(win, variable=val2, text='香蕉').pack()
        win.mainloop()
        pass
    elif subtest == 2:
        win = Tk()
        fruits = ('苹果','香蕉','草莓','百香果','牛油果')
        for i in fruits:
            val = IntVar()
            checkbox1 = Checkbutton(win, variable=val, text=i).pack(side=LEFT)
        win.mainloop()
        pass
    elif subtest == 3:
        def result1():
            sel=''
            for i in range(len(str1)):
                if (check[i].get() == 1):
                    sel = sel +str1[i] + ' '
            re.config(text=sel)
            pass
        win = Tk()
        win.title('调查问卷')
        str1 =['旅游','追剧上网','和亲友聚餐','户外健身']
        text = Label(win, text='适当的放松，有益身心健康',font=14).grid(row=0,column=0,columnspan=6)
        check=[]
        for i in range(len(str1)):
            v = IntVar()
            checkbox = Checkbutton(win, text=str1[i], variable=v,font=12,selectcolor='#00ffff',padx=5)
            checkbox.grid(row=1, column=i)
            check.append(v)
        button = Button(win, text='提交',command=result1, font=14,bg='#efb4de').grid(row=3,pady=6, columnspan=6)
        re = Label(win, font=12, height=5,width=50,bg='#cfcfcf')
        re.grid(row=4,columnspan=5)
        win.mainloop()
    else:
        pass
elif testcode == '7.1':
    subtest = 2
    if subtest == 1:
        win = Tk()
        items = ['苹果','香蕉','葡萄','梨','圣女果','百香果']
        listbox = Listbox(win, height=6, width=20,relief='solid')
        for i in items:
            listbox.insert(END,i)
        listbox.pack()
        win.mainloop()
        pass
    else:
        def show(event):
            for i in items:
                listbox.insert(END,i)
                listbox.pack(fill=X)
            pass
        win = Tk()
        win.title('listbox 初级使用：')
        win.geometry('180x150')
        listbox = Listbox(win, bg='#fff8dc', selectbackground='#d15fee',selectmode='multiple', height=5,width=25)
        items =['重庆','北京','天津','上海','广州','深圳']
        enc = Entry(win)
        enc.pack(fill=X)
        enc.bind('<Button-1>',show)
        win.mainloop()
        pass
elif testcode == '7.2':
    def show(ele):
        listbox.pack(fill=X)
        pass
    def typein(event):
        enc.delete(0, END)
        enc.insert(INSERT, listbox.get(listbox.curselection()))
        pass
    win = Tk()
    win.title('listbox 初级使用：')
    win.geometry('180x150')
    val = StringVar()
    val.set('重庆 北京 天津 上海 深圳')
    listbox = Listbox(win, bg='#fff8dc',selectbackground='#2c92df',selectmode='single',height=6,width=25,listvariable=val)
    enc = Entry(win)
    enc.pack(fill=X)
    enc.bind('<Button-1>',show)
    enc.bind('<Double-Button-1>', typein)
    win.mainloop()
elif testcode == '7.3':
    def add(from1, to1):
        # from1.curselection()  为获取选中的项的序号元祖
        item1 = from1.get(from1.curselection())  # 获取选中的项的内容
        to1.insert(END, item1)  # 在目标列表中插入选项
        from1.delete(from1.curselection())  # 删除原目标组中的该选项
    win = Tk()
    win.title('添加快捷键消息列表')
    win.geometry('250x200')
    Label(win, text='系统信号').grid(row=0,column=0)
    Label(win, text='快捷信号').grid(row=0,column=2)
    val1 = StringVar()
    val1.set('发起进攻 请求集合 小心草丛 跟着我')
    val2 = StringVar()
    val2.set('开始撤退 清理兵线 回防高地 请求支援')
    listbox1 = Listbox(win, bg = '#fff8dc',selectbackground='#d15fee',selectmode='single',listvariable=val1, height=8,width=10)
    listbox2 = Listbox(win, bg='#c1ffc1', selectbackground='#d15fee', selectmode='single', listvariable=val2, height=8,width=10)
    listbox1.grid(row =1,column=0,rowspan=2)
    listbox2.grid(row=1, column=2, rowspan=2)
    btn1 = Button(win, text='>>>',command=lambda :add(listbox1,listbox2))
    btn2 = Button(win, text='<<<', command=lambda: add(listbox2, listbox1))
    btn1.grid(row=1,column=1,padx=10)
    btn2.grid(row=2, column=1, padx=10)
    win.mainloop()
elif testcode == '7.4':
# ==========================  2023-09-05    ===================================================
    def gettext(event):
        str=''
        index1 = fruites.curselection()
        for item in index1:
            str += fruites.get(item) + '、'
            label.config(text='你选择了'+ str)
        pass
    win = Tk()
    win.configure(bg='#f5d7c4')
    win.geometry('240x240')
    label = Label(win, height=5, wraplength=190, justify='left', bg='#f1daa1', relief='groove')
    label.pack(side='top', fill='x',padx=10,pady=10)
    scr1 = Scrollbar(win)
    listitem = ['苹果','香蕉','草莓','樱桃','梨','柚子','菠萝','橘子','葡萄','柠檬','奇异果','百香果','牛油果','西瓜']
    fruites = Listbox(win, height=7, yscrollcommand=scr1.set, selectmode='multiple', justify='center',width=30)
    for i in listitem:
        fruites.insert(END, i)
    fruites.pack(side='left',fill='x')
    fruites.bind('<<ListboxSelect>>',gettext)
    scr1.config(command=fruites.yview)
    win.mainloop()
elif testcode == '7.5':
    subtest = 2
    if subtest == 1:
        win = Tk()
        val = StringVar()
        fruits=('苹果','香蕉','橘子','草莓')
        #optionmenu = OptionMenu(win, val, '苹果','香蕉','橘子','草莓')
        optionmenu = OptionMenu(win, val, *fruits)
        optionmenu.pack()
        win.mainloop()
        pass
    else:
        win = Tk()
        win.geometry('150x200')
        win.title('optionmenu的创建')
        Label(text='我的歌单：').pack(fill ='x',anchor='w')
        list = ('逞强--刘洋洋', '时间的过客--名爵', '情深几许--香子','我爱--袁维娅', '一个人挺好--梦颖', '世间美好--夏一涵', '念旧--阿悠悠')
        v = StringVar()
        om = OptionMenu(win, v, *list).pack(fill='x')
        win.mainloop()
        pass
elif testcode == '7.6':
    subtest = 3
    if subtest == 1:
        def result():
            if v.get() == items[2]:
                re.config(text='答对了')
            else:
                re.config(text='答错了')
            pass
        win = Tk()
        win.title('逻辑推理谁是小偷')
        win.configure(bg = '#ffffcc')
        text = Text(win, width=50, height=13, bg='#ffffcc',font=14,relief='flat')
        ques = ("一位警察，抓获四个嫌疑犯，张三、李四、王二、麻子，而他们的供词如下：\n\n张三说：不是我偷的。"
                "\n\n李四说：是张三偷的。\n\n王二说：不是我。\n\n麻子说：是李四偷的。\n\n他们四人只有一人说了真话，你知道谁是小偷吗？\n")
        text.insert(END, ques)
        text.grid(row=1, columnspan=4)
        text.config(state='disable')
        items = ('张三','李四','王二','麻子')
        v = StringVar()
        om = OptionMenu(win, v, *tems)
        om.grid(row=2, columnpppspan=2)
        button = Button(win, text='确定',command=result).grid(row = 2, column=1, columnspan=2)
        re =Label(win,padx=5, pady=5,width=60)
        re.grid(row=3, column=0, columnspan=3)
        win.mainloop()
    elif subtest == 2:
        from tkinter.ttk import *
        win = Tk()
        val = StringVar()
        fruits = ('苹果', '香蕉', '橘子', '草莓')
        # optionmenu = OptionMenu(win, val, '苹果','香蕉','橘子','草莓')
        optionmenu = OptionMenu(win, val, *fruits)
        optionmenu.pack()
        win.mainloop()
    else:
        from tkinter.ttk import *
        win = Tk()
        val = StringVar()
        fruits = ('苹果', '香蕉', '橘子', '草莓')
        # optionmenu = OptionMenu(win, val, '苹果','香蕉','橘子','草莓')
        Combobox(win, textvariable=val, values=fruits).pack(padx=10,pady=10)
        win.mainloop()
        pass
elif testcode == '7.7':
    subtest = 2
    if subtest == 1:
        from tkinter.ttk import *
        win = Tk()
        win.title('Combobox的创建')
        label1 = Label(win, text='选择管理员身份：').grid(row=1, column=0,columnspan=2,pady=10)
        item=('蓝色妖姬','烈焰焚情','寒冰幽兰','岁岁芳华','朝暮盈宵','陌上花开')
        useroption = Combobox(win, width=12, values=item)
        useroption.grid(row=1,column=2,pady=10)
        useroption.current(0)
        label2 = Label(win,text='查看类别：').grid(row=2,pady=10,columnspan=2)
        numberChosen = Combobox(win, width=12, values=('进销总览','销量','库存','进售价','账单'))
        numberChosen.grid(row=2, column=2,pady=10)
        numberChosen.current(0)
        button = Button(win, text='提交').grid(row=3, columnspan=4,pady=10)
        win.mainloop()
    elif subtest == 2:
        def set1():
            combobox1.set('128元钻石卡')
            pass
        def get1():
            str = combobox1.get()
            label.config(text='恭喜'+str+'办理成功')
            label.grid(row=2, column=0, columnspan=3)
            pass
        from tkinter.ttk import *
        win = Tk()
        Label(win, text='选择会员：').grid(row=0, column=0)
        val = StringVar()
        combobox1 = Combobox(textvariable=val)
        combobox1['values']=('38元会员银卡','58元会员金卡','88元会员白金卡','128元钻石卡')
        combobox1.grid(row=0,column=1,pady=10)
        Button(win, text='一键选择钻石会员', command=set1).grid(row=0, column=2)
        Button(win, text='提交', command=get1).grid(row=1, column=0,columnspan=3,pady=10)
        label = Label(win, foreground='red', font=14)
        win.mainloop()
    else:
        pass
elif testcode == '7.8':
    from tkinter.ttk import *
    def getMon(a):
        items = monOpiton.get()
        if items == '4' or items == '6' or items == '9' or items == '11':
            b = tuple(range(1,31))
        elif items == '2':
            b = tuple(range(1,29))
        else:
            b = tuple(range(1,32))
        dateOption['values'] = b
        pass
    def getDate():
        info = label3.cget('text')
        temp = monOpiton.get() + '月' + dateOption.get() + '日：\t' + text.get('0.0', END)
        label3.config(text=info + temp)
        text.delete('0.0',  END)
        pass
    win = Tk()
    win.title('添加日程')
    number = StringVar()
    a = tuple(range(1,13))
    monOpiton = Combobox(win, width=5, textvariable=number, values=a)
    monOpiton.current(0)
    monOpiton.grid(row=1, column=0, sticky='E', columnspan=2)
    monOpiton.bind('<<ComboboxSelected>>',getMon)
    label1 = Label(win,text='月').grid(row=1, column=2,sticky=W)
    b = tuple(range(1,32))
    dateOption = Combobox(win,width=5, values=b)
    dateOption.current(0)
    dateOption.grid(row=1, column=3, pady=10, columnspan=2)
    label2 = Label(win, text='日').grid(row=1, column=5,sticky='w')
    text = Text(win, width=40, height=10)
    text.grid(row=2, columnspan=8)
    button = Button(win, text='确定', command=getDate).grid(row=3, columnspan=8)
    label3 = Label(win)
    label3.grid(row=4, columnspan=8)
    win.mainloop()
elif testcode == '8.1':
    subtest = 1
    if subtest == 1:
        win = Tk()
        win.geometry('360x180')
        for i in range(6):
            if i %2 == 0:
                Frame(bg = '#b1ffbb',width=60, height=40,cursor='cross').grid(row=0,column=i,pady=10)
            else:
                Frame(bg='#ffd9c5',width=60,height=40,cursor='plus').grid(row=0,column=i,pady=20)
        win.mainloop()
    else:
        win = Tk()
        win.geometry('360x120')
        box = Frame(width=100, height=100, relief='groove',borderwidth=5)
        box.grid(row=0, column=0,pady=10,padx=10)
        txt= '小明去钓鱼，结果6条无头，8条只有半个身子，9条无尾巴，请问小明一共钓了几条鱼？'
        Label(box, text=txt, wraplength=320,justify='left',font=14).grid(columnspan=4)
        select=['8条','6条','9条','0条']
        val = IntVar()
        for i in range(len(select)):
            Radiobutton(box,text=select[i], value=i, variable=val).grid(row=1,column=i)
        win.mainloop()
elif testcode == '8.2':
    from tkinter.ttk import *
    win = Tk()
    win.title('长春市轨道交通1号线')
    win.configure(background='#afebe5')
    sty1= Style()
    sty1.configure('BW.TLabel',foreground='#fff',background='red')
    sty2= Style()
    sty2.configure('BW.TFrame',background='#afebe5')
    win.geometry('250x200')
    win.configure(bg='#afebe5')
    left = Frame(win, style='BW.TLabel',width=260)
    left.pack(side=LEFT)
    Label(left, text='2020-03-08',background='red',foreground='#fff').pack()
    Label(left, text='06:49', background='red', foreground='#fff').pack()
    Label(left, text='星期一 sun', background='red', foreground='#fff').pack()
    Separator(left, orient=HORIZONTAL).pack(side=TOP, fill=X)
    Label(left, text='本站', background='red', foreground='#fff').pack(ipady=5)
    Label(left, text='解放大路', background='red', foreground='#fff').pack(ipady=5)
    Separator(left, orient=HORIZONTAL).pack(side=TOP, fill=X)
    Label(left, text='前进方向', background='red', foreground='#fff').pack(ipady=5)
    Label(left, text='东环城路', background='red', foreground='#fff').pack(ipady=5)
    right = Frame(win, width=260,style='BW.TFrame')
    right.pack(side=LEFT)
    Label(right, text='请排队上下车先下后上',background='#aebbe5',justify='center',wraplength=100, font=16).pack(padx=40)
    win.mainloop()
elif testcode == '8.3':
    subtest = 2
    if subtest == 1:
        def all():
            print(checkbox)
            for index, item in enumerate(checkbox):
                item.set(True)
        def none():
            for inext, item in enumerate(checkbox):
                item.set(False)
        def inverse():
            for index, item in enumerate(checkbox):
                if item.get() == False:
                    item.set(True)
                else:
                    item.set(False)
        win = Tk()
        frame1 = Frame(win, width=200, height=50)
        frame1.grid(row=0, column=0)
        frame2 = Frame()
        frame2.grid(row=1,column=0)
        val = BooleanVar()
        val.set(1)
        radio1 = Radiobutton(frame1, value=0, variable=val, text='全选',command=all)
        radio1.grid(row=0, column=0)
        radio2 = Radiobutton(frame1, value=1, variable=val, text='全不选',command=none)
        radio2.grid(row=0, column=1)
        radio3 = Radiobutton(frame1, value=2, variable=val, text='反选', command=inverse)
        radio3.grid(row=0, column=3)
        fruits = ['苹果', '香蕉','苹果','草莓','柠檬']
        checkbox = []
        for index, item in enumerate(fruits):
            str = BooleanVar()
            str.set(False)
            Checkbutton(frame2, text=item, variable=str).grid(row=index+1, column=1)
            checkbox.append(str)
        win.mainloop()
    else:
        win = Tk()
        labelframe = LabelFrame(win, text='选择你的出站英雄')
        labelframe.grid(row=0,ipadx=10,ipady=10,column=1)
        hero = StringVar()
        hero.set('貂蝉')
        Radiobutton(labelframe, variable=hero, text='貂蝉',value='貂蝉').grid(row=1, column=1)
        Radiobutton(labelframe, variable=hero, text='吕布', value='吕布').grid(row=2, column=1)
        Radiobutton(labelframe, variable=hero, text='小乔', value='小乔').grid(row=3, column=1)
        Radiobutton(labelframe, variable=hero, text='周瑜', value='周瑜').grid(row=4, column=1)
        win.mainloop()
elif testcode == '8.4':
    def duihuan():
        txt = entry.get()
        if len(txt)> 0:
            re.config(text='兑换成功！')
        else:
            re.config(text='兑换码无效')
        re.grid(row=4, column=2)
    win = Tk()
    win.geometry('270x220')
    labelframe = LabelFrame(win, text='礼品兑换', bg='#fff5d7',padx=20,pady=10,font=14)
    labelframe.grid(row=0,ipadx=10,ipady=10,column=1)
    img = PhotoImage(file=r'.\pict\cat.png')
    Label(labelframe, image=img, bg='#fff5d7').grid(row=1, column=2)
    Label(labelframe, text='兑换码',bg='#fff5d7').grid(row=2, column=1,pady=10)
    entry=Entry(labelframe)
    entry.grid(row=2, column=2,pady=10)
    Button(labelframe,text='确认对换',borderwidth=1,bg='#4eb1ff',command=duihuan).grid(row=3, column=2)
    re = Label(labelframe, bg='#fff5d7',font=16,fg='red')
    win.mainloop()
elif testcode == '8.5':
    subtest = 2
    if subtest == 1:
        def creat():
            top = Toplevel()
            top.geometry('150x150')
            top.title('创建顶层窗口')
            top.configure(bg='#d8ebb8')
            Label(top, text='这是toplevel组件窗口').pack()
            pass
        win1 = Tk()
        win1.geometry('200x200')
        win1.configure(bg='#f7d7c4')
        Button(win1, text='创建顶层窗口', command=creat).pack()
        win1.mainloop()
    else:
        def begin():
            win2 = Toplevel()
            win2.geometry('200x120')
            win2.configure(bg='#ffacab')
            win2.title('准备游戏')
            Label(win2, text='玩家已就位，请准备', font=14,bg='#ffacab').pack(pady=50)
            pass
        def change():
            win2 = Toplevel()
            win2.geometry('200x120')
            win2.configure(bg='#ffacab')
            win2.title('2号棋牌室')
            Label(win2, text='欢迎进入2号棋牌室', font=14, bg='#ffacab', width=35).pack(side='top',fill=X)
            Label(win2, text='玩家已就位，请准备', font=16, bg='#ffacab', width=35).pack(pady=20,side='top', fill=X)
            pass
        win1 = Tk()
        win1.geometry('270x220')
        win1.title('1号棋牌室')
        win1.configure(bg='#ffcd63')
        label=Label(win1, text='欢迎进入1号棋牌室',background='#fffbb5',font=14,width=35)
        label.grid(row=0, column=0, columnspan=5, ipady=8)
        btn1 = Button(win1, text='开始对局',background='#35a837', command=begin)
        btn1.grid(row=2, column=1,pady=10)
        btn2 = Button(win1, text='更换房间', background='#ff4a4f', command=change)
        btn2.grid(row=2, column=3,pady=10)
        win1.mainloop()
elif testcode == '8.6':
    panewindow = PanedWindow(sashrelief= SUNKEN, background='#1df5df',width=200)
    panewindow.pack()
    btn1 = Button(panewindow, text='左侧按钮', state='disabled')
    panewindow.add(btn1)
    btn2 = Button(panewindow, text='右侧按钮', state='disabled')
    panewindow.add(btn2)
    mainloop()
elif testcode == '8.7':
    from tkinter.ttk import *
    win = Tk()
    win.title('日期和时间')
    note = Notebook(win, width=250, height=150)
    pane1 = Frame()
    Button(pane1, text='更改日期时间').pack(pady=20)
    pane2= LabelFrame()
    Checkbutton(pane2, text='显示此时钟', variable=StringVar()).pack(pady=20)
    pane3 = Frame()
    Button(pane3, text='更改设置').pack(pady=20)
    note.add(pane1, text='日期和时间')
    note.add(pane2, text='附加时钟')
    note.add(pane3, text='Internet时间')
    note.pack()
    win.mainloop()
elif testcode == '8.8':
    from tkinter.ttk import *
    win = Tk()
    note = Notebook(win, width=300, height= 200)
    pane1 = Frame()
    img1 = PhotoImage(file=r'pict\pane1.png')
    Label(pane1, image= img1).pack()
    Label(pane1, text='脑洞大不大，一问便知').pack(pady=20)
    Button(pane1, text='现在就玩', state='DISABLE').pack()
    pane2 = Frame()
    img2 = PhotoImage(file=r'pict\pane2.png')
    Label(pane2, image=img2).pack()
    Label(pane2, text='抽象派还是形象派，你到底是哪一派').pack(pady=20)
    Button(pane2, text='现在就玩', state='DISABLE').pack()
    note.add(pane1, text='最强的大脑')
    note.add(pane2, text='水泼墨画')
    note.pack()
    win.mainloop()
elif testcode == '9.1':
    i=0
    def mess():
        global i
        textleft = enc.get()
        Message(box, text=textleft, bg='#cbede9', width=140).grid(row=i,column=0,sticky=W)
        Message(box, text='你说：'+ textleft,bg='#fee2b8',width=140).grid(row=i+1, column=2)
        i+=2
        pass
    win = Tk()
    win.geometry('300x230')
    box = Frame(width=300, height=200)
    box.place(x=0,y=0)
    info = Frame(width=250, height=20)
    info.place(x=40,y=200)
    enc = Entry(info)
    enc.pack(side=LEFT, fill=BOTH)
    btn = Button(info, text='发送', command=mess).pack(side=LEFT)
    win.mainloop()
elif testcode == '9.2':
    def coll():
        a = randint(0, 6)
        mess.config(fg='#f00')
        if a==0:
            text = '恭喜获得敬业福一张'
        elif a == 1:
            text = '恭喜获得友善福一张'
        elif a == 2:
            text = '恭喜获得爱国福一张'
        elif a == 3:
            text = '恭喜获得和谐福一张'
        elif a == 4:
            text = '恭喜获得富强福一张'
        else:
            text = '很遗憾，什么都没有'
            mess.config(fg='#000')
        val.set('\n' + text + '\n')
        mess.pack()
    pass
    win = Tk()
    win.geometry('300x230')
    win.title('集福卡')
    val = StringVar()
    mess = Message(win, textvariable=val, font=14,aspect=350, fg='red')
    Button(win, text='集福卡', command=coll).pack(side=TOP)
    win.mainloop()
elif testcode == '9.3':
    def mess():
        showinfo('welcome', '好久不见，欢迎回归')
        pass
    from tkinter.messagebox import *
    win = Tk()
    Button(win, text='进入游戏', command=mess).pack(padx=20, pady=20)
    win.mainloop()
elif testcode == '9.4':
    from tkinter.messagebox import *
    def mess():
        showwarning('警告','您正在退出游戏，退出后所有积分将清零')
        pass
    win = Tk()
    win.title('警告会话框')
    Button(win, text='退出游戏', command=mess).pack(padx=20,pady=20)
    win.mainloop()
elif testcode == '9.5':
    from tkinter.messagebox import *
    def mess():
        showerror('错误提醒','游戏请求开启摄像头权限')
        pass
    win = Tk()
    win.title('警告会话框')
    Button(win, text='退出游戏', command=mess).pack(padx=20, pady=20)
    win.mainloop()
elif testcode == '9.6':
    def mess():
        boo = askokcancel('关闭提醒','您正在关闭窗口，点击确定可以关闭窗口')
        if boo == True:
            win.quit()
        pass
    win = Tk()
    win.title('关闭会话框')
    Button(win, text='关闭窗口', command=mess).pack(padx=20, pady=20)
    win.mainloop()
elif testcode == '9.7':
    def mess():
        boo = askyesno('关闭提醒','您正在关闭主窗口，点击确定可以关闭主窗口')
        if boo == True:
            win.quit()
        pass
    win = Tk()
    win.title('关闭会话框')
    Button(win, text='关闭窗口', command=mess).pack(padx=20, pady=20)
    win.mainloop()
elif testcode == '9.8':
    def mess():
        boo = askyesnocancel('退出提醒','您正在退出程序，点击‘是’可以退出程序，点击‘否’后台运行程序，点击‘取消’关闭会话框')
        if boo == True:
            win.quit()
        elif boo== False:
            win.iconify()
        pass
    win = Tk()
    win.title('退出会话框')
    Button(win, text='退出程序', command=mess).pack(padx=20, pady=20)
    win.mainloop()
elif testcode == '9.9':
    def mess():
        boo = askretrycancel('重试提醒','打开游戏出现错误，选择"重试"或"取消"')
        if boo == True:
            mess()
        else:
            win.quit()
        pass
    win = Tk()
    win.title('询问重试或取消会话框')
    Button(win, text='打开游戏', command=mess).pack(padx=20, pady=20)
    win.mainloop()
elif testcode == '10.1':
    win = Tk()
    win.title('为游戏窗口添加菜单')
    menu1 = Menu(win)
    menu1.add_command(label='游戏')
    menu1.add_command(label='帮助')
    menu1.add_command(label='退出')
    win.config(menu=menu1)
    win.mainloop()
elif testcode == '10.2':
    def help():
        showwarning('提醒','第四行')
        pass
    def game():
        boo = askyesnocancel('暂停','是否停止本游戏，点击是，重新开始，点击否，暂停游戏')
        if boo == True:
            i = 0
        else:
            i=84
        label.config(text=i)
        pass
    i = 84
    def wrong():
        global i
        i -=1
        label.config(text=i)
        pass
    def suc():
        top = Toplevel(win)
        Label(top, text='恭喜找到了\n得分为' + str(i), foreground='red').grid(row=0, column=0, padx=10, pady=10)
        pass
    win = Tk()
    win.title('为游戏窗口添加菜单')
    menu1 = Menu(win)
    menu1.add_command(label='游戏', command=game)
    menu1.add_command(label='帮助',command=help)
    menu1.add_command(label='退出',command=win.quit)
    win.config(menu=menu1)
    for c in range(6):
        for j in range(14):
            #if i == 3 and j ==3:
                #continue
            Button(win, text='大',width=2, command=wrong).grid(row=c, column=j)
    Button(win, text= '女',width=2,command=suc).grid(row=3,column=3)
    label = Label(win, font=14, foreground='red', text=84)
    label.grid(row=8, column=0, columnspan=14)
    win.mainloop()
elif testcode == '10.3':
    def pop1():
        menu2_2.post(win.winfo_x()+60,win.winfo_y()+120)
        pass
    win = Tk()
    menu1 = Menu(win)
    menu2_1 = Menu(menu1, tearoff=False)
    menu1.add_cascade(label='城市',menu=menu2_1)
    menu2_1.add_command(label='北京')
    menu2_1.add_command(label='上海')
    menu2_1.add_command(label='重庆')
    menu2_1.add_command(label='广州')
    menu2_1.add_command(label='深圳')
    menu1.add_command(label='修改',command=pop1)
    menu2_2=Menu(menu1, tearoff=False)
    menu2_2.add_command(label='添加城市')
    menu2_2.add_command(label='修改城市')
    menu1.add_command(label='退出',command=win.quit)
    win.config(menu=menu1)
    win.mainloop()
elif testcode == '10.4':
    def max_win(event):
        win.geometry('600x400')
        pass
    def normal_win(event):
        win.geometry('300x200')
        pass
    def txt():
        global val
        global font_size
        global top
        top = Toplevel(win)
        val = StringVar()
        val.set('宋体')
        font_family=('宋体','黑体','方正舒体','楷体','隶书','方正姚体')
        family = Combobox(top, textvariable=val, values=font_family)
        family.grid(row=0, column=0)
        font_size = Spinbox(top, from_=12, to=30, increment=2, width=10)
        font_size.grid(row=0, column=1)
        btn1 = Button(top, text='确定',command=font_set)
        btn1.grid(row=1, column=1)
        pass
    def font_set():
        font1 = (val.get(), font_size.get())
        label.config(font=font1)
        pass
    win = Tk()
    win.geometry('300x200')
    menu1 = Menu(win)
    menu2_1 = Menu(menu1)
    menu1.add_cascade(label='窗体', menu=menu2_1)
    menu2_1.add_command(label='最大化', accelerator='Ctrl+Up', command=lambda :max_win(''))
    menu2_1.add_command(label='中等窗口', accelerator='Ctrl+Down',command= lambda :normal_win(''))
    menu2_1.add_command(label='最小化', command=win.iconify)
    menu2_1.add_separator()
    menu2_1.add_command(label='关闭', command=win.quit)
    menu2_2 = Menu(menu1, tearoff=0)
    menu1.add_cascade(label='自定义', menu=menu2_2)
    menu2_2.add_command(label='字体设置', command=txt)
    win.config(menu=menu1)

    label = Label(win, text='这是一个窗口')
    label.grid(row=0, column=0)
    win.bind_all('<Control-Up>', max_win)
    win.bind_all('<Control-Down>', normal_win)
    win.mainloop()
elif testcode == '10.5':
    num = 0
    idiom = ['别出心裁', '白云苍狗', '暴虎冯河', '鞭长莫及']
    idiom_means = ['独出巧思，不同流俗', '比喻世事变化无常', '比喻有勇无谋，鲁莽冒险', '本意为马鞭子再长也打不到马肚子']

    def panduan():
        global num
        a = entry.get()
        if a == idiom[num]:
            num += 1
        if (num > len(idiom)):
            boo = askyesno('成功过关', '恭喜，已完成所有关卡，是否重新开始？')
            if boo == True:
                num = 0
                panduan()
            else:
                win.quit()
        entry.delete(0, END)
        means.config(text=idiom_means[num])
        level.config(text='第' + str(num + 1) + '关')

    def next(event):
        global num
        num += 1
        if (num >= len(idiom)):
            num = 0
        panduan()


    def restart(event):
        global num
        num = 0
        panduan()


    def show1():
        showinfo('游戏规则', '根据成语含义猜成语，正确则自动跳转至下一关')


    def tip():
        str = idiom[num][0]
        entry.delete(0, END)
        entry.insert(0, str)

    win = Tk()
    win.geometry('250x200')
    win.title('成语猜猜猜')
    menu1 = Menu(win)
    menu2_1 = Menu(menu1)
    menu1.add_cascade(label='游戏',menu=menu2_1)
    menu2_1.add_command(label='下一关', command= lambda :next(''), accelerator='Ctrl+N')
    menu2_1.add_command(label='重新开始', command= lambda :restart(''), accelerator='Ctrl+R')
    menu2_1.add_separator()
    menu2_1.add_command(label='退出', command=win.quit)
    menu2_2 = Menu(menu1)
    menu1.add_cascade(label='帮助',menu=menu2_2)
    menu2_2.add_command(label='游戏规则',command=show1)
    menu2_2.add_command(label='提示',command=tip)
    win.config(menu=menu1)

    level = Label(win, font=14, text='第1关')
    level.grid(row=0, column=0, columnspan=4, sticky=E)
    means = Label(win, text=idiom_means[0],font=14, width=30,background='#d8f3f0',wraplength=200)
    means.grid(row=1, column=0,pady=10,columnspan=4)
    entry =Entry(win, font=14)
    entry.grid(row=2, column=1, sticky=E)
    btn = Button(win, text='确定',command=panduan).grid(row=2, column=2)
    win.bind_all('<Control-n>',next)
    win.bind_all('<Control-r>', restart)
    win.mainloop()
elif testcode == '10.6':
    win = Tk()
    tree = Treeview(win, columns=('hero','type','operate'),show='headings',displaycolumns=(0,1,2))
    tree.heading('hero', text='英雄', anchor='center')
    tree.heading('type', text='类型', anchor='center')
    tree.heading('operate', text='操作难易程度', anchor='center')
    tree.insert('', END, values=('孙尚香','射手','5'))
    tree.insert('', END, values=('孙策','战士', '3'))
    tree.insert('', END, values=('大乔','辅助', '3'))
    tree.insert('', END, values=('小乔','法师', '3'))
    tree.pack()
    win.mainloop()
elif testcode == '10.7':
    subtest = 2
    if subtest == 1:
        win = Tk()
        tree = Treeview(win, columns=('date','temperature'))
        tree.heading('#0', text='天气')
        tree.heading('date', text='日期')
        tree.heading('temperature', text='气温')
        rain = PhotoImage(file=r'.\pict\rainheardly.png')
        storm = PhotoImage(file=r'.\pict\storm.png')
        sunny = PhotoImage(file=r'.\pict\sunny.png')
        tree.insert('', END, values=('4月1日', '-3~5'), image=rain, text='中到暴雨')
        tree.insert('', END, values=('4月2日', '-3~5'), image=sunny, text='晴')
        tree.insert('', END, values=('4月3日', '-3~5'), image=storm, text='雷阵雨')
        tree.insert('', END, values=('4月4日', '-3~5'), image=sunny, text='晴')
        tree.insert('', END, values=('4月5日', '-3~5'), image=sunny, text='晴')
        tree.insert('', END, values=('4月6日', '-3~5'), image=sunny, text='晴')
        tree.insert('', END, values=('4月7日', '-3~5'), image=rain, text='晴')
        tree.pack()
        win.mainloop()
    else:
        win = Tk()
        tree = Treeview(win)
        tree.heading('#0', text='皇帝')
        tree.insert('', 0, 'wei', text='魏')
        shu = tree.insert('',1,text='蜀')
        wu = tree.insert('', 2, text='吴')
        tree.insert('wei', 0, text='曹操')
        tree.insert(shu, 0, text='刘备')
        tree.insert(wu, 0, text='孙权')
        tree.pack()
        win.mainloop()
elif testcode == '10.8':
    win = Tk()
    #win.geometry('900x400')
    tree = Treeview(win, columns=('score'))
    tree.heading('#0', text='小组',anchor=W)
    score1={'R001':'20','R002':'19','R003':'19','R004':'16'}
    score2={'B001':'17','B002':'19','B003':'18','B004':'14'}
    score3 = {'G001': '17', 'G002': '15', 'G003': '16', 'G004': '16'}
    red = tree.insert('',END, text='红队',open=True)
    blue = tree.insert('', END, text='蓝队')
    green = tree.insert('', END, text='绿队')
    for index, item in score1.items():
        tree.insert(red, END, text=index, values=(item))
    for index, item in score2.items():
        tree.insert(blue, END, text=index, values=(item))
    for index, item in score3.items():
        tree.insert(green, END, text=index, values=(item))
    tree.pack()
    win.mainloop()
elif testcode == '10.9':
    def setdat(a):
        temp = monsel.get()
        if temp ==2:
            dat['value'] = tuple(range(1,29))
        elif temp ==4 or temp ==6 or temp ==9 or temp ==11:
            dat['value'] = tuple(range(1, 31))
        else:
            dat['value'] = tuple(range(1, 32))
        pass
    def get1():
        if len(entry.get())== 0:
            return False
        else:
            h = str(horsel.get()) if horsel.get() > 10 else '0'+str(horsel.get())
            m = str(minsel.get()) if minsel.get() > 10 else '0' + str(minsel.get())
            item1 = (str(mon.get()) + '月' + str(datsel.get()) + '日',h + ':' +m,entry.get())
            if not tree.focus() == '':
                tree.insert('', tree.index(tree.focus()),values=item1)
                del1()
            else:
                tree.insert('',END,values=item1)
            reset1()
        pass
    def del1():
        if tree.focus() == '':
            return False
        else:
            tree.delete(tree.focus())
        pass
    def edt(a):
        temp =tree.set(tree.focus())
        print(temp)
        print(temp['date'])
        d = temp['date'].split('月')
        t = temp['time'].split(':')
        monsel.set(int(d[0]))
        datsel.set(int(d[1].split('日')[0]))
        horsel.set(int(t[0]))
        minsel.set(int(t[1]))
        entry.delete(0, END)
        entry.insert(INSERT, temp['depart'])
        pass
    def reset1():
        monsel.set(1)
        datsel.set(1)
        horsel.set(0)
        minsel.set(0)
        entry.delete(0, END)
    win = Tk()
    frame = Frame()
    frame.grid()
    Label(frame, text='日期：').grid(row=0, column=0)
    monsel = IntVar()
    monsel.set(1)
    mon = Combobox(frame, value=tuple(range(1,13)), textvariable=monsel, width=5)
    mon.grid(row=0, column=1)
    mon.bind('<<ComboboxSelected>>',setdat)
    Label(frame, text='-').grid(row=0, column=2)
    datsel= IntVar()
    datsel.set(1)
    dat = Combobox(frame, value=tuple(range(1,32)), textvariable=datsel, width=5)
    dat.grid(row=0, column=3)
    Label(frame, text='时间：').grid(row=0, column=4,columnspan=2,sticky=S+E)
    horsel = IntVar()
    horsel.set(0)
    hor = Spinbox(frame, from_=0 ,to=24,width=5, textvariable=horsel)
    hor.grid(row=0, column=6)
    Label(frame, text=':').grid(row=0, column=7)
    minsel = IntVar()
    minsel.set(0)
    min = Spinbox(frame, from_=0, to=59, width=5, textvariable=minsel)
    min.grid(row=0 ,column=8)
    Label(frame, text='出发地：').grid(row=0, column=9)
    entry = Entry(frame)
    entry.grid(row=0, column=10)
    Button(frame, text='确定',command=get1).grid(row=0, column=11)
    Button(frame, text='删除', command=del1).grid(row=0, column=12)

    tree = Treeview(win, column=('date','time','depart'),show='headings')
    tree.heading('date', text='日期')
    tree.heading('time', text='时间')
    tree.heading('depart', text='出发地')
    tree.grid(row=1, column=0)
    tree.bind('<<TreeviewSelect>>', edt)
    win.mainloop()
elif testcode == '11.1':
    subtest = 2
    if subtest == 1:
        win = Tk()
        Progressbar(win, value=50).pack(pady=10)
        win.mainloop()
    else:
        val = 0
        def add1(c):
            global  val
            val += c
            if val > pro['max']:
                label.config(text='我吃饱了')
            else:
                vari.set(val)
            pass
        win = Tk()
        win.geometry('220x190')
        Label(win, text='投食：').grid(row=0, column=0, columnspan=1)
        Button(win, text='大鱼', command=lambda : add1(2)).grid(row=0, column=1,pady=10)
        Button(win, text='小鱼', command=lambda: add1(1)).grid(row=0, column=2, pady=10)
        img = PhotoImage(file=r'.\pict\cat.png')
        label=Label(win, imag=img, compound=TOP, foreground='red')
        label.grid(row=1, column=0, columnspan=4)
        vari = IntVar()
        vari.set(0)
        pro = Progressbar(win, mode='determinate', variable=vari, max=50, length=200)
        pro.grid(row=2, column=0, columnspan=4, pady=5)
        win.mainloop()
        pass
elif testcode == '11.2':
    def rego():
        pro.stop()
        pro.step(5)
        pro.start()
        pass
    win = Tk()
    win.title('灵魂画师')
    img = PhotoImage(file=r'.\pict\game.png')
    label=Label(win, image=img, text='灵魂画师',foreground='red',font=('华文新魏', 18), compound=BOTTOM)
    label.grid(row=1, column=0, columnspan=3)
    pro = Progressbar(win, mode='determinate', value=0, max=100, length=100)
    pro.grid(row=2, column=0 ,columnspan=3, pady=10)
    Button(win, text='进入游戏',command=pro.start, width=7).grid(row=4, column=0,padx=5)
    Button(win, text='游戏加速', command=rego, width=7).grid(row=4, column=1, padx=5)
    Button(win, text='停止加载', command=pro.stop, width=7).grid(row=4, column=2, padx=5)
    win.mainloop()
elif testcode == '11.3':
    win = Tk()
    win.title('灵魂画师')
    img = PhotoImage(file=r'.\pict\game.png')
    label=Label(win, image=img, text='灵魂画师',foreground='red',font=('华文新魏', 18), compound=BOTTOM).pack(pady=5)

    pro = Progressbar(win, mode='indeterminate', value=0, max=100, length=200)
    pro.pack(pady=10)
    Button(win, text='进入游戏',command=pro.start(40), width=7).pack()
    win.mainloop()
elif testcode == '12.1':
    win = Tk()
    win.title('创建canvas画布')
    win.geometry('300x200')
    canvas = Canvas(win, width=200, height=200, bg='#efefa3').pack()
    win.mainloop()
elif testcode == '12.2':
    win = Tk()
    win.title('创建canvas画布')
    win.geometry('300x200')
    canvas = Canvas(win, width=200, height=200)
    line1 = (14,65,66,65,83,19,99,64,148,64,111,96,126,143,83,113,44,142,58,97,14,65)
    line1 = canvas.create_line(*line1,fill='red')
    canvas.pack()
    win.mainloop()
elif testcode == '12.3':
    '''
    def up1(event):

        canvas.move(rect, 0 ,-2)
        pass
    def down1(event):

        canvas.move(rect,0,2)
        pass
    def left1(event):

        canvas.move(rect, -2,0)
        pass
    def right1(event):

        canvas.move(rect,2,0)
        pass       
    win = Tk()
    win.title('键盘控制矩阵移动')
    win.geometry('300x200')
    canvas = Canvas(win, width=200, height=200, relief='solid')
    rect = canvas.create_rectangle(10,10, 50,50,fill = '#c8f7f2')
    canvas.pack()
    win.bind('<Up>', up1)
    win.bind('<Down>',down1)
    win.bind('<Left>', left1)
    win.bind('<Right>', right1)
    win.mainloop()
    '''
#  _*_ coding:utf-8 _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 文件名称：demo1.py
# 开发工具：PyCharm
# canvas绘制矩形


    def up1(event):
        # move方法实现rect向上移动两个单位
        canvas.move(rect, 0, -2)


    def down1(event):
        # move方法实现rect向下移动两个单位
        canvas.move(rect, 0, 2)


    def left1(event):
        # move方法实现rect向左移动两个单位
        canvas.move(rect, -2,0 )


    def right1(event):
        # move方法实现rect向右移动两个单位
        canvas.move(rect, 2,0 )


    from tkinter import *

    win = Tk()
    win.title("键盘控制矩形移动")
    win.geometry("300x200")
    canvas = Canvas(win, width=200, height=200, relief="solid")  # 创建画布
    rect = canvas.create_rectangle(10, 10, 50, 50, fill="#C8F7F2") # 绘制矩形
    canvas.pack()

    win.bind("<Up>", up1)      # 绑定键盘事件
    win.bind("<Down>", down1)
    win.bind("<Left>", left1)
    win.bind("<Right>", right1)
    win.mainloop()
elif testcode == '12.4':
    subtest = 2
    if subtest == 1:
        win = Tk()
        win.title('绘制人脸')
        win.geometry('300x200')
        canvas = Canvas(win, width=200, height=200, relief='solid')
        cir1 = canvas.create_oval(34, 68, 143, 127, fill='#c8f7f2')
        cir2 = canvas.create_oval(59, 83, 71, 99, fill='#e6f1b7')
        cir2_1 = canvas.create_oval(61, 86, 71, 94, fill='#000000')
        cir3 = canvas.create_oval(101, 83, 113, 99, fill='#e6f1b7')
        cir3_1 = canvas.create_oval(100, 86, 109, 94, fill='#000000')
        canvas.pack()
        win.mainloop()
    else:
        win = Tk()
        win.title('绘制圆弧')
        win.geometry('300x200')
        canvas = Canvas(win, width=500, height=400, relief='solid')
        canvas.create_arc(20, 40, 150, 150, extent=120, outline='#EBD17a',start=30,width=2,style=ARC)
        canvas.create_arc(170, 40, 300,150, extent=120, outline='#edb17a',start=30,width=2,style=CHORD)
        canvas.create_arc(320, 40,450,150,extent=120,outline='#edb17a',start=30, width=2,style=PIESLICE)
        canvas.pack()
        win.mainloop()
        pass
elif testcode == '12.5':
    win = Tk()
    win.title('绘制西瓜')
    win.geometry('300x200')
    canvas = Canvas(win,width=200,height=200, relief='solid')
    arc1 = canvas.create_arc(40,40,150,150,extent=-180,fill='#e95121',outline='#73f18b',width=5)
    line = canvas.create_line(42,94,148,94,width=7, fill='#e95121')
    cir1 = canvas.create_oval(95,95,100,100, fill='#000000')
    cir2 = canvas.create_oval(70, 97, 75, 102, fill='#000000')
    cir3 = canvas.create_oval(95, 125, 100, 130, fill='#000000')
    cir4 = canvas.create_oval(65, 125, 70, 130, fill='#000000')
    cir5 = canvas.create_oval(125, 110, 130, 115, fill='#000000')
    canvas.pack()
    win.mainloop()
elif testcode == '12.6':
    win = Tk()
    win.title('绘制西瓜形状的雪糕')
    win.geometry('300x200')
    canvas = Canvas(win, width=500, height=400, relief='solid')
    canvas.create_line(95, 124, 95, 194,fill='#e9d39d', capstyle=ROUND, width=12)
    canvas.create_arc(5, -70, 185,162,extent=-40, outline='#32e143',fill='#32e143',start=-70,width=2,style=PIESLICE)
    canvas.create_arc(8,-67, 181,155,extent=-40, outline='#e29724',fill='#e29724',start=-70, width=2,style=PIESLICE)
    canvas.create_arc(92,74,97,79,extent=159, fill='#000',width=2,style=ARC)
    canvas.create_arc(97, 94, 102, 99, extent=180,start=90, fill='#000', width=2, style=ARC)
    canvas.create_arc(110, 124, 113, 127, extent=359, fill='#000', width=2, style=ARC)
    canvas.create_arc(90, 134, 93, 137, extent=359, fill='#000', width=2, style=ARC)
    canvas.pack()
    win.mainloop()
elif testcode == '12.7':
    win = Tk()
    win.title('绘制松鼠')
    win.geometry('240x260')
    canvas = Canvas(win, width=250, height=250, relief='solid')
    poly1  = canvas.create_polygon(27,8,27,62,54,34,fill='#fbfe0d')
    poly2 = canvas.create_polygon(54, 34, 81, 8, 81, 63, fill='red')
    poly3 = canvas.create_polygon(81,63,54, 35, 25, 61, 53, 90, fill='#0001fc')
    poly4 = canvas.create_polygon(81, 63, 81, 176, 138, 121, fill='#32ccfe')
    poly5 = canvas.create_polygon(81, 97, 43, 135, 81, 174, fill='#fdcbfe')
    poly6 = canvas.create_polygon(139, 119, 60, 198, 140, 198, fill='#02cd02')
    poly7 = canvas.create_polygon(140,198,167, 170, 233, 170, 196, 198, fill='#9b01ff')
    canvas.pack()
    win.mainloop()


else:
    print('not testcode number define')