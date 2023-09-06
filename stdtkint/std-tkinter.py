
#==========================  2023-09-02    ===================================================
from tkinter import *
testcode = '8.1'
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
    win = Tk()
    win.geometry('360x180')
    for i in range(6):
        if i %2 == 0:
            Frame(bg = '#b1ffbb',width=60, height=40,cursor='cross').grid(row=0,column=i,pady=10)
        else:
            Frame(bg='#ffd9c5',width=60,height=40,cursor='plus').grid(row=0,column=i,pady=20)
    win.mainloop()

else:
    print('not testcode number define')