a = 10
def func():
    a = 20
    print(a)
func()
print(globals()) #globals() 获取到全局作用域(内置\全局)中的所有名字
print(locals())  # locals()  查看当前作用域中的所有名字