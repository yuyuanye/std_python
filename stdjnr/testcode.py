import keyword
import random
import re
import math
#print(keyword.kwlist)
#print('what should i do ?')
#charis = input('please input someting char ')
#print(charis+' asc code is ',ord(charis))
'''
myname='生化危机'
print(type(myname))
tase = myname = 100
print(type(myname))
print(id(myname))
print(id(tase))
'''
'''
a = 0x33
print(type(a))
print(a)
'''
'''
heith = 1.78
print('您的身高',heith)
print('您的身高'+str(heith))
print(bin(10))
'''
#print('a '*20)
'''
day= input('please input week day')
if day == 'mon' or day == 'tus':
    print('this is mon or tus')
else:
    print('not these day')
'''
verse =['nihao' ,'beijing', 'huanying', 'nimen']
other = ['beijing','shangbai','guangzhou','shenzhen',23,['tianxia', 28]]
numeg = [1,3,5,6,9,76]
'''
print(verse[0])
print(verse[-1])
print(verse[-2])
print(verse[0:3:2])
print(verse[0:2])
'''
#print(verse + other)
#print(verse * 3)
#print('beijing' in verse)
#print('zhongguo' in verse)
#print(len(verse))
#print(max(numeg))
#print(sum(numeg))
#print(min(numeg))
#numsort = numeg.sort()
#print(numsort)
'''
abc = list(range(10, 20 ,2))
del abc
print(abc)
'''
#print(other)
#for item in other:
#    print(item)
#for index,item in enumerate(other):
#    print(index,item)
#other.append('what')

