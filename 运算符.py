# a = 10
# a +=20 # a=a+20
# print(a)

# print(3>4 or 4<3 and 1==1)
'''逻辑运算
and 并且的意思，左右两顿的值必须都是真，运算结果才是真
or  或者的意思，左右两端有一个是真的，结果就是真，全部都是假，结果才是假
not  非的意思，原来是假，现在是真，非真即假，  非假即真
and or not 同时存在，先算括号，然后算not，然后算and，最后算or
'''
# print(1 < 2 and 3< 4 or 1>2)

# print(1 > 2 and 3 < 4 or 4> 5 and 2 > 2 or 9 < 9) # false
# x or y  如果x==0 那么就是y 否则就是x
# print(1 or 2)
# print(2 or 3)
# print(0 or 3)
# print(0 or 4)

# and跟or是反着来的
# print(1 and 2)  # 2
# print(2 and 0)  # 0
# print(0 and 3) # 0
# print(0 and 4) # 0

# count = 1
# n = 66
# while count <= 3:
#     num = input('猜一下是多少:')
#     if int(num) > n:
#         print('猜大了')
#     elif int(num) < n:
#         print('猜小了')
#     else:
#         print('猜对啦')
#         break
#     print('你已经猜了%d次了' % count)
#     count = count + 1
# else:
#     print('蠢货啊蠢货')


# 求1-2+3-4+5....99所有数的和
# sum = 0
# count = 1
# while count <100:
#     if count%2 ==0:  # 奇数
#         sum = sum - count
#     else:
#         sum = sum + count
#     count = count + 1
# print(sum)     # 计算结果等于50

# 登录 三次机会
# count = 1
# while count <= 3:
#     username = input('请输入你的用户名:')
#     password = input('请输入密码')
#     if username == 'alex' and password == 'sb':
#         print('登录成功')
#         break
#     else:
#         print('登录失败')
#     print('还剩余%d次机会' % (3 - count))
#     count = count + 1
# else:
#     print('蠢货啊')


while True:
    fen = input("请输入成绩:")
    if fen == "q":
        break
    elif int(fen)<60:
        print("成绩不合格")
    elif int(fen) > 70 and int(fen)<80:
        print("合格")
    else:
        print("ddd")




