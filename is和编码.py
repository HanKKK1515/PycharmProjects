# s = "张三是个大傻子"
# abc = id(s)    # 得到内存地址
# print(abc)

# lst = ["fbb","hhh","lll"]
# print(id(lst))  #就是一个内存地址,毫无意义

# s = "abc"
# s1 = "abc"
# print(id(s))
# print(id(s1))

# lst = ["heh","eref","dfef "]
# lst1 = ["heh","eref","dfef "]
# print(id(lst))
# print(id(lst1))

# tu = ("dhf ","dfer")
# tu1 = ("dhf ","dfer")
# print(id(tu))
# print(id(tu1))

#dic = {"keed":"ede","edf":"fffd"}
# dic1 = {"keed":"ede","edf":"fffd"}
# print(id(dic))
# print(id(dic1))

# a = 1999999
# b = 1999999
# print(id(a))
# print(id(b))

# a = True
# b = True
# print(id(a))
# print(id(b))

# -5
# a = 20
# b = 20
# print(id(a))
# print(id(b))

# == is id
# == 判断. 左右两端是否相等和一致, 比较的是内容
# is 判断. 判断的是内存地址  id()的值来判断    内存地址
# lst = ["madd","dfef","dferf "]
# lst1 = ["madd","dfef","dferf "]
# print(lst == lst1)   #  true
# print(lst is lst1)  # false

# lst = ["madd","dfef","dferf "]
# lst1 = lst
# print(lst == lst1)  #true
# print(lst is lst1)  #true
# print(id(lst))
# print(id(lst1))


# encode() 编码之后的内容是bytes类型的数据
# s = "饿了么"
# bs = s.encode("GBK")
# print(bs)    # b'\xb6\xf6\xc1\xcb\xc3\xb4' GBK 一个中文:２个字节



# s = "中"
# print(s.encode("utf-8"))
# print(s.encode("GBK"))

#decode()解码
# bs = b'\xb6\xf6\xc1\xcb\xc3\xb4'
# s = bs.decode("GBK")
# print(s)  # 打印出 饿了么

# GBK => utf-8
bs = b'\xb6\xf6\xc1\xcb\xc3\xb4'   # 国标码
s = bs.decode("GBK")
print(s)        #  打印结果:饿了么
bss = s.encode("UTF-8")
print(bss)