#other.extend(verse)
'''
print(verse)
verse[2] = 'replace'
print(verse)
del verse[1]
print(verse)
'''
team = [1,2, 3, 4, 5, 8, 1, 3, 2, 3]
'''
if team.count(3) > 0:
    print(team.count(3))
else:
    print('no count')
'''
#pos = team.index(3)
#print(pos)
#print(sum(team))
#print(sum(team[:3]))
#stable = sorted(team,reverse=True)
#verse.sort(key=str.lower)
#print(stable)
#print(team)
#print(verse)
#randomnum = [random.randint(10,100) for i in range(10)]
#print(randomnum)
'''
price = [100.33,300,500.88,800,1000]
sale = [int(0.5*x) for x in price if x > 300]
print(price)
print(sale)

verse1 = ('champion')
print(type(verse1))
verse2 = ('champion',)
print(type(verse2))

creat = tuple(range(10,20,2))
print(creat)
case2 = (['name','famliy'],30,80,3.14)
#print(creat+case2)
case2= (10,20,30,40)
print(case2[:3])
'''
#randomnum = [random.randint(10,100) for i in range(10)]
#print(tuple(randomnum))
'''
number = (i for i in range(4))
for i in number:
    print(i,end=" ")
print(tuple(number))

mot_en = 'long time no see'
mot_cn = 'how do you do ?'
print(mot_en +'----'+ mot_cn)
'''
strmy = "   人生苦短，必须>>>性 感 - what?www.baidu.com   ,"
#print(len(strmy))
#length = len(strmy.encode('gbk'))
#print(length)
#print(strmy[2:15:2])
'''
substr1 = strmy[1]
substr2 = strmy[5:]
substr3 = strmy[:5]
substr4 = strmy[2:5]
print(substr1)
print(substr2)
print(substr3)
print(substr4)

try:
    substr1 = strmy[30]
except IndexError:
    print('index not exist')

list1 = strmy.split()
list2 = strmy.split('>>>')
list3 = strmy.split('.')
list4 = strmy.split(' ',4)
list5 = strmy.split('>')
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

print(strmy.count('.'))
print(strmy.find('.'))
print(strmy.index('.'))

print(strmy.startswith('人'))
print(strmy.endswith('nom'))

stru = 'UPLOAD'
strd = 'download'
print(stru.lower())
print(strd.upper())

print(strmy)
print(strmy.strip())
'''
'''
print(strmy.lstrip())
print(strmy.rstrip(','))
'''
'''
template = '编号：{:0>9s}\t公司名称： {:s}\t官网:http//www.{:s}.com'
context1 = template.format('7','百度','baidu')
context2 = template.format('8','腾讯','tecent')
print(context1)
print(context2)
'''
pattern = r'mr_\w+'
string = 'Mr_shop mr_shop'
'''
match = re.match(pattern,string,re.I)
print(match)
stri1 = 'actMr_shop mr_shop'
match = re.match(pattern,string,re.I)
print(match.start())
print(match.end())
print(match.span())
print(match.string)
print(match.group())

match = re.search(pattern,string,re.I)
print(match)
print(match.start())
print(match.end())
print(match.span())
print(match.string)
print(match.group())
stri1 = 'actMr_shop mr_shop'
match = re.search(pattern,stri1,re.I)
print(match.start())
print(match.end())
print(match.span())
print(match.string)
print(match.group())

match = re.findall(pattern,string,re.I)
print(match)

stri1 = '你好Mr_shop mr_shop'
match = re.findall(pattern,stri1,re.I)
print(match)

pattern = r'[0-9]{1,3}(\.[0-9]{1,3}){3}'
str1 ='127.0.0.1 192.168.1.66'
match = re.findall(pattern,str1)
print(match)

pattern = r'1[3456]\d{9}'
string = '13099036223'
result = re.sub(pattern,'1xxxxxxxx',string)
print(result)

pattern = r'[?|&]'
url = 'http://www.baidu.com/?/what is this & this is elephent'
result = re.split(pattern,url)
print(result)

number = int(input('please enten 6 ticket number:'))
if number == 123456:
    print(number, 'you win')
if number != 123456:
    print(number, 'sorry,good luck next time')

data = 65
if data > 100:
    print(date,'is b good')

number = int(input('please enten 6 ticket number:'))
if number == 123456:
    print(number, 'you win')
else:
    print(number, 'sorry,good luck next time')

a = 9
b = a if a > 0 else -a
print(a,b)
'''
#number = int(input('please enten 6 ticket number:'))
'''
if number > 1000:
    print('number bigger than 1000')
elif number > 500:
    print('number samll than 1000, bigger than 500')
elif number > 200:
    print('number samll than 500, bigger than 200')
else:
    print('number samll than 200')
'''
'''
if number > 1000:
    print('number bigger than 1000')
else:
    if number > 500:
        print('number samll than 1000, bigger than 500')
    else:
        if number > 200:
            print('number samll than 500, bigger than 200')
        else:
            print('number samll than 200')
'''
'''
if number % 3 == 2 or number % 5 == 3 or number % 7 ==2:
    print('it\'s number')
else:
    print('not number')
    print('it\'s number')

a =''
if not a:
    print('it\'s a')
else:
    print('it\'s b')
'''
'''
for i in [1, 2, 3]:
    print('大笑江湖')
'''
'''
for i in ['mingtian','jintian','houtian']:
    print(i)
'''
'''
result = 0
for i in range(1,101,2):
    result +=i
print(result)
'''
'''
string = '天道酬勤'
print(string)
for i in string:
    print(i)

i = 1
while i <=3:
    print('大笑江湖')
    i+=1

i = 1
password = 1
while i < 7:
    num = input('请输入数字密码')
    num = int(num)
    if num == password :
        print('right')
        i = 7
    else:
        print('wrong,error',i,'time')
    i+=1
if i == 7:
    print('error 6 times')
    

none = True
number = 0
while none:
    number +=1
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print('it\'s the number',number)
        break
    else:
        print(number,'is not condition')

total = 99
mod7 = end7 = 0
for number in range(1,100):
    if number % 7 == 0:
        print(number,'mod 7')
        mod7+=1
        continue
    else:
        string = str(number)
        if string.endswith('7'):
            print(number,'end with 7')
            end7 +=1
            continue
    total -=1
print('all time is ', total,'time','mod7 is ',mod7,'end7 is ',end7 )

dictionary = {'qq':'123456','phone':'1309906','name':'mr goood'}
print(dictionary)

dictionary = dict(name='good',sex='male',age='80')
print(dictionary)

name_list = ['dengken','park','jimobili']
dictionary = dict.fromkeys(name_list)
print(dictionary)

name_tuple = ('邓肯','帕克','奥尼尔')
sign = [2.00,1.98,2.16]
dict1 = {name_tuple:sign}
'''
dict1 = {'邓肯':2.16,'帕克':1.98,'奥尼尔':2.10,'robinson':2.22}
'''
print(dict1)
print(dict1['邓肯'])
print('robinson',dict1['robinson'] if 'robinson' in dict1 else 'not exist')
print(dict1.get('robinson'))

for item in dict1.items():
    print(item)

dict1['walaishi'] = 2.18
del dict1['邓肯']
for key,value in dict1.items():
    print(key ,value)
'''
'''
dict2 = dict((('dad',40),('mom',38),('son',20)))
print(dict2)
print(dict2['dad'])
'''
'''
randomdict = {i:random.randint(10,100) for i in range(1,5)}
print(randomdict)

set1 = {1,2,3,4,5,5,1,2,3}
set2 = {'abc','bcd','cdd','abc'}
print(set1)
print(set2)


set1 = set("today is a good day, i will go home")
set2 = set([1,2,3,4,5,3,3,3.14,2,3,1,'today','t','h'])
set3 = set(('life is hard','what do you want','it\'s hard','life is hard'))

print(set1)
print(set2)
print(set3)
set3.add('money')
print(set3)

print(set2)
set2.remove(1)
print(set2)
set2.pop()
print(set2)
set2.pop()
print(set2)
set2.clear()
print(set2)

print(set1)
print(set2)
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
'''



