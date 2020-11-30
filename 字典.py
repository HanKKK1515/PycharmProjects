# dict = {"jay":"周杰伦","jj":"林俊杰","eason":"陈奕迅"}
# print(dict)
#
# dict = {"wo":"hehe"}
# dict["ni"] = "haha"   #  增加  如果keychongf,会替换掉原来数据
# dict.setdefault("马蓉","王宝强前任")
# dict.setdefault("马蓉","宋哲现任")  # 也可以新增,但是如果字典中已包含这个key,不在继续保存
# print(dict)

# dict = {"jay":"周杰伦","jj":"林俊杰","eason":"陈奕迅","ni":"大傻子","我":"哈哈","你是谁":"你猜啊"}
# dict.pop("jay")
# del dict["jj"]
# dict.popitem()  # 随机删
# print(dict)

# 查询
# dict = {"jay":"周杰伦","jj":"林俊杰","eason":"陈奕迅","ni":"大傻子","我":"哈哈","你是谁":"你猜啊"}
# print(dict["ni"])    # 如查询东西找不到,会报错
# print(dict.get("jj"))   # 查询不到,会返回none  ,也可以给一个默认值,当key不存在时返回它

#1,首先判断字典里有没有这个key,没有,就执行新增,2用这个key去字典 中查询,返回查询结果
# dict = {"jay":"周杰伦","jj":"林俊杰","eason":"陈奕迅"}
# ret = dict.setdefault("西门庆","潘金莲")
# print(dict)
# print(ret)

# dict = {"jay": "周杰伦", "jj": "林俊杰", "eason": "陈奕迅"}
# # print(dict.keys())  # 拿到所有的key,返回key的集合,像是列表,但不是列表
# # print(dict.values())
# # for key in dict.keys():
# #     print(key)
# #print(dict.items())  # 拿到键值对
# for k,v in dict.items():
#     print(k,v)

#字典的嵌套
# dic = {
#     "name":"周杰伦",
#     "age":40,
#     "wife":{
#         "name":"hehe",
#         "age":20,
#         "salay":20000
#
#     },
#
#     "baby":[
#         {"name":"laoda","age":2},
#         {"name":"laoer","age":1}
#
#
#     ]
# }
# #print(dic)
#
#
# print(dic["wife"]["salay"])
# print(dic["baby"][1]["age"])

dict = {"jay":"周杰伦","jj":"林俊杰","eason":"陈奕迅","ni":"大傻子","我":"哈哈","你是谁":"你猜啊"}
for a in dict:
    #print(a)  #  直接循环字典,拿到的是key
    print(dict[a])  # 拿字典的value