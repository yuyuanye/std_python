#任意输入三个数字，按从小到大顺序输出。
x = input('x=')
y = input('y=')
z = input('z=')
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)


