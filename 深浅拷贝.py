# lst = ["张三","李四","王五"]
# lst2 = lst # 列表进行赋值操作,实际上是引用内存地址的赋值,内存中此时只有一个列表,两个变量指向同一个列表.
# lst2.append("赵柳") 对其中一个操作,两个都跟着变  打印的结果一样
# print(lst)
# print(lst2)

# 浅拷贝
# lst1 = ["赵本山","刘能","赵四"]
# lst2 = lst1.copy()  # lst2 和lst1 不是一个对象了
# lst1.append("谢大脚")
# print(lst1,lst2)
# 浅拷贝还有一种写法: lst2 = lst1[:]

# lst1 = ["赵本山","刘能",["赵四","赵武"]]
# lst2 = lst1.copy()   #  浅拷贝,拷贝第一层
# lst1[2].append("谢大脚")
# print(lst1,lst2)


import copy

lst1 = ["赵本山","刘能",["赵四","赵武"]]
lst2 = copy.deepcopy(lst1)  # 吧lst1扔进去进行深度拷贝,包括内部的所有内容
lst1[2].append("谢大脚")
print(lst1,lst2)