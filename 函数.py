# def chi(): #定义一个函数
#     print("洗菜")
#     print("炒菜")
#     print("吃饭")
# chi() # 调用一个函数

# 函数的返回值 return
# def yue():
#     print("yuema")
#     print("buyue")
#     return "hehe" # 函数的返回值, return 当函数结束的时候,给调用方一个结果,
# ret = yue()
#
# ret2 = yue()
# print(ret)
# print(ret2)

# 1.每个函数,如果在函数中不写return,默认返回none
# def yue():
#     print("嗯嗯嗯")
# ret = yue()
# print(ret)

#2.也可以单纯的只写return,也是返回none
# def yue():
#     print("嗯嗯嗯")
#     return
# ret = yue()
# print(ret)

#注意,只要函数执行到return,函数就会停止执行
# def yue():
#     print("嗯嗯嗯")
#     return #函数就停止了
#     print("恩恩额") # 不会执行
# ret = yue()
# print(ret)

#.3.return有多个返回值时,中间用逗号隔开,接收的是元祖
# def ren():
#     print("haoren")
#     print("huairen")
#     return "张三","李四","王五"
# ret = ren()
# print(ret)   # 多个返回值返回结果是tuple类型的数据 ('张三', '李四', '王五')

#既然是元祖类型,可以解构写法,如下:
# def ren():
#     print("haoren")
#     print("huairen")
#     return "张三","李四","王五"
# a,b,c = ren()
# print(a)
# print(b)
# print(c)

#参数:在函数执行的时候,给函数传递的信息
#形参:在函数声明的位置,声明出来的参数
#实参:在函数调用的时候,实际你给函数传递的值
# 函数的参数个数是没有要求的,但是,在运行的时候,形参和实参要匹配,按照位置把实参赋值给形参
# def yue(fangshi, age): # 行参
#     print("打开手机")
#     print("打开%s" % fangshi)
#     print("找一个漂亮妹子")
#     print("年龄最好是%s" % age)
#     print("出来约一约")
# yue("陌陌", 18)
# yue("探探", 20)

#函数的实际应用
# 求1+2+3+...100 之和
# def sum(n):
#     s = 0
#     count = 1
#     while count <=n:
#         s = s + count
#         count = count + 1
#     return s
# ret = sum(100)
# print(ret)

# 计算n是奇数还是偶数

# 动态传参
# def chi(*food):  # 可以传入任意的位置参数
#     print("我要吃",food) #  动态参数接收的是tuple类型的数据
# chi("烧烤","啤酒") # 结果:我要吃 ('烧烤', '啤酒')
#
# # 位置参数>*动态传参>默认值参数
# def func(a,b,c,*an,d = 5):
#     print(a,b,c,d,an)
# func(1,2,3,4,5,6,7)

# 练习,写函数,给函数传递任意个整数,然后返回这些整数和
# def he(*n):
#     sum = 0
#     for e in n:
#         sum += e
#     return sum
# print(he(1,2,3,4))


#动态接收关键字参数
#  *位置参数
#  **关键字参数
# def chi(**food):
#     print(food) # 接收的是字典
# chi(good_food = "面条", bad_food = "辣条")

#函数名的应用
# def func():
#     print("wwww")
# print(func)  # 打印的是函数的内存地址 <function func at 0x000001AC35D8BAE8>

# def func():
#     print("111")
# print(func)
# a = func  # 函数名就是一个变量
# print(a)
# func()
# a()  # 就是一个函数的调用

# def func():
#     print("你吃了吗")
# def a():
#     print("我吃了")
# func = a
# func()   # 打印结果我吃了
#
# def f1():
#     print("1")
# def f2():
#     print("2")
# def f3():
#     print("3")
# lst = [f1,f2,f3]
# print(lst)  # 打印函数的内存地址,如果想打印出每个函数,操作如下:

#
# def f1():
#     print("1")
# def f2():
#     print("2")
# def f3():
#     print("3")
# lst = [f1,f2,f3]
# for el in lst:
#     el() # 结果:1 2 3

