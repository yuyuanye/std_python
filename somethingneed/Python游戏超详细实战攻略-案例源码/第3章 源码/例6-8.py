#定义基类：Person类
import types
class Person(object): #基类必须继承于object，否则在派生类中将无法使用super()函数
    def __init__(self, name = '', age = 20, sex = 'man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
    def setName(self, name):
        if type(name) != str:		#内置函数type( )返回被测对象的数据类型
            print ('姓名必须是字符串.')
            return
        self.__name = name
    def setAge(self, age):
        if type(age) != int:
            print ('年龄必须是整型.')
            return
        self.__age = age
    def setSex(self, sex):
        if sex != '男' and sex != '女':
            print ('性别输入错误')
            return
        self.__sex = sex
    def show(self):
        print ('姓名：', self.__name, '年龄：', self.__age ,'性别：', self.__sex)
#定义子类（Student类），其中增加一个入学年份私有属性（数据成员）。
class Student (Person):
    def __init__(self, name='', age = 20, sex = 'man', schoolyear = 2016):
        #调用基类构造方法初始化基类的私有数据成员
        super(Student, self).__init__(name, age, sex) 
        #Person.__init__(self, name, age, sex) 	#也可以这样初始化基类私有数据成员
        self.setSchoolyear(schoolyear) 			#初始化派生类的数据成员
    def setSchoolyear(self, schoolyear):
        self.__schoolyear = schoolyear
    def show(self):
        Person.show(self)					#调用基类show()方法
        #super(Student, self).show()			#也可以这样调用基类show()方法
        print ('入学年份：', self.__schoolyear)
#主程序
if __name__ =='__main__':
    zhangsan = Person('张三', 19, '男')
    zhangsan.show()
    lisi = Student ('李四', 18, '男', 2015)
    lisi.show()
    lisi.setAge(20) 				#调用继承的方法修改年龄
    lisi.show()