#fun_bmi('jason',1.83,50)
def demo(obj):
    print(obj)
    obj+=obj
mot = 'good day today'

#demo(mot)
#print(mot)
#kat = [1,2,3]
#demo(kat)
#print(kat)
#fun_bmi(height = 2.13,weight=80,person='david')
'''
def demo1(obj=[]):
    print('obj value:',obj)
    obj.append(1)
print(demo1.__defaults__)
demo1()
print(demo1.__defaults__)
demo1()

def demo2(obj=None):
    if obj ==None:
        obj = []
    print('obj value:',obj)
    obj.append(1)
demo2()
demo2()
'''
'''
def printplayname(*name):
    print('my faverate play name:')
    for item in name:
        print(item)
printplayname('baden','max','yao','lin')

def printsign(**sign):
    dage_pos = 'not here'
    print()
    for key,value in sign.items():
        print('key is ',key,'value is ',value)
        if key == 'dage':
            dage_pos = 'dage here'
    return dage_pos

val = printsign(dage='yueyuan',xiaodi='yuanye')
print(val)

message = 'global message'
def f_demo():
    message = 'it\' a message'
    print('local variable',message)

f_demo()
print('outside funtion body',message)

message = 'define global message'
def f_demo():
    global message
    print('local variable', message)
    message = 'it\' a message'
    print('inside funtion body',message)
f_demo()
print('outside funtion body',message)

import math
def circearea(r):
    result = math.pi * r * r
    return result
r = 10
print('r is',r,'area is ',circearea(r))

r = 10
result = lambda r:math.pi * r * r
print('r is ', r,'result is ',result(r))
'''
"""
class Geese:
    #'''geese class'''
    def __init__(self):
        print('I am geese class')
wildgeese = Geese()

class Geese:
    '''geese class'''
    neck = 'long neck'
    wings = 'fast wings'
    def __init__(self,beak, wing, claw):
        self.hand = 'two'
        self.tail = 'one'
        print('I am geese class')
        print(beak)
        print(wing)
        print(claw)
wildgeese = Geese(beak='I have mouth',wing='I have white wing',claw='I have red claw')
print('it\'s instance wildgeese\'s wings',wildgeese.wings)
print('it\'s instance wildgeese\'s neck',wildgeese.neck)
print('it\'s class Geese\'s wings',Geese.wings)
print('it\'s class Gesse\'s wings',Geese.neck)

print('it\'s instance wildgeese\'s member :tail',wildgeese.tail)
print('it\'s instance wildgeese\'s member :hand',wildgeese.hand)
"""
'''
class Swan:
    _neck_swan = 'long neck'
    def __init__(self):
        print('__init__():',Swan._neck_swan)
swan = Swan()
print('dircet access',swan._neck_swan)

class Swan:
    __neck_swan = 'long neck'
    def __init__(self):
        print('__init__():',Swan.__neck_swan)
swan = Swan()
print('dircet access',swan._Swan__neck_swan)
print('dircet access',swan.__neck_swan)

class Rect:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
rect = Rect(100,200)
print('area is :',rect.area)

class Tvshow:
    def __init__(self,show,beati):
        self.__show = show
        self.see = beati
    @property
    def look(self):
        return self.__show
    @property
    def loop(self):
        return self.see
tvshow = Tvshow('wolf','pp')
print('default:',tvshow.look,'see is ',tvshow.see)
tvshow.show = 'kk'
tvshow.see = 'dd'
print('default:',tvshow.look,'see is ',tvshow.see)

class Fruit:
    color = 'green'
    def harvest(self,color):
        print('fruit is ',color,'style')
        print('fruit is harvest')
        print('oh,fruit is ',Fruit.color,'style')
class Orange(Fruit):
    color = 'orange'
    def __init__(self):
        print('I am orange')
    def harvest(self, color):
        print('orange color is ' + color)
        print('orange is harvest')
        print('Fruit orange color is now',Fruit.color)
        print('class orange color is now', orange.color)
apple = Fruit()
print('apple \'s color is',apple.color)
apple.harvest('white')
orange = Orange()
print('orange \'s color is',orange.color)
orange.harvest('blue')

class Fruit:
    def __init__(self, color = 'green'):
        Fruit.color = color
    def harvest(self):
        print('Fruit color is ', Fruit.color)
class Apple(Fruit):
    def __init__(self):
        super().__init__()
        print('I am apple')
apple = Apple()
apple.harvest()

import mypack.bmi as bm
#import mypack.bmi.head
from mypack import bmi
bm.fun_bmi('jack', 1.90,80)
print(bm.head)
print(bm.width)
print(head)
'''
'''
#import mypack.bmi as bm
from mypack import bmi as bm

bm.fun_bmi('jack', 1.90,80)
print(bm.head)
print(bm.width)
#from mypack.bmi import head
#print(head)

from mypack import bmi

bmi.fun_bmi('jack', 1.90,80)
print(bmi.head)
print(bmi.width)

import random
for i in range(1,20,3):
    print(random.randint(0,10)) 

#file = open('pic.png','rb')
#print(file)
file = open('newnote.txt','r',encoding='utf-8')
print(file)
'''
'''
#print('\n','='*10,'python classic applicaiton','='*10)
string1 = 'I will write something in file\n'
string2 = '\n' + '='*10 + 'python classic applicaiton'+ '='*10
string3 = '\n'*3+'write finish'
with open('message.txt','w') as file:
    file.write(string1)
    file.write(string2)
    file.write(string3)
    pass


with open('message.txt','r') as file:
    file.seek(8,0)
    string = file.read(10)
    print(string)
print('with sequence will close file')

print('\n'+'='*20)
with open('message.txt','r') as file:
    number = 0
    while True:
        number +=1
        line = file.readline()
        if line == '':
            break
        print(number,line,end='\n')

print('\n'+'='*20)

print('\n' + '------' * 20)
with open('message.txt','r') as file:
    message = file.readlines()
    print(message)
print('\n' + '------' * 20)

print('\n' + '------' * 20)
with open('message.txt','r') as file:
    messageall = file.readlines()
    for message in messageall:
        print(message)
print('\n' + '------' * 20)
'''
import os
'''
print(os.name)
print(os.linesep)
print(os.sep)
'''
#print(os.getcwd())
'''
with open('mypack/book.txt') as file:
    while True:
        line = file.readline()
        print(line)
        if line == '':
            break

with open(r'mypack\book.txt') as file:
    while True:
        line = file.readline()
        print(line)
        if line == '':
            break

path = os.path.abspath(r'mypack\book.txt')
print('='*40)
print(path)
print('='*40)

path1 = os.path.join('d:\\std-python\\test','mypack\\book.txt')
print(path1)

#result = os.path.exists('d:\\movie')
result = os.path.exists('d:\\std-python')
print(result)

path = 'd:\\newdir'
if not os.path.exists(path):
    print(path,'not exist,creat it')
    os.mkdir(path)
else:
    print(path,'already exist')

path = 'd:\\newdir\\dir1'
if not os.path.exists(path):
    print(path,'not exist,creat it')
    os.makedirs(path)
else:
    print(path,'already exist')
'''
'''
a = 11
path = 'd:\\newdir'
if a == 1:
    if not os.path.exists(path):
        print(path,'not exist,creat it')
        os.mkdir(path)
    else:
        print(path,'already exist')
else:
    if  os.path.exists(path):
        print(path, 'remove')
        os.rmdir(path)
    else:
        print(path, 'not exist,can\'t remove')
'''
import shutil
'''
a = 11
path = 'd:\\newdir'
if a == 1:
    if not os.path.exists(path):
        print(path,'not exist,creat it')
        os.makedirs(path)
    else:
        print(path,'already exist')
else:
    if os.path.exists(path):
        print(path, 'remove')
        shutil.rmtree(path)
    else:
        print(path, 'not exist,can\'t remove')

tuples = os.walk(r'D:\std-python\test\mypack')
for tuple in tuples:
    print(tuple,'\n')
'''
#---------------------------2023-08-30---------------------------------------------------
'''
path = 'message.txt'
if os.path.exists(path):
    os.remove(path)
    print(path + ' delete success')
else:
    print('file not exist')

src = 'D:\\std-python\\test\\newnote.txt'
dst = 'D:\\std-python\\test\\oldnote.txt'
if os.path.exists(src):
    os.rename(src,dst)
    print('rename file success')
else:
    print('can\'t find file')

src = 'tpath'
dst = 'dpath'
if os.path.exists(src):
    os.rename(src,dst)
    print('directory rename ok')
else:
    print('can\'t find dircectory')

path = 'oldnote.txt'
if os.path.exists(path):
    fileinfo = os.stat(path)
    print(os.path.abspath(path))
    print(fileinfo.st_size)
    print(fileinfo.st_mtime)
'''
from multiprocessing import Process
import time
'''
def test(interval):
    print('I am child process')
    
def main():
    print('main process start')
    p = Process(target=test,args=(1,))
    p.start()

if __name__ == '__main__':
    main()
'''
'''
def child_1(interval):
    pid = os.getpid()
    print('child1 process--%s begin execute, father process is %s'%(pid,os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print('child1 process--%s exexcute time "%0.2f" second'%(pid,t_end - t_start))

def child_2(interval):
    pid = os.getpid()
    print('child2 process--%s begin execute, father process is %s' % (pid, os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print('child2 process--%s exexcute time "%0.2f" second' % (pid, t_end - t_start))

if __name__ == '__main__':
    fpid = os.getpid()
    print('-----father process begin------')
    print('father pid %s' % fpid)
    p1 = Process(target=child_1, args=(1,))
    p2 = Process(target=child_2, name='mrsoft',args=(2,))
    p1.start()
    p2.start()
    print('p1.is_alive=%s' % p1.is_alive())
    print('p2.is_alive=%s' % p2.is_alive())
    print('p1.name=%s' % p1.name)
    print('p1.pid=%s' % p1.pid)
    print('p2.name=%s' % p2.name)
    print('p2.pid=%s' % p2.pid)
    print('-------wait child process end-------')
    p1.join()
    p2.join()
    print('-------father process end-------')
'''

