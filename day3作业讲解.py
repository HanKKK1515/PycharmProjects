# name = "alex leanb"
# s1 = name[:1]
# print(s1)
# s2 = name[1:]
# print(s2)
# print(s1.upper() + s2)

# s = "123a4b5c"
# s1 = s[:3]
# print(s1)

# s = "adbdfe"
# for c in s:
#     print(c)

# s = "321"
# for c in s:
#     print("倒计时%s秒" % c)
# else:
#     print("出发！")

# content = input("请输入内容：")
# count = 0
# for c in content:
#     if c.isdigit():
#         count = count + 1
# print(count)   #  输入的数字统计个数

# 计算 1-2+3-4....+99 去掉88
count = 1
sum = 0
while count <100:
    if count == 88:
        count = count + 1
        continue
    if count %2 == 0: #偶数
        sum = sum -count
    else:
        sum = sum + count
    count = count + 1
print(sum)