【例6-6】公有方法、私有方法、静态方法的定义和调用。
class Fruit:
    price=0
    def __init__(self):
        self.__color='Red'				#定义和设置私有属性color
        self.__city='Kunming'			#定义和设置私有属性city
    def __outputColor(self):			#定义私有方法outputColor
        print(self.__color)				#访问私有属性color
    def __outputCity(self):				#定义私有方法outputCity
       print(self.__city)				#访问私有属性city
    def output(self):					#定义公有方法output
        self.__outputColor( )			#调用私有方法outputColor
        self.__outputCity( )			#调用私有方法outputCity
    @ staticmethod
    def getPrice():					#定义静态方法getPrice
         return Fruit.price
    @ staticmethod
    def setPrice(p):					#定义静态方法setPrice
        Fruit.price=p
#主程序
apple=Fruit()
apple.output() 
print(Fruit.getPrice( ))
Fruit.setPrice(9)
print(Fruit.getPrice( ))




