def case4_1():
    import tkinter
    win = tkinter.Tk()
    win.title('我的第一个GUI程序')
    win.mainloop()

def case4_2():
    #from tkinter import *
    import tkinter
    win = tkinter.Tk()
    win.geometry('800x600')
    win.mainloop()
def case4_3():
    import tkinter
    root = tkinter.Tk()
    label = tkinter.Label(root, text='hello,python')
    label.pack()
    button1 = tkinter.Button(root, text='botton1')
    button1.pack(side =tkinter.LEFT)
    button2 = tkinter.Button(root, text='botton2')
    button2.pack(side=tkinter.RIGHT)
    root.mainloop()
def case4_4():
    import tkinter as tk
    root = tk.Tk()
    root.geometry('200x200+280+280')
    #print(help('tkinter.Tk.gemetry'))
    #root.geometry('+280+280')
    root.title('计算器示例')
    L1 = tk.Button(root, text='1', width=5,bg='yellow')
    L2 = tk.Button(root, text='2', width=5)
    L3 = tk.Button(root, text='3', width=5)
    L4 = tk.Button(root, text='4', width=5)
    L5 = tk.Button(root, text='5', width=5, bg='green')
    L6 = tk.Button(root, text='6', width=5)
    L7 = tk.Button(root, text='7', width=5)
    L8 = tk.Button(root, text='8', width=5)
    L9 = tk.Button(root, text='9', width=5, bg='yellow')
    L0 = tk.Button(root, text='0')
    Lp = tk.Button(root, text='.')
    L1.grid(row = 0, column= 0)
    L2.grid(row=0, column=1)
    L3.grid(row=0, column=2)
    L4.grid(row=1, column=0)
    L5.grid(row=1, column=1)
    L6.grid(row=1, column=2)
    L7.grid(row=2, column=0)
    L8.grid(row=2, column=1)
    L9.grid(row=2, column=2)
    L0.grid(row=3, column=0, columnspan=2,sticky=tk.E + tk.W)
    Lp.grid(row=3, column=2, sticky=tk.E + tk.W)
    root.mainloop()
def case4_5():
    import tkinter as tk
    root = tk.Tk()
    root.title('登陆')
    root['width'] = 200
    root['height'] = 80
    tk.Label(root,text='用户名',width=6).place(x=1,y=1)
    tk.Entry(root,width=20).place(x=45,y=1)
    tk.Label(root,text='密码',width=6).place(x=1,y=20)
    tk.Entry(root, width=20,show='*').place(x=45,y=20)
    tk.Button(root,text='登陆',width=8).place(x=40,y=40)
    tk.Button(root,text='取消',width=8).place(x=110,y=40)
    root.mainloop()
def main(test_num):
    if test_num == '1':
        case4_1()
        pass
    elif test_num == '2':
        case4_2()
        pass
    elif test_num == '3':
        case4_3()
        pass
    elif test_num == '4':
        case4_4()
        pass
    elif test_num == '5':
        case4_5()
        pass
    else:
        pass
if __name__ == '__main__':
    main('5')



