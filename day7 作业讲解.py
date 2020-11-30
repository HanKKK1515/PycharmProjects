# for i in range(1, 11):
#     fen = input("请%d评委打分:" % i)
#     if int(fen) > 5 and int(fen) < 10:
#         print("分数ok")
#     else:
#         print("不在有效范围内")

# i = 1
# while i <11:
#     fen = input("请%d评委打分:" % i)
#     if int(fen) > 5 and int(fen) < 10:
#         print("分数ok")
#     else:
#         print("不在有效范围内")
#         continue
#     i = i + 1

# lst = ["abc","def","ghi"]
# lst.clear()
# print(lst)
# list在循环中不能删,会改变索引
# lst = ["abc","def","ghi"]
# del_lst = ["abc","def","ghi"]
#
# # del_lst = []
# # for el in lst:
# #     del_lst.append(el) # 记录下来要删的内容
# for el in del_lst:     #循环记录下的内容
#     lst.remove(el) # 删除原来的内容
# print(lst)

lst = ["a","b","c","a","c"]
s = set(lst)
print(s)
lst = list(s)
print(lst)
tu = tuple(lst)
print(tu)