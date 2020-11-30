# f = open("姓名",mode = "r",encoding="utf-8")
# s = f.read()
# f.close()
# print(s)

# f = open("年龄",mode = "w",encoding="utf-8")
# s = f.write("20")  # w写入之前会清掉原来内容  , a 在原来的基础上追加内容
# f.flush()
# f.close()


# f = open("年龄",mode = "r+",encoding="utf-8") # r+模式,默认情况下光标在在文件的开头,必须先读后写
# s = f.read()
# f.write("30")
# f.flush()
# f.close()


# f = open("写读",mode = "w+",encoding="utf-8")      # w操作会清空原来的内容,基本不用
# f.write("你好ffff吗")
# f.flush()
# f.close()


# f = open("姓名",mode = "r+",encoding="utf-8")
# s = f.read(3)
# # 不管你前面读了几个,后面去写都在末尾
# f.write("wangwan")  # 在没有任何操作前,进行写,写的内容在开头.如果读了些内容,在写,写的东西在末尾  都是覆盖插入
# f.flush()
# f.close()
# print(s)


# f = open("姓名",mode = "r+",encoding="utf-8")
# f.write("二货")
# f.flush()
# f.close()


#二货热,王五,狗六,哈哈哈wangwangwangwangwangwangwangwan
# f = open("姓名",mode = "r+",encoding="utf-8")
# f.seek(6)  # 移动6个字节,2个字
# s = f.read(3) #读取3个字
# print(s)
# f.seek(0) # 光标移动到开头
# #f.seek(0,2) 末尾  第二个参数有3个值,0 开头,1 当前,2 末尾
# ss = f.read(3)
# print(ss)


# f = open("姓名",mode = "r+",encoding="utf-8")
# f.read(3)
# print(f.read(3))

#文件修改写法一:
# import os  #  固定格式
# with open("吃的", mode = "r+", encoding= "utf-8") as f1, open("吃的_副本", mode = "w" ,encoding= "utf-8") as f2:
#     s = f1.read()
#     ss = s.replace("肉","蔬菜")
#     f2.write(ss)
# os.remove("吃的")
# os.rename("吃的_副本", "吃的")
#总结: 先读取内容,然后替换,再将替换的东西添加到新文件中,然后删除老文件,将新文件重命名
#zz总结:with写法,不需要关闭文件句柄


#文件修改写法二:
# import os
# with open("吃的", mode = "r+", encoding= "utf-8") as f1, open("吃的_副本", mode = "w" ,encoding= "utf-8") as f2:
#     for line in f1:
#         s = line.replace("肉","菜")
#         f2.write(s)
#
# filename = "姓名.txt"
# with open(filename,"a",encoding= "utf-8") as file_object:  # a附加模式,直接写入在文件末尾,不会替换掉之前的内容
#     file_object.write("redf\n")  # \n换行符
#     file_object.write("kik")

# while 1:
#     content = input("请输入姓名:")
#     print(content + "下午好哦!")
#     if content == "q":
#         break
#     with open("姓名.txt", "a", encoding="utf-8") as file_object:
#         file_object.write("\n" + content)

# # 异常
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print( "不能除0")



print("输入两个数,求商")
print("按'q' 退出")
while 1:
    num1 = input("第一个数是:")
    if num1 == "q":
        break
    num2 = input("第二个数是:")
    if num2 == "q":
        break
    try:
        answer = int(num1)/ int(num2)
    except ZeroDivisionError:
        print(" 不能除0")
    else:
        print(answer)