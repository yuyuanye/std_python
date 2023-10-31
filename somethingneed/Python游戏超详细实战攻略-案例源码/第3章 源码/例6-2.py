【例6-2】定义一个复数类Complex，构造函数完成对象变量初始化工作。
class Complex:
    def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart
x = Complex(3.0,-4.5)
print(x.r, x.i)

