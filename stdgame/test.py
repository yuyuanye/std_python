# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test_code(chapter):
    if chapter == '1':
        '''
        print_hi('PyCharm')
        x = input('please input')
        print(type(x))

        for i in range(10):
            print(i,)

        for i in range(10,20):
            print(i,end=' ')
        '''
        #print(123, 'abc', 45, 'book', sep='#')
        #print('price');print(100)
        #print('price',end='=');print(100)
        '''
        x = 'longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglong1223\
            6666longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglong'
        print(x)
        y = ('longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglong1223'
             '6666longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglong')
        print(y)
        '''
        '''
        width = 0;height = 0; color = 'black';emphasis = 'small'
        if (width == 0 and height ==0 and
            color == 'red' and emphasis == 'strong'):
            y = 'right'
        else:
            y = 'wrong'
        print(y)
        '''
        WHITE = 0xFFFF
        THIS_IS_A_CONSTANT = 1
        #print(not True)
        #print(not False)
        #a = 'python'
        #print(a and True)
        #b = ''
        #print(b or False)
        list1 = ['中国','美国',1997,2000]
        list2 = [1,2,3,4,5,6,7]
        list3 = ["a","b","c","d"]
        #print('list1[0]=',list1[0])
        #print('list2[1:5]=',list2[1:5])
        '''
        list1[2] = 8888
        print(list1)
        del list1[2]
        print(list1)
        list1.remove(2000)
        print(list1)
        
        list1.pop(2)
        print(list1)
        
        list1.pop()
        print(list1)
        '''
        #list1.append(3000)
        #print(list1)
        '''
        rows = 3
        cols = 6
        matrix = [[0 for col in range(cols)] for row in range(rows)]
        print(matrix)
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = i*3 +j
                print(matrix[i][j],end=',')
            print('\n')
        '''
        tup1 = ('中国', '美国', 1997, 2000)
        tup2 = (1, 2, 3, 4, 5, 6, 7)
        '''
        print('tup1[0]=', tup1[0])
        print('tup2[1:5]=',tup2[1:5])
        print(tup2[2:])
        print(tup2*2)
        '''
        '''
        tup3 = tup1 + tup2
        #print(tup3)
        #del tup3
        #print(tup3)
        listt3 = list(tup3)
        #print(tup3)
        dic1 = {'xiaoming':40,'xiaohong':50,'xiaoliu':60}
        #print(dic)
        dic2 ={33:44,'hello':50,88:'good'}
        print(dic2)
        '''
        #ditc = {'name':'xmj','age':17,'name':'manni'}
        ditc = {'name': 'xmj', 'age': 17, 'name': ['manni','haha'],'age':'what do'}
        #print("dict['name']",ditc['name'])
        ditc['age']=18
        #print(ditc)
        ditc['school']='pku'
        #print(ditc)
        #del ditc['age']
        '''
        ditc.clear()
        print(ditc)
        del ditc
        print(ditc)
        '''
        #print('age' in ditc)
        #print(ditc.values())
        '''
        for key,value in ditc.items():
            print(key,value)
        d = {'name':'wanghai','age':1}
        print('age is %s' % d.get('age'))
        print('sex is %s' % d.get('sex','man'))
        print('sex is %s' % d.get('sex'))
        '''
        '''
        student={'tom','jim','mary','tom','jack'}
        print(student)
        if 'rose' in student:
            print('rose in')
        else:
            print('rose out')
        '''
        '''
        a = set('abcd')
        b = set('cdef')
        print(a)
        print('a-b',a-b)
        print('a|b',a | b)
        print('a&b',a & b)
        '''
        '''
        year = int(input('输入年份：'))
        if year % 4 == 0 and year % 100 !=0 or year %400 ==0:
            print(year,'是闰年')
        else:
            print(year, '不是闰年')
        '''
        '''
        year = int(input('输入年：'))
        month = int(input('输入月：'))
        day = int(input('输入日：'))
        months = (0,31,59,90,120,151,181,212,243,273,304,334)
        if 0 <= month <=12:
            sum = months[month-1]
        else:
            print('月份输入错误')
        sum+=day
        leap = 0
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            leap = 1
        if (leap == 1) and (month > 2):
            sum +=1
        print('这一天是这一年的第%d天' % sum)
        '''
        '''
        fruits = ['banana','apple','mango']
        for fruit in fruits:
            print('元素：',fruit)
        print('finish')
        sum = 0
        for x in range(1,10):
            sum = sum + x
        print(sum)
        '''
        #print(list(range(5)))
        '''
        sum = 0
        for x in range(1,101):
            sum = sum +x
        print(sum)
        '''
        '''
        i = 1
        while i<10:
            i+=1
            if i %2 > 0:
                continue
            print(i)
        print('='*10)
        i=1
        while 1:
            print(i)
            i+=1
            if i>10:
                break
        '''
        '''
        color = ['♦','♣','♠','♥']
        num_poker = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        sum_poker = [i+j for i in num_poker for j in color]
        print(sum_poker)
        '''
        '''
        def sum(a ,n):
            result,t = 0,0
            for i in range(n):
                t = t*10+a
                result +=t
            return result
        a = int(input('enter a:'))
        n = int(input('enter n:'))
        print(sum(a,n))
        '''
        '''
        def func_lib():
            def add(x,y):
                return x+y
            return add
        fadd = func_lib()
        print(fadd(1,2))
        '''
        '''
        def f(x):
            if x == 1:
                return 1
            else:
                return(f(x-1)+x*x)
        print(f(5))
        '''
        import fibo
        fibo.fib(1000)
        print(fibo.fib2(100))
        print(fibo.add(2,3))
        pass
    else:
        pass
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_code('1')