# def f1():
#     print("1")
# def f2():
#     print("2")
# def f3():
#     print("3")
# lst = [f1(),f2(),f3()]
# print(lst)

# def f1():
#     print("1")
#     return "a"
# def f2():
#     print("2")
#     return "b"
# def f3():
#     print("3")
#     return "c"
# lst = [f1(),f2(),f3()]  # 调函数,返回值
# print(lst)




# def func():
#     def inner():
#         print("woshishui")
#     return inner
# ret = func()  # 这里func()执行之后获取到的是inner函数
# ret()  # 这里是让inner函数执行

#闭包  在内层函数中调用外层函数的变量,叫闭包.
#特点:可以让一个局部变量常驻内容;防止其他程序改变变量
#可迭代对象:str list tuple set f dict
#所有以上类型中都有一个函数__iter__()
# dir()查看一个对象,数据类型中包含了哪些东西
# def func():
#     name = "abc"
#     def inner():
#         print(name)
#     inner()
# func

# list = [1,2,3]
# print(dir(list))
# print("__iter__" in dir(list))
# s = '__iter__' in dir(list)
# s1 = 2 in list
# print(s1)

#获取迭代器
# list = ["张三","赵四","李六"]
# it = list.__iter__()
# # 迭代往外拿元素 __next__()
# print(it.__next__())   # 张三
# print(it.__next__())  #  赵四
# print(it.__next__()) # 李六
# print(it.__next__()) # 报错

#模拟for循环
# lst = ["紫薇","皇阿玛","小燕子"]
# it = lst.__iter__() # 获取迭代器
# while True:
#     try:
#         name = it.__next__()
#         print(name)
#     except StopIteration :  # 拿完了
#         break

# lst = ["紫薇","皇阿玛","小燕子"]
# from collections import Iterable            # 可迭代的
# from collections import Iterator            # 迭代器
# # isinstance(对象,类型)  判断xx对象是否xx类型的
# print(isinstance(lst,Iterable))
# print(isinstance(lst,Iterator))
# it = lst.__iter__() # 迭代器
# print(isinstance(it,Iterable)) # 判断是否可迭代,迭代器一定是可迭代的
# print(isinstance(it,Iterator)) # 迭代器里一定有__next__(),__iter__()

# 迭代器特点:节省内存,惰性机制,只能往下一个拿值,不能返回来拿值

# 生成器
# def func():
#     print("我是周杰伦")
#     yield "昆凌"  #函数中包含yield,函数就不再是普通函数,是生成器函数
#     print("我是王力宏")
#     yield "李云迪"
#     print("你好啊") # 最后一个yield之后如果再执行__next__() 会报错
# g = func() # 通过func()创建一个生成器
# print(g.__next__())
# print(g.__next__()
# print(g.__next__())
# return 直接返回结果,结束函数的调用
# yield 返回结果,可以让函数分段执行

# send 可以让生成器像下执行一次,也可以给上一个yield传值, 第一个不能用send,最后一个也不要传值,否则会报错

# def eat():
#     print("今天吃什么")
#     a = yield "馒头"
#     print("a=",a)
#     b = yield "大饼"
#     print("b=",b)
#     c= yield "韭菜盒子"
#     print("c=",c)
#     yield "GAME OVER"
# gen = eat()
# ret1 = gen.__next__()
# print(ret1)
# ret2 = gen.send("胡辣汤")
# print(ret2)
# ret3 = gen.send("狗粮")
# print(ret3)
# ret4 = gen.send("猫粮")
# print(ret4)

# 推导式
# lst = []
# for i in range(1,15):
#     lst.append(i)
# print(lst)
#列表推导式,最终给到的是列表
# 语法:[最终结果(变量) for 变量 in 可迭代对象]
lst = [i for i in range(1, 15)]
print(lst)
lst = [i for i in range(1, 15) if  i % 3 ==1]
print(lst)
lst = [i for i in range(1, 15) if i % 5 ==0]
print(lst)