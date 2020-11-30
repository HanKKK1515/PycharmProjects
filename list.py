# lst = [1,"太白","wusir",["马化腾",["可口可乐"],"王健林"]]
# # print(lst[3][1][0]) # d打印可口可乐
# lst[3][1].append("芬达")
# print(lst)

# range()
# for i in range(10): #  从0开始，到10结束，不取10，取到9
#     print(i)

# 求1-2+3-4......+99-100=？
# sum = 0
# for i in range(1,101):
#     if i % 2 ==0:
#         sum = sum - i
#     else:
#         sum = sum + i
# print(sum)

# 练习  ["alex" ,"eric","rain"], 打印成alex_eric_rain
# li = ["alex","eric","rain"]
# s = ""
# for el in li:
#     s = s + el + "_"
# print(s[:len(s)-1])

# li = ["alex","eric","rain"]
# for i in range(len(li)):
#     print(i)

# 利用for循环和range找出100以内所有偶数并将这些偶数插入到一个新表中
# lst = []
# for i in range(1,101):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)
# lst = []
# for i in range(50):
#     if i % 3 ==0:
#         lst.append(i)
# print(lst)
#
# for i in range(100,0,-1):
#     print(i)

# for i in range(100,9,-1):
#     print(i)   #  倒着取到10

# li = ["马云","马化腾","傻子"]
# content = input("请输入你的评论:")
# for el in li:
#     if el in content:
#         content = content.replace(el,"*" * len(el))
# print(content)

# 把班级学生数学考试成绩录入到一个列表中：并求平均值，要求，录入的时候要带着
# 学生姓名和成绩，例如：张三_44
lst = []
while 1:
    stu = input ("请输入学生的姓名和成绩(姓名_成绩),输入Q退出录入:")
    if stu.upper() == "Q":
        break
    lst.append(stu)

# 求平均值
sum = 0
for el in lst:
    li = el.split("_")
    sum += int(li[1])
print(sum/len(lst))