from multiprocessing import Pool
from multiprocessing import Queue
'''
def task(name):
    print('child process %s execute task %s ...' % (os.getpid(),name))
    time.sleep(1)

if __name__ == '__main__':
    print('father process %s' % (os.getpid()))
    p = Pool(3)
    for i in range(10):
        p.apply_async(task,args=(i,))
    print('wait all child process finish')
    p.close()
    p.join()
    print('all child process finish')
'''
'''
#----------------------------------------------------
def plus():
    print('='*15 +'child process 1 start'+'='*16)
    global g_num
    g_num += 50
    print('g_num is %d' % (g_num))
    print('='*15 +'child process 1 finish'+'='*15)
#-----------------------------------------------------
#-----------------------------------------------------
def minus():
    print('='*15 +'child process 2 start'+'='*16)
    global g_num
    g_num -= 50
    print('g_num is %d' % (g_num))
    print('='*15 +'child process 2 finish'+'='*15)
#-----------------------------------------------------
g_num = 100
if __name__ == '__main__':
    print('-------main process start---------')
    p1 = Process(target=plus)
    p2 = Process(target=minus)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('-------main process finish---------')


if __name__ == '__main__':
    q = Queue(3)
    q.put('message 1')
    q.put('message 2')
    print(q.full())
    q.put('message 3')
    print(q.full())
    try:
        q.put('message', True ,2)
    except:
        print('queue is full,now message number is %s' % q.qsize())
    try:
        q.put_nowait('message 4')
    except:
        print('queue is full,now message number is %s' % q.qsize())
    if not q.empty():
        print('-'*10 + 'get message from queue' + '-'*10)
        for i in range(q.qsize()):
            print(q.qsize())
            print(q.get_nowait())
        print('='*30)
        if not q.full():
            q.put_nowait('message 4')
            print(q.qsize())
            print(q.get_nowait())
    print(q.qsize())
'''
#=================================   2023-08-31   =======================================
'''
def write_task(q):
    if not q.full():
        for i in range(5):
            message = 'message' + str(i)
            #time.sleep(1)
            q.put(message)
            print('write %s\n' % message)
def read_task(q):
    time.sleep(1)
    while not q.empty():
        print('read %s\n' % q.get(True, 2))

if __name__ == '__main__':
    print('father process start')
    q= Queue(3)
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('father process end')
'''
import threading
'''
def process():
    for i in range(3):
        time.sleep(1)
        print('thread name is %s\n' % threading.current_thread().name)

if __name__ == '__main__':
    print('main thread start')
    threads = [threading.Thread(target=process) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('main thread end')
'''
'''
class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = 'child thread' + self.name + 'execute i =' + str(i)
            print(msg+'\n')

if __name__ == '__main__':
    print('-'*15 + 'main thread begin' + '-'*15)
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main thread end')
'''
from threading import Thread
'''
def plus():
    print('-'*15+'child1 thread start'+ '1'*15)
    global g_num
    g_num +=50
    print('g_num is %d' % g_num)
    print('-' * 15 + 'child1 thread end' + '-' * 15)

def minus():
    print('-' * 15 + 'child1 thread start' + '-' * 15)
    global g_num
    g_num -= 50
    print('g_num is %d' % g_num)
    print('-' * 15 + 'child1 thread end' + '-' * 15)

g_num = 100
if __name__ == '__main__':
    print('main thread start')
    print('g_num is %d' % g_num)
    t1 = Thread(target=plus)
    t2 = Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('now g_num is %d' % g_num)
    print('main thread end')
'''
from threading import Lock
'''
n = 100
def task():
    global n
    #mutex.acquire()
    temp = n
    time.sleep(0.1)
    n = temp -1
    print('buy success rest ticket %d' % n)
   # mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    t_l= []
    for i in range(10):
        t = Thread(target=task)
        t_l.append(t)
        t.start()
        for t in t_l:
            t.join()
'''

