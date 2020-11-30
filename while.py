'''
count = 1


while count <=30:
    print("你是大傻子吗")
    print("嗯是啊撒")
    count = count + 1

while True:
    s = input("请开始喷：")
    if s == 'q':
        break
    if "马化腾" in s:
        print("输入非法")
        continue
    print("喷的内容是：" + s)


count = 1
sum = 0
while count <= 100:
    print(count)
    sum = sum + count
    count = count + 1
print(sum)

count = 1
while count <= 100:
    if count % 2 != 0:
        print(count)
    count = count + 1
'''

# name = input("请输入姓名")
# age = input(' 年龄 ')
# gender = input("输入年龄")
#print(name + '今年' + age +'岁,是一个老头,性别：' + gender)
# %s  字符串占位符     %d   数字的专用占位符
# print("%s 今年%s岁，是一个老头，性别：%s" % (name, age, gender))

# name = "all"
# print("%s已经喜欢了班里%%40的女生" % (name))# 坑：注意，如果字符串有了占位符，那么后面的%都默认为占位，如果需要% 就要转义，用%%
print("shazi喜欢了%30女生")  这句话里没有站位符，%还是%