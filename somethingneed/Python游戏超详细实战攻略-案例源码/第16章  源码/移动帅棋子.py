from tkinter import *

def callback():			#事件处理函数
    cv.move(rt1,150,150)         #移动rt1

root = Tk()
root.title('移动“帅”棋子')			#设置窗口标题
#创建一个Canvas，设置其背景色为白色 
cv = Canvas(root, bg = 'white', width = 260, height = 220) 
img1 = PhotoImage(file = '红帅.png')
cv.create_rectangle(40,40,190,190,outline='red',fill='green')
rt1 = cv.create_image((40,40),image=img1) 		#绘制“帅”棋子图片

cv.pack()
button1 = Button(root, text="移动棋子",command=callback,fg="red")
button1.pack()
def callback2():			#事件处理函数
    cv.delete(rt1)              #删除rt1
button2 = Button(root, text="删除棋子",command=callback2,fg="red")
button2.pack()
root.mainloop()



