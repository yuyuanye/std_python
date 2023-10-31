number=20
a=2
b=1
s=0
for n in range(1,number+1):
    s=s+a/b
    t=a       #以下三句是程序的关键
    a=a+b
    b=t
print(s)