from queue import Queue
'''
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue
    def run(self):
        for i in range(5):
            print('producer %s add product %d into queue' % (self.getName(),i))
            self.data.put(i)
            time.sleep(random.random())
        print('producer %s' % self.getName())

'''
'''
class Producer(threading.Thread):
    def __init__(self, name,queue):
        threading.Thread.__init__(self, name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            print("生成者%s将产品%d加入队列!" % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.random())
        print("生成者%s完成!" % self.getName())
'''
'''
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue
    def run(self):
        for i in range(5):
            val = self.data.get()
            print('consumer %s get %d from queue' % (self.getName() , val))
        print('consumer %s' % self.getName())
if __name__ == '__main__':
    print('-'*15 + 'main thread begin' + '-'*15)
    queue = Queue()
    producer = Producer('produce',queue)
    consumer = Consumer('consumer',queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('-' * 15 + 'main thread end' + '-' * 15)
'''

from queue import Queue
import random,threading,time

'''
# 生产者类
class Producer(threading.Thread):
    def __init__(self, name,queue):
        threading.Thread.__init__(self, name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            print("生成者%s将产品%d加入队列!" % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.random())
        print("生成者%s完成!" % self.getName())

# 消费者类
class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            val = self.data.get()
            print("消费者%s将产品%d从队列中取出!" % (self.getName(),val))
            time.sleep(random.random())
        print("消费者%s完成!" % self.getName())

if __name__ == '__main__':
    print('-----主线程开始-----')
    queue = Queue()        # 实例化队列
    producer = Producer('Producer',queue)   # 实例化线程Producer，并传入队列作为参数
    consumer = Consumer('Consumer',queue)   # 实例化线程Consumer，并传入队列作为参数
    producer.start()    # 启动线程Producer
    consumer.start()    # 启动线程Consumer
    producer.join()     # 等待线程Producer结束
    consumer.join()     # 等待线程Consumer结束
    print('-----主线程结束-----')
'''
'''
def division():
    num1 = int(input('enter dividend '))
    num2 = int(input('enter divisor '))
    result = num1/num2
    print(result)

if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print('input error divisor can\'t be 0')

def division():
    num1 = int(input('enter dividend '))
    num2 = int(input('enter divisor '))
    result = num1/num2
    print(result)

if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print('input error divisor can\'t be 0')
    except ValueError as e:
        print('input error')
        print('='*10,e,'='*10)
    else:
        print('execute finish')
'''
'''
def division():
    num1 = int(input('enter dividend '))
    num2 = int(input('enter divisor '))
    result = num1/num2
    print(result)

if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print('input error divisor can\'t be 0')
    except ValueError as e:
        print('input error')
        print('='*10,e,'='*10)
    else:
        print('execute finish')
    finally:
        print('always run this code')
'''
