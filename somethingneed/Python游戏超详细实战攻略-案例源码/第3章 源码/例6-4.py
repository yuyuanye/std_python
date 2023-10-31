【例6-4】为Car类动态增加属性name和成员方法setSpeed()。
import types			 			#导入types模块
class Car:
    price = 100000 				 #定义类属性price
    def __init__(self, c):
        self.color = c				 #定义实例属性color
#主程序
car1 = Car("Red")
car2 = Car("Blue")
print(car1.color, Car.price)
Car.price = 110000					 #修改类属性
Car.name = 'QQ'					 #增加类属性
car1.color = "Yellow"				 #修改实例属性
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)
def setSpeed(self, s):
    self.speed = s
car1.setSpeed = types.MethodType(setSpeed, Car)    #动态为对象增加成员方法
car1.setSpeed(50)                              #调用对象的成员方法
print(car1.speed)


