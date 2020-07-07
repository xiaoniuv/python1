
# name = input("请输入要查找的用户名：")
# print(type(name))
# score = [[' 迷途 ', 85], [' 黑夜 ', 80], [' 小布丁 ', 65], [' 福禄娃娃 ', 95], [' 怡静 ', 90]] 
# isfind = False
# i = 0
# for each in score:
#     i += 1
#     if name in each:
#         print(name + '的得分是:', each[1])
#         isfind = True
#         break
#     print(i)

# if isfind == False:
#     print("查找的数据不存在！")



# def min(x):

#     least = x[0]

#     for each in x:
#         if least > each:
#             least = each
#     return least

# print(min('1230456789'))


def sum(x):

    result = 0

    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue
    return result

print(sum([1,2,3,'a']))