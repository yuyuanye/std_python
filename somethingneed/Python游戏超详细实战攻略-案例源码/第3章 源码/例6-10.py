class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
   def __str__(self):					#重写print()方法，打印Vector对象实例信息
      return 'Vector (%d, %d)' % (self.a, self.b)
   def __add__(self,other): 			#重载加法+运算符
      return Vector(self.a + other.a, self.b + other.b)
   def __sub__(self,other): 				#重载减法-运算符
      return Vector(self.a - other.a, self.b - other.b)
#主程序
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
