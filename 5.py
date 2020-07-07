# import random

# time = 3
# password = random.randint(1,10)
# guess = 0
# print("请猜一猜小牛心中想的数字（1~10）：", end = "")

# while (guess != password) and (time > 0):
#     temp = input()
#     while not temp.isdigit():
#         print("您输入的不是整数，请重新输入：")
#         temp = input()
#     secret = int(temp)
#     time -= 1
#     if secret == password:
#         print("你真厉害！")
#         break
#     else:
#         if secret > password:
#             print("大了大了！")
#         else:
#             print("小了小了！")
#         if time > 0:
#             print("还有机会，再试试！")
#         else:
#             print("没有机会！")
# print("游戏结束！") 


# temp = input("请输入一个年份：")
# while not temp.isdigit():
#     print("不合法输入，请重新输入")
#     temp = input()
# year = int(temp)

# if (year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):
#     print(temp + "该年是闰年")
# else:
#     print(temp + "该年不是闰年")


