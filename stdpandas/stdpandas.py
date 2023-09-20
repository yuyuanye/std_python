# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas
import pandas as pd
import numpy as np
import glob

#testcode = '4_19'

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
def test(testcode):
    if testcode == '01':
        pd.set_option('display.unicode.east_asian_width', True)
        #pd.set_option('display.max_rows',10)
        #pd.set_option('display.max_columns', 10)
        df = pd.read_excel(r'.\resource\data.xlsx')
        print(df.head())
        #print(df)
    elif testcode == '02':
        subtest = 1
        if subtest == 1:
            s1 = pd.Series([88,60,75])
            print(s1)
        else:
            pass
    elif testcode == '03':
        s1 = pd.Series([88, 60, 75], index=[1, 2, 3])
        s2 = pd.Series([88, 60, 75], index=['明日同学', '高同学', '七月流火'])
        print(s1)
        print(s2)
    elif testcode == '04':
        s1 = pd.Series([88, 60, 75])
        print(s1[0])
        s2 = pd.Series([88, 60, 75], index=[1, 2, 3])
        print(s2[1])
    elif testcode == '05':
        s1 = pd.Series([88, 60, 75], index=['明日同学', '高同学', '七月流火'])
        print(s1['明日同学'])
        print('='*20)
        print(s1[['明日同学','七月流火']])
    elif testcode == '06':
        s1 = pd.Series([88, 60, 75], index=['明日同学', '高同学', '七月流火'])
        print(s1['明日同学':'七月流火'])
    elif testcode == '07':
        s2 = pd.Series([88, 60, 75, 44, 67, 36])
        print(s2[1:4])
    elif testcode == '08':
        s2 = pd.Series([88, 60, 75, 44, 67, 36])
        print(s2. index)
        print('=' * 20)
        print(s2.values)
    elif testcode == '09':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110,105,99],[105,88,115],[109,120,130]]
        index = [2,3,4]
        columns =['语文','数学','英语']
        df = pd.DataFrame(data=data, index=index, columns=columns)
        print(df)
        print('=' * 20)
        for col in df.columns:
            series = df[col]
            print(series)
            print('=' * 20)
    elif testcode == '10':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130]]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data, columns=columns)
        print(df)
    elif testcode == '11':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.DataFrame({
        '语文':[110,105,99],
        '数学': [105, 88, 115],
        '英语': [109, 120, 130],
        '班级':'高一7班'
        },index=[0,1,2])
        print(df)
    elif testcode == '12':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\1月.xlsx')
        print(df.head())
    elif testcode == '13':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\1月.xlsx',sheet_name='莫寒')
        print(df.head())
    elif testcode == '14':
        pd.set_option('display.unicode.east_asian_width', True)
        #df = pd.read_excel(r'.\resource\1月.xlsx',index_col=0)
        #df = pd.read_excel(r'.\resource\1月.xlsx', header=1)
        df = pd.read_excel(r'.\resource\1月.xlsx', header=None)
        print(df.head())
    elif testcode == '15':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\1月.xlsx',usecols=[0])
        print(df.head())
    elif testcode == '16':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_csv(r'.\resource\1月.csv', encoding='gbk')
        print(df.head())
    elif testcode == '17':
        df = pd.read_csv(r'.\resource\1月.txt', encoding='gbk')
        print(df.head())
    elif testcode == '18':
        df = pandas.DataFrame()
        url_list = ['https://www.espn.com/nba/salaries/_/year/2024/seasontype/4']
        #url_list = ['http://www.espn.com/nba/salaries/_/seasontype/4']
        '''
        for i in range(2020,2023):
            url = 'https://www.espn.com/nba/salaries/_/year/%s/seasontype/4' % i
            url_list.append(url)
        '''
        #print(url_list)
        for url in url_list:
            df = df._append(pd.read_html(url), ignore_index=True)
        #print(df[3])
        a = df[[x.startswith('$') for x in df[3]]]
        print(df[3])
        #print(a)
        df = df[[x.startswith('$') for x in df[3]]]
        #print(df)
        df.to_csv(r'.\resource\nba.csv', header=['RK','NAME','TEAM','SALARY'],index=False)
    elif testcode == '19':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130],[112,115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火','二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        print('='*30)
        print(df.loc['明日'])
    elif testcode == '20':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df.loc[['明日','高同学']])
        print('=' * 30)
        print(df.iloc[[0,1]])
    elif testcode == '21':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df.loc['明日':'二月二'])
        print('=' * 30)
        print(df.loc[:'七月流火':])
        print('=' * 30)
        print(df.iloc[0:4])
        print('=' * 30)
        print(df.iloc[1::])
    elif testcode == '22':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df[['语文', '数学']])
    elif testcode == '23':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df.loc[:,['语文', '数学']])
        print('=' * 30)
        print(df.iloc[:,[0,1]])
        print('=' * 30)
        print(df.loc[:, '语文':])
        print('=' * 30)
        print(df.iloc[:,:2])
    elif testcode == '24':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        '''
        print(df.loc['七月流火','英语'])
        print('=' * 30)
        print(df.loc[['七月流火'], ['英语']])
        print('=' * 30)
        print(df.loc[['七月流火'], ['英语','数学']])
        print('=' * 30)
        '''
        print(df.iloc[[1],[2]])
        print('=' * 30)
        print(df.iloc[1:, [2]])
        print('=' * 30)
        print(df.iloc[1:, [0,2]])
        print('=' * 30)
        print(df.iloc[:, 2])
        print('=' * 30)
    elif testcode == '25':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        print(df.loc[(df['语文'] > 105) & (df['数学'] > 88)])
    elif testcode == '26':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        df['物理'] = [88,99,79,60]
        print(df)
    elif testcode == '27':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        df.loc[:,'物理'] = [88,99,79,60]
        print(df)
    elif testcode == '28':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        wl = [88, 99, 79, 60]
        df.insert(1,'物理',wl)
        print(df)
    elif testcode == '29':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        df.loc['钱多多'] = [110,98,79]
        print(df)
    elif testcode == '30':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        df_insert = pd.DataFrame({'语文':[100,123,138],'数学':[99,142,60],'英语':[98,139,99]},index=['钱多多','童年','无名'])
        print(df_insert)
        df1 = df._append(df_insert)
        print(df1)
    elif testcode == '31':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        print('='*30)
        df.columns = ['语文', '数学（上）', '英语']
        print(df)
    elif testcode == '32':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        print('='*30)
        #df.columns = ['语文(上)', '数学（上）', '英语（上）']
        df.rename(columns = {'语文':'语文(上)', '数学':'数学（上）', '英语':'英语（上）'},inplace=True)
        print(df)
    elif testcode == '33':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        #print(list('1234'))
        print('='*30)
        #df.index = list('1234')
        df.rename({'明日':2, '高同学':2, '七月流火':3, '二月二':4}, inplace=True)
        print(df)
    elif testcode == '34':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        print('='*30)
        #df.loc['明日'] =[120,115,109]
        #df.loc['明日'] = df.loc['明日'] + 20
        #df.loc[:,'语文'] = [120, 115, 109,89]
        #df.loc['明日', '语文'] = 127
        #df.iloc[0, 0] = 124
        #df.iloc[:, 0] = [120, 115, 109, 89]
        df.iloc[0,:] = [120, 115, 109]
        print(df)
    elif testcode == '35':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        print('='*30)
        #df.drop(['数学'],axis=1,inplace=True)
        #df.drop(columns='数学', inplace=True)
        #df.drop(labels='数学', axis=1, inplace=True)
        #df.drop(['明日','二月二'], inplace=True)
        #df.drop(index='明日', inplace=True)
        df.drop(labels='明日',axis=0, inplace=True)
        #msg = help(DataFrame.drop)
        #print(msg)
        print(df)
    elif testcode == '36':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115]]
        columns = ['语文', '数学', '英语']
        name = ['明日', '高同学', '七月流火', '二月二']
        df = pd.DataFrame(data=data, index=name, columns=columns)
        print(df)
        print('='*30)
        #df.drop(df[df['数学'].isin([88])].index, inplace=True)
        df.drop(df[df['语文']<110].index, inplace=True)
        print(df)
    elif testcode == '37':
        df = pd.read_excel(r'.\resource\TB2018.xls')
        print(df)
        print(df.info())
    elif testcode == '38':
        df = pd.read_excel(r'.\resource\TB2018.xls')
        #print(df)
        #print(df.isnull())
        #print(df.notnull())
        #df.dropna(inplace=True)
        df1 = df[df['宝贝总数量'].notnull()]
        print(df1)
    elif testcode == '39':
        df = pd.read_excel(r'.\resource\TB2018.xls')
        df['宝贝总数量'] = df['宝贝总数量'].fillna(0)
        print(df)
    elif testcode == '40':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\1月.xlsx')
        #print(df.duplicated(['收货人姓名']))
        #df1 = df.drop_duplicates(['收货人姓名'])
        df1 = df.drop_duplicates(['收货人姓名'],keep='last')
        print(df1)
    elif testcode == '41':
        subtest = 2
        if subtest == 1:
            s1 = pd.Series([10,20,30],index=list('abc'))
            s2 = pd.Series([2, 3, 4], index=list('bcd'))
            print(s1)
            print('='*30)
            print(s2)
            print('=' * 30)
            print(s1+s2)
        elif subtest == 2:
            s1 = pd.Series([88,60,75], index=[1,2,3])
            print(s1)
            print('=' * 30)
            #print(s1.reindex([1,2,3,4,5]))
            print(s1.reindex([1, 2, 3, 4, 5], fill_value=0))
        else:
            pass
    elif testcode == '3_42':
        '''
        s1 = pd.Series([88,60,75], index=[1,2,3])
        print(s1)
        print('=' * 30)
        print(s1.reindex([1,2,3,4,5],method='ffill'))
        '''
        s1 = pd.Series([88, 60, 75], index=[3, 4, 5])
        print(s1)
        print('=' * 30)
        print(s1.reindex([1, 2, 3, 4, 5], method='bfill'))
    elif testcode == '3_43':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [[110,105,99],[105,88,115],[109,120,130]]
        index = ['mr001','mr003','mr005']
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data, index=index,columns=columns)
        print(df)
        print('='*30)
        #print(df.reindex(['mr001','mr002','mr003','mr004','mr005']))
        #print(df.reindex(columns=['语文', '数学', '英语','物理']))
        print(df.reindex(index=['mr001', 'mr002', 'mr003', 'mr004', 'mr005'],columns=['语文', '数学', '英语','物理']))
        #print(df)
    elif testcode == '3_44':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\1月.xlsx')
        print(df.head())
        print('=' * 30)
        df = df.set_index(['买家会员名'])
        print(df)
    elif testcode == '3_45':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\TB2018.xls')
        print(df.dropna())
        print('=' * 30)
        print(df.dropna().reset_index(drop=True))
    elif testcode == '46':
        excelfile = 'mrbook.xlsx'
        df = pd.DataFrame(pd.read_excel(r'.\resource\mrbook.xlsx'))
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.ambiguous_as_wide',True)
        pd.set_option('display.unicode.east_asian_width', True)
        df = df.sort_values(by='销量',ascending=False)
        print(df)
    elif testcode == '3_47':
        df = pd.DataFrame(pd.read_excel(r'.\resource\mrbook.xlsx'))
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.ambiguous_as_wide',True)
        pd.set_option('display.unicode.east_asian_width', True)
        df = df.sort_values(by=['图书名称','销量'],ascending=False)
        print(df)
    elif testcode == '3_48':
        df = pd.DataFrame(pd.read_excel(r'.\resource\mrbook.xlsx'))
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.ambiguous_as_wide',True)
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = df.groupby(['类别'])
        df2 = df1['销量'].sum().reset_index()
        print(df1)
        print(df2)
    elif testcode == '3_49':
        dfrow = pd.DataFrame(pd.read_excel(r'.\resource\books.xls'))
        # 设置数据显示的列数和宽度
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        # 解决数据输出时列名不对齐的问题
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)

        print('-------------------------按行数据排序-------------------------')
        # 按照索引值为0的行，即第一行的值升序排序
        dfrow.sort_values(by=0, ascending=True, axis=1)
        print(dfrow.sort_values(by=0, ascending=True, axis=1))
    elif testcode == '3_50':
        df = pd.DataFrame(pd.read_excel(r'.\resource\mrbook.xlsx'))
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        df = df.sort_values(by='销量',ascending=False)
        df['顺序排名'] = df['销量'].rank(method='first', ascending=False)
        print(df[['图书名称','销量','顺序排名']])
    elif testcode == '3_51':
        df = pd.DataFrame(pd.read_excel(r'.\resource\mrbook.xlsx'))
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        df = df.sort_values(by='销量',ascending=False)
        #df['平均排名'] = df['销量'].rank(ascending=False)
        #df['最小排名'] = df['销量'].rank(method='min', ascending=False)
        df['最大排名'] = df['销量'].rank(method='max', ascending=False)
        print(df)
    elif testcode == '4_01':
        data  = [[110,105,99], [105,88,115],[109,120,130]]
        index = [1,2,3]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data, index=index, columns=columns)
        df['总成绩'] = df.sum(axis=1)
        print(df)
        print(df.sum(axis=0))
        print(df.sum(axis=1))
    elif testcode == '4_02':
        data  = [[110,105,99], [105,88,115],[109,120,130]]
        index = [1,2,3]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data, index=index, columns=columns)
        new = df.mean()
        df = df._append(new ,ignore_index=True)
        print(df)
    elif testcode == '4_03':
        data  = [[110,105,99], [105,88,115],[109,120,130],[112,115]]
        index = [1,2,3,4]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data, index=index, columns=columns)
        new = df.max()
        df = df._append(new ,ignore_index=True)
        print(df)
    elif testcode == '4_04':
        data  = [[110,105,99], [105,88,115],[109,120,130],[112,115]]
        index = [1,2,3,4]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data, index=index, columns=columns)
        new = df.min()
        df = df._append(new ,ignore_index=True)
        print(df)
    elif testcode == '4_05':
        data  = [[110,105,99], [105,88,115],[109,120,130]]
        index = [1,2,3]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data, index=index, columns=columns)
        new = df.median()
        df = df._append(new ,ignore_index=True)
        print(df)
    elif testcode == '4_06':
        data  = [[110,105,99], [105,88,115],[109,120,130],[112,115]]
        index = [1,2,3,4]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data, index=index, columns=columns)
        new = df.median()
        df = df._append(new ,ignore_index=True)
        print(df)
    elif testcode == '4_07':
        pd.set_option('display.unicode.east_asian_width', True)
        data  = [[110,88,99], [110,88,115],[109,120,130]]
        #data = [[111, 120, 110], [131, 130, 130], [130, 120, 130]]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data,  columns=columns)
        print(df.mode())
        print(df.mode(axis=1))
        print(df['数学'].mode())
    elif testcode == '4_08':
        pd.set_option('display.unicode.east_asian_width', True)
        data  = [[110,88,99,110],[88,109,120,130]]
        columns = ['物理1', '物理2', '物理3', '物理4']
        index = ['小黑','小白']
        df = pd.DataFrame(data=data,  columns=columns,index=index)
        print(df)
        print(df.var(axis=1))
    elif testcode == '4_09':
        pd.set_option('display.unicode.east_asian_width', True)
        data  = [[110,88,99], [110,88,115],[109,120,130]]
        columns = ['语文', '数学', '英语']
        df = pd.DataFrame(data=data,  columns=columns)
        print(df)
        print(df.std())
    elif testcode == '4_10':
        pd.set_option('display.unicode.east_asian_width', True)
        data  = [70,88,99, 100,88,115,109,120,130]
        columns = ['数学']
        df = pd.DataFrame(data=data,  columns=columns)
        print(df)
        x = df['数学'].quantile(0.35)
        print(x)
        print(df[df['数学']<=x])
    elif testcode == '4_11':
        df = pd.DataFrame({'A':[1,2],
             'B':[pd.Timestamp('2019'),pd.Timestamp('2020')],
             'C':[pd.Timedelta('1 days'), pd.Timedelta('2 days')]})
        print(df)
        print(df.quantile(0.5, numeric_only=False))
    elif testcode == '4_12':
        df = pd.DataFrame(np.random.random([5,5]),columns=['A1','A2','A3','A4','A5'])
        print(df)
        #print(df.round(2))
        print(df.round({'A1':1, 'A2':2}))
        s1 = pd.Series([1,0,2],index=['A1','A2','A3'])
        print(s1)
        print(df.round(s1))
    elif testcode == '4_13':
        df = pd.DataFrame(np.random.random([5, 5]), columns=['A1', 'A2', 'A3', 'A4', 'A5'])
        print(df)
        df['A1百分比']=df['A1'].apply(lambda x: format(x,'.0%'))
        #print(df)
        df['A1百分比'] = df['A1'].apply(lambda x: format(x, '.2%'))
        #print(df)
        df['A1百分比'] = df['A1'].apply(lambda x:'{:.0%}'.format(x))
        print(df)
    elif testcode == '4_14':
        pd.set_option('display.unicode.east_asian_width', True)
        data = [['零基础学python','1月',49768889],['零基础学python','2月',11777775],['零基础学python','3月',127737455]]
        columns = ['图书','月份','码洋']
        df = pd.DataFrame(data=data, columns=columns)
        df['码洋'] = df['码洋'].apply(lambda  x :format(int(x),','))
        print(df)
    elif testcode == '4_15':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_csv(r'.\resource\JD.csv', encoding='gbk')
        df1 = df[['一级分类','7天点击量','订单预定']]
        print(df1.groupby('一级分类').sum())
    elif testcode == '4_16':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_csv(r'.\resource\JD.csv', encoding='gbk')
        df1 = df[['一级分类','二级分类','7天点击量','订单预定']]
        print(df1.groupby(['一级分类','二级分类']).sum())
    elif testcode == '4_17':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_csv(r'.\resource\JD.csv', encoding='gbk')
        df1 = df[['一级分类','二级分类','7天点击量','订单预定']]
        print(df1.groupby(['二级分类'])['7天点击量'].sum())
    elif testcode == '4_18':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_csv(r'.\resource\JD.csv', encoding='gbk')
        df1 = df[['一级分类','7天点击量','订单预定']]
        for name,group in df1.groupby('一级分类'):
            print(name)
            print(group)
    elif testcode == '4_19':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_csv(r'.\resource\JD.csv', encoding='gbk')
        df1 = df[['一级分类','二级分类','7天点击量','订单预定']]
        for (key1,key2),group in df1.groupby(['一级分类','二级分类']):
            print(key1,key2)
            print(group)
    elif testcode == '4_20':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_csv(r'.\resource\JD.csv', encoding='gbk')
        df1 = df[['一级分类','7天点击量','订单预定']]
        print(df1.groupby('一级分类').agg(['mean','sum']))
    elif testcode == '4_21':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_csv(r'.\resource\JD.csv', encoding='gbk')
        df1 = df[['一级分类','7天点击量','订单预定']]
        print(df1.groupby('一级分类').agg({'7天点击量':['mean', 'sum'],'订单预定':['sum']}))
    elif testcode == '4_22':
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\1月_4-22.xlsx')
        max1 = lambda x :x.value_counts(dropna=False).index[0]
        print(max1)
        df1=df.agg({'宝贝标题':[max1],'数量':['sum','mean'],'买家实际支付金额':['sum','mean']})
        print(df1)
    elif testcode == '4_23':
        df = pd.read_csv(r'.\resource\JD_4-23.csv', encoding='gbk')
        df = df.set_index(['商品名称'])
        dict1 = {'北京出库销量':'北上广','上海出库销量':'北上广','广州出库销量':'北上广',
                 '成都出库销量':'成都','武汉出库销量':'武汉','西安出库销量':'西安'}
        df1 = df.groupby(dict1, axis=1).sum()
        print(df1)
    elif testcode == '4_24':
        df = pd.read_csv(r'.\resource\JD_4-23.csv', encoding='gbk')
        df = df.set_index(['商品名称'])
        data = {'北京出库销量': '北上广', '上海出库销量': '北上广', '广州出库销量': '北上广',
                 '成都出库销量': '成都', '武汉出库销量': '武汉', '西安出库销量': '西安'}
        s1 = pd.Series(data)
        #print(s1)
        df1 = df.groupby(s1, axis=1).sum()
        print(df1)
    elif testcode == '4_25':
        data = [110, 105,99,120,115]
        index = [1,2,3,4,5]
        df = pd.DataFrame(data=data, index=index, columns=['英语'])
        df['升降'] = df['英语']-df['英语'].shift()
        print(df['英语'].shift())
        print(df)
    elif testcode == '4_26':
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\mrbooks_4-26.xls', usecols=['买家会员名','收货地址'])
        series=df['收货地址'].str.split(' ',expand=True)
        #print(series)
        df['省'] = series[0]
        df['市'] = series[1]
        df['区'] = series[2]
        disp = ['省','市','区']
        print(df[disp].head())
    elif testcode == '4_27':
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\mrbooks_4-26.xls',usecols=['宝贝标题'])
        df = df.join(df['宝贝标题'].str.split(',',expand=True))
        print(df.head())
    elif testcode == '4_28':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.DataFrame({'a':[1,2,3,4,5],'b':[(1,2),(3,4),(5,6),(7,8),(9,10)]})
        print(df)
        #df[['b1','b2']] = df['b'].apply(pd.Series)
        #print(df)
        df = df.join(df['b'].apply(pd.Series))
        print(df)
    elif testcode == '4_29':
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\grade.xls')
        df = df.set_index(['班级','序号'])
        df = df.stack()
        print(df)
    elif testcode == '4_30':
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\grade.xls', sheet_name='英语2')
        df = df.set_index(['班级','序号','Unnamed: 2'])
        df = df.unstack()
        print(df)
    elif testcode == '4_31':
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\grade.xls', sheet_name='英语3')
        print(df.pivot(index='序号',columns='班级',values='得分'))
    elif testcode == '4_32':
        df = pd.read_excel(r'.\resource\mrbooks_4-32.xls')
        df1 = df.groupby(['宝贝标题'])['宝贝总数量'].sum()
        mydict = df1.to_dict()
        for i,j in mydict.items():
            print(i,':\t',j)
    elif testcode == '4_33':
        df = pd.read_excel(r'.\resource\mrbooks_4-32.xls')
        df1=df[['买家会员名']].head()
        list1 = df1['买家会员名'].values.tolist()
        for s in list1:
            print(s)
    elif testcode == '4_34':
        df = pd.read_excel(r'.\resource\fl4.xls')
        df1 = df[['label1', 'label2']].head()
        tuples = [tuple(x) for x in df1.values]
        for t in tuples:
            print(t)
    elif testcode == '4_35':
        df = pd.read_excel(r'.\resource\mrbooks_4-35.xls')
        df.to_html(r'.\resource\mrbook.html',header= True, index=False)
    elif testcode == '4_36':
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                            '语文':[110,105,109],
                            '数学':[105,88,120],
                            '英语':[99,115,130]})
        df2 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                            '体育':[34.5,39.7,38]})
        df_merge = pd.merge(df1,df2,on='编号')
        print(df_merge)
    elif testcode == '4_37':
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                            '语文':[110,105,109],
                            '数学':[105,88,120],
                            '英语':[99,115,130]})
        df2 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                            '体育':[34.5,39.7,38]})
        df_merge = pd.merge(df1,df2,right_index=True, left_index=True)
        print(df_merge)
    elif testcode == '4_38':
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003'],
                            '语文': [110, 105, 109],
                            '数学': [105, 88, 120],
                            '英语': [99, 115, 130]})
        df2 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003'],
                            '体育': [34.5, 39.7, 38]})
        df_merge = pd.merge(df1, df2, on='编号',how='left')
        print(df_merge)
    elif testcode == '4_39':
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                            '学生姓名':['明日同学','高圆圆','钱多多']})
        df2 = pd.DataFrame({'编号': ['mr001', 'mr001', 'mr003'],
                            '语文': [110, 105, 109],
                            '数学': [105, 88, 120],
                            '英语': [99, 115, 130],
                            '时间':['1月','2月','3月']})
        df_merge1 = pd.merge(df1, df2, on='编号')
        print(df_merge1)
        df_merge2 = pd.merge(df2, df1, on='编号')
        print(df_merge2)
    elif testcode == '4_40':
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003','mr001','mr001'],
                            '体育': [34.5, 39.7, 38,33,35]})
        df2 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003', 'mr003', 'mr003'],
                            '语文': [110, 105, 109,110,108],
                            '数学': [105, 88, 120,123,119],
                            '英语': [99, 115, 130,109,128]})
        df_merge=pd.merge(df1,df2)
        print(df_merge)
    elif testcode == '4_41':
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003', 'mr001', 'mr001'],
                            '体育': [34.5, 39.7, 38, 33, 35]})
        df2 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003', 'mr003', 'mr003'],
                            '语文': [110, 105, 109, 110, 108],
                            '数学': [105, 88, 120, 123, 119],
                            '英语': [99, 115, 130, 109, 128]})
        df_merge = pd.merge(df1, df2)
        #df_merge = df_merge.set_index('编号')
        print(df_merge)
        df_merge.to_excel(r'.\resource\merge_4_41.xlsx')
    elif testcode == '4_42':
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003', 'mr001', 'mr001'],
                            '体育': [34.5, 39.7, 38, 33, 35]})
        df2 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003', 'mr003', 'mr003'],
                            '语文': [110, 105, 109, 110, 108],
                            '数学': [105, 88, 120, 123, 119],
                            '英语': [99, 115, 130, 109, 128]})
        df_merge = pd.merge(df1, df2)
        # df_merge = df_merge.set_index('编号')
        #print(df_merge)
        #df_merge.to_excel(r'.\resource\merge_4_41.xlsx')
        #df_merge.to_csv(r'.\resource\merge_4_41.csv')
        #df_merge.to_csv(r'.\resource\merge_4_41.csv',sep='?')
        #df_merge.to_csv(r'.\resource\merge_4_41.csv', float_format='%.2f')
        #df_merge.to_csv(r'.\resource\merge_4_41.csv', columns=['数学','体育'])
        #df_merge.to_csv(r'.\resource\merge_4_41.csv', header=False)
        #df_merge.to_csv(r'.\resource\merge_4_41.csv', index=True)
        df_merge.to_csv(r'.\resource\merge_4_41.csv', index=False)
    elif testcode == '4_43':
        work = pd.ExcelWriter(r'.\resource\writetest.xlsx')
        pd.set_option('display.unicode.east_asian_width', True)
        df1 = pd.DataFrame({'编号': ['mr001', 'mr002', 'mr003', 'mr001', 'mr001'],
                            '体育': [34.5, 39.7, 38, 33, 35]})
        df1.to_excel(work, sheet_name='df1')
        df1['体育'].to_excel(work, sheet_name='df2')
        work.close()
    elif testcode == '4_44':
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.DataFrame({'原日期':['14-feb-20','02/14/2020','2020.02.14','2020/02/14','20200214']})
        df['转换后的日期']=pd.to_datetime(df['原日期'])
        print(df)
    elif testcode == '4_45':
        df = pd.DataFrame({'year':[2018,2019,2020],
                            'month':[1,3,2],
                           'day':[4,5,14],
                           'hour':[13,8,2],
                           'minute':[23,12,14],
                           'second':[2,4,0]})
        df['组合后的日期'] = pd.to_datetime(df)
        print(df)
    elif testcode == '4_46':
        df = pd.DataFrame({'year': [2018, 2019, 2020],
                           'month': [1, 3, 2],
                           'day': [4, 5, 14],
                           'hour': [13, 8, 2],
                           'minute': [23, 12, 14],
                           'second': [2, 4, 0]})
        df['日期'] = pd.to_datetime(df)
        #df['年'],df['月'],df['日'] = df['日期'].dt.year, df['日期'].dt.month,df['日期'].dt.day
        #df['星期几'] = df['日期'].dt.day_name()
        #df['季度'] = df['日期'].dt.quarter
        df['是否年底'] = df['日期'].dt.is_year_end
        print(df)
    elif testcode == '4_47':
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\mingribooks_4-47.xls')
        df1 = df[['订单付款时间','买家会员名','联系手机','买家实际支付金额']]
        df1 = df1.sort_values(by=['订单付款时间'])
        df1 = df1.set_index('订单付款时间')
        print(df1['2018-05-11':'2018-05-15'])
    elif testcode == '4_48':
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        df = pd.read_excel(r'.\resource\TB2018_4-48.xls')
        df1 = df[['订单付款时间', '买家会员名', '联系手机', '买家实际支付金额']]
        df1 = df1.set_index('订单付款时间')  # 将date设置为index
        #print(df1.to_period('A'))
        #print(df1.to_period('Q'))
        #print(df1.to_period('M'))
        #print(df1.to_period('W'))
        #df2 = df1.resample('AS').sum().to_period('A')
        #df2 = df1.resample('Q').sum().to_period('Q')
        #df2 = df1.resample('M').sum().to_period('M')
        df2 = df1.resample('W').sum().to_period('W')
        print(df2)
    elif testcode == '4_49':
        index = pd.date_range('02/02/2020', periods=9, freq='T')
        series = pd.Series(range(9), index=index)
        print(series)
        print(series.resample('3T').sum())
    elif testcode == '4_50':
        df = pd.read_excel(r'.\resource\time.xls')
        df1 = df[['买家实际支付金额','宝贝总数量','订单付款时间']]
        df1 = df1.set_index('订单付款时间')
        print(df1.resample('W').sum().head())
    elif testcode == '4_51':
        rng = pd.date_range('20200202',periods=2)
        #print(rng)
        s1 = pd.Series(np.arange(1,3), index=rng)
        s1_6h_asfreq = s1.resample('6H').asfreq()
        #print(s1_6h_asfreq)
        #s1_6h_pad = s1.resample('6H').pad()
        #print(s1_6h_pad)
        #s1_6h_ffill = s1.resample('6H').ffill()
        #print(s1_6h_ffill)
        s1_6h_bfill = s1.resample('6H').bfill()
        print(s1_6h_bfill)
    elif testcode == '4_52':
        rng = pd.date_range('2/2/2020',periods=12,freq='T')
        s1 = pd.Series(np.arange(12), index =rng)
        print(s1)
        print(s1.resample('5min').ohlc())
    elif testcode == '4_53':
        index =pd.date_range('20200201','20200215')
        data=[3,6,7,4,2,1,3,8,9,10,12,15,13,22,14]
        s1_data=pd.Series(data,index=index)
        print(s1_data)
    elif testcode == '4_54':
        index = pd.date_range('20200201', '20200215')
        data = [3, 6, 7, 4, 2, 1, 3, 8, 9, 10, 12, 15, 13, 22, 14]
        s1_data = pd.Series(data, index=index)
        s2= s1_data.rolling(3).mean()
        #print(s1_data)
        print(s2)
    elif testcode == '4_55':
        index = pd.date_range('20200201', '20200215')
        data = [3, 6, 7, 4, 2, 1, 3, 8, 9, 10, 12, 15, 13, 22, 14]
        s1_data = pd.Series(data, index=index)
        s2= s1_data.rolling(3,min_periods=1).mean()
        #print(s1_data)
        print(s2)
    elif testcode == '4_e1':
        filearray=[]
        filelocation=glob.glob(r'.\resource\aa\*.xlsx')
        for filename in filelocation:
            filearray.append(filename)
            print(filename)
        res = pd.read_excel(filearray[0])
        for i in range(1, len(filearray)):
            A = pd.read_excel(filearray[i])
            res = pd.concat([res,A], ignore_index=True, sort=False)
        print(res.index)
        #res = res.sort_values(by=['时间'])
        writer = pd.ExcelWriter(r'.\resource\all.xlsx')
        res.to_excel(writer,'sheet1')
        writer.close()

    else:
        pass
if __name__ == '__main__':
    test('4_e1')



