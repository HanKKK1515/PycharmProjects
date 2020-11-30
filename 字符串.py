# 索引  就是下标，注意， 下标从o开始
# s = '我爱周杰伦他媳妇'
# print(s[2])    #第二个位置是  周

#     切片 可以对字符串进行截取
#     语法 s [起始位置: 结束位置]
#  特点：顾头不顾尾
# s = '周杰伦唱歌很好听'
# # s1 = s[2: 5]   # 轮唱歌
# # print(s1)
# s1 = s[2:] # 结尾什么都不写，默认截取到结尾 若从0开始截取，开头也可以不写，从头截取到尾写法[:]
# print(s1)
# s2 = s[:]  #  从头截取到尾写法[:]
# print(s2)
# s3 = s[-2:] # 从-2切到结尾，默认从左往右切
# print(s3)

#    步长
#   语法：  s[起始位置:结束位置:步长]
# s = '我是梅西，我很慌'
# s1 = s[1:5:2]    #  从1 开始，到5结束， 每2个取1个。这个不太懂
# print(s1) # 是西

# s = '我是梅西，我很慌'
# s1 = s[1::3]   #从第1位取到尾，每3个取1个。
# print(s1)  # 是,慌

# s = '我是梅西，我很慌'
# # s1 = s[::3]
# # print(s1)   # 我西很
# s2 = s[6:2:-2]
# print(s2)   # 很,  -表示反着来，每两个取1个

# s = '这个标点符号很不好'
# # s1 = s[7::-2]
# # print(s1)
# s2 = s[-1:-6:-2]
# print(s2)  #从-1开始取，-1是好  因为0是没有负数的 所以-1从好开始取

# s = 'da sha zi and xiao sha zi'
# s1 = s.capitalize() # 首字母大写
# print(s)
# print(s1)

# s = 'Alex is not a Good Man'
# print(s.upper()) #  大写
# print(s.lower()) #  小写#
# # 在程序需要判断不区分大小写的时候使用

# while True:
#     content = input('请喷:')
#     if content.upper() == 'Q':
#         break
#     print('你喷了：',content)

# username = input('用户名:').strip()  # 去空格
# password = input('密码:').strip()
# if username =='abc' and password =='123':
#     print('登录成功')
# else:
#     print('登录失败')

# s = '马化腾随便啊随地随便打的哈哈哈'
# print(s.strip('马化腾'))         # strip去掉的是左右两边内容，不去中间

# s = '我叫{},我今年{},喜欢{}'.format('wang',18,'lulu')
# print(s)       # 跟%s一样用法，格式化输出

# s = '我叫{1},我今年{0},喜欢{2}'.format('wang',20,'lulu')
# print(s)
#
# s = '我叫{name},我今年{age},喜欢{mingxing}'.format(name='wang',mingxing='lulu',age=18,)
# print(s)

# 查找
# s = "汪峰的老婆不爱汪峰"
# print(s.startswith("汪峰"))  #  判断字符串是否以xxx开头
# print(s.endswith("汪"))  #    ....结尾
# print(s.count("guoji")) #   计算xxx在字符串中出现的次数
# print(s.find("老婆不"))  #  计算xx字符串在原字符串中出现的位置，‘老婆不’当成一个整体，去比较。如果没有出现返回 -1
# print(s.find("汪峰",3))   #  3范围 从位置3开始取
# print(s.index("gg")) # 跟find功能一样，但是index中的内容如果不存在，直接报错

#条件判断
# s = "abc"
# # print(s.isdigit())  # 判断字符串是否由数字组成
# # print(s.isalpha())  # 判断是否由字母组成
# print(s.isalnum()) # 是否由字母和数字组成

# #len()   字符串长度
# s = "你今天喝酒了吗"
# i = len(s)
# print(i)

# 把字符串从头到尾进行遍历
# s = "小学老师，你好漂亮"
# print(len(s))  #  长度是8  索引到7
# count = 0
# while count <len(s):
#     print(s[count])
#     count = count + 1

# for循环  优势：简单 劣势：没有索引
s = "小学老师，你好漂亮"
for c in s:  # 把s中的每一个字符交给前面c循环，c是自己随便定义
    print(c)
