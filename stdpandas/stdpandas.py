# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas
import pandas as pd

testcode = '38'

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
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
    print(df.notnull())
else:
    pass




