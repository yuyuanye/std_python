import random
class Person:
    num = 1
    def SayHello(self):
        print('hello')
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def __del__(self):
        print('析构函数，不存在了')
class People:
    num = 1
    def __init__(self, str, n):
        self.name = str
        self.age = n
    def SayHello(self):
        print('hello!')
    def Printname(self):
        print('my name is :',self.name)
    def Printnum(self):
        print('people num is:',People.num)
class Car:
    price = 10000
    def __init__(self,c ,w):
        self.color = c
        self.__weight = w
class Human:
    num = 0
    def __init__(self, str, n ,w):
        self.name = str
        self.age = n
        self.__weight = w
        Human.num += 1
    def __outputweight(self):
        print('体重:',self.__weight)
    def Printinfo(self):
        print('姓名:',self.name,'年龄：',self.age)
        self.__outputweight()
    def Printnum(self):
        print('amount number:',Human.num)
    @ staticmethod
    def getNum():
        return Human.num
class Man(object):
    def __init__(self,name='',age=20,sex='male'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
    def setName(self,name):
        if type(name) != str:
            print('name must be string')
            return
        self.name = name
    def setAge(self,age):
        if type(age) != int:
            print('age must be int')
            return
        self.__age = age
    def setSex(self,sex):
        if type(sex) != str:
            print('sex must be string')
            return
        self.__sex = sex
    def showinfo(self):
        print('name = ',self.name,', age =',self.__age,', sex =',self.__sex)
class Student(Man):
    def __init__(self, name='',age = 20, sex='male', school=2016):
        super(Student,self).__init__(name,age,sex)
        self.school = school
    def setschool(self,school):
        self.school = school
    def show(self):
        Man.showinfo(self)
        print('school year is:',self.school)
class Animal:
    def run(self):
        print('animal is running...')
class Cat(Animal):
    def run(self):
        print('cat is running...')
class Dog(Animal):
    def run(self):
        print('dog is running...')
def run_twice(something):
    something.run()
    something.run()

class Card():
    '''A playing card'''
    RANKS = ['A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','Q ','K ']
    SUITS = ['♣','♦','♥','♠']
    def __init__(self):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep
    def pic_order(self):
        if self.rank == 'A':
            FaceNum = 1
        elif self.rank == 'J':
            FaceNum = 11
        elif self.rank == 'Q':
            FaceNum = 12
        elif self.rank == 'K':
            FaceNum = 13
        else:
            FaceNum = int(self.rank)
        if self.suit == '♣':
            Suit = 1
        elif self.suit == '♦':
            Suit = 2
        elif self.suit == '♥':
            Suit = 3
        else:
            Suit = 4
        return (Suit - 1) * 13 + FaceNum
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand():
    '''A hand of playing cards'''
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep =''
            for card in self.cards:
                rep +=str(card) +'\t'
        else:
            rep ='无牌'
        return rep
    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class Poke(Hand):
    '''A deck of playing cards'''
    #cards = []
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add((rank+suit))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 13):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print('不能继续发牌了，牌已发完')
    #def add(self,card):
        #self.cards.append(card)

def main(case_num):
    if case_num == '1':
        someone = Person()
        someone.SayHello()
    elif case_num == '2':
        cplx_num = Complex(100,200)
        print('real part:',cplx_num.r,'\nimag part:',cplx_num.i)
    elif case_num == '3':
        cplx_num = Complex(100,200)
        print(cplx_num)
        print('first\n','real part:',cplx_num.r,'\nimag part:',cplx_num.i)
        del cplx_num
        print('second\n','real part:', cplx_num.r, '\nimag part:', cplx_num.i)
    elif case_num == '4':
        p1 = People('xiaohong', 33)
        p2 = People('damao', 55)
        p1.SayHello()
        p1.Printname()
        p2.SayHello()
        p2.Printname()
        p1.Printnum()
        People.num = 3
        p1.Printnum()
        p2.Printnum()
    elif case_num == '5':
        car1 = Car('red',10)
        car2 = Car('blue', 20)
        print('car1 color',car1.color)
        print('car1 weight1',car1._Car__weight)
        #print('car1 weight2', car1.__weight)
    elif case_num == '6':
        h1 = Human('daolang',42,120)
        h2 = Human('wangfeng',43,140)
        h1.Printinfo()
        h2.Printinfo()
        Human.Printinfo(h1)
        Human.Printinfo(h2)
        print('human number:',Human.getNum())
        print('h1 number:',h1.getNum())
    elif case_num == '7':
        '''
        m1 = Man('qingang', 52,'male')
        m1.showinfo()
        m1.name = 'lishangfu'
        m1.showinfo()
        m1.setAge(70)
        m1.showinfo()
        m1._Man__age = 80
        m1.showinfo()
        '''
        s1 = Student()
        s1.show()
        s1.setAge(10)
        s1.show()
        s1.setschool(2023)
        s1.show()
    elif case_num == '8':
        ani = Animal()
        #ani.run()
        cat = Cat()
        #cat.run()
        dog = Dog()
        #dog.run()
        '''
        print(isinstance(dog, Animal))
        print(isinstance(dog, Cat))
        print(isinstance(dog,Dog))
        '''
        #print(isinstance(ani, Dog))
        run_twice(ani)
        run_twice(cat)
        run_twice(dog)
        pass
    elif case_num == '9':
        print('this is a module with classes for playing cards')
        players = [Hand(),Hand(),Hand(),Hand()]
        poke1 = Poke()
        poke1.populate()
        poke1.shuffle()
        poke1.deal(players,13)
        n = 1
        for hand in players:
            print('player',n, end=':')
            print(hand)
            n=n+1
    elif case_num == '10':
        from itertools import combinations
        from itertools import permutations
        test_data = ['a','b','c','d']
        '''
        print('2个元素的组合：')
        for i in combinations(test_data, 2):
            print(i, end=',')
        print('\n3个元素的组合：')
        for i in combinations(test_data, 3):
            print(i, end=',')
        '''
        print('2个元素的排列：')
        for i in permutations(test_data, 2):
            print(i, end=',')
        print('\n3个元素的排列：')
        for i in permutations(test_data, 3):
            print(i, end=',')
        pass
if __name__ == '__main__':
    main('10')


