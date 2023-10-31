【例4-5】求1到5的平方和。
def f(x):
   if x==1: 						#递归调用结束的条件
      return 1
   else:
      return(f(x-1)+x*x)				#调用f( ) 函数本身
print(f(5))