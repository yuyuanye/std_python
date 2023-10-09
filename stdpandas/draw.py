import pandas
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

#df = pd.read_excel(r'.\20231009-EBSX12249H00015.xlsx',sheet_name='Sheet2')
#df = pd.read_excel(r'.\20231009min-EBSX12249H00079.xls',sheet_name='Sheet2')
df = pd.read_excel(r'.\20231009sec-EBSX12249H00079.xlsx',sheet_name='Sheet2')
plt.rcParams['font.sans-serif'] = ['SimHei']

gps1 = df['gps1'].to_numpy()
#print(gps1)
len = len(gps1)
a3 =np.arange(1,len+1,1)
a1 = a3/a3
gps1a = gps1
x = range(0, len, 1)

gps2 = df['gps2'].to_numpy()
gps2 = gps2 + a1 + a1
dap = df['dap'].to_numpy()
dap = dap + a1 + a1+ a1 + a1
plt.plot(x, gps1a,color='r')
plt.plot(x, gps2,color='g')
plt.plot(x, dap,color='b')
plt.legend(['gps1','gps2','dap'],loc='lower right')
plt.show()



