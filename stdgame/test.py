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

        pass
    else:
        pass
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_code('1')


