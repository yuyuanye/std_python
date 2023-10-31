【例4-4】使用闭包的例子。
def func_lib():
    def add(x, y):
        return x+y
    return add       # 返回函数对象

fadd = func_lib()
print(fadd(1, 2))