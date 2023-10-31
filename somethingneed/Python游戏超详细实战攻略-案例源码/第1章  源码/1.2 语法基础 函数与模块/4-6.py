def fac(n):
   if n==1: 					#递归调用结束的条件
      p=1
   else:
      p=(fac(n-1)*n)				#调用f( ) 函数本身
   return p
x=int(input("输入一个正整数:"))
print(fac(x))