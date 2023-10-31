a=int(input("Input a positive number:"))       #输入被开方数
x0 = a / 2;                               #任取的初值
x1 = (x0 + a / x0)                         #x0, x1; 分别代表前一项和后一项 
while abs(x1 - x0)>0.00001 :               #abs(x)函数用来求参数x绝对值
    x0 = x1
    x1 = (x0 + a / x0) / 2
print("The square root is：" , x0)













