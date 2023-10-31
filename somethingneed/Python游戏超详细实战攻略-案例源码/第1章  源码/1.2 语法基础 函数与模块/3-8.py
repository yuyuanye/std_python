i = 1
p = 1
sum_e = 1;
t=1/p
while t>0.00001
    p=p*i;    // 计算i的阶乘
    t=1/ p;
    sum_e=sum_e+t;
    i = i + 1;		//为计算下一项作准备
print("自然对数e的近似值" ,sum_e);








