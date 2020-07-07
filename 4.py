# while "C":
#     print("我爱鱼C")


# i = 10
# while i:
#     print("i love xiaoniu")
#     i -= 1


# 10 < const < 50  = (const > 10) and (const < 50 )


# print("hello ");print("i love xiaoniu")

# print("hello" \
# "xiaoniu")

# (print("hello"
# "xiaoniu"))


# print(0 and 3)    #此处用于表现 python中的 "and" 和C语言中的 "&&" 的区别


# import random

# times = 3
# password = random.randint(1,11)

# while times:
#     number = int(input("请猜小牛心中想的一个数（1~10）："))
#     if number == password :
#         print("你太聪明了！")
#         break
#     elif number > password:
#         print("大了大了！")
#     else:
#         print("小了小了！")

#     times -= 1

import random
time = 3
password = random.randint(1,10)
guess = 0
print("请猜一猜小牛心中想的数字（1~10）：", end = "")

while (guess != password) and (time > 0):
    temp = input()
    secret = int(temp)
    time -= 1
    if secret == password:
        print("你真厉害！")
    else:
        if secret > password:
            print("大了大了！")
        else:
            print("小了小了！")
        if time > 0:
            print("还有机会，再试试！")
        else:
            print("没有机会！")
print("游戏结束！")    








# number = int(input("请输入一个数："))
# for each in range(1,number+1):
#     print(each)


# number = int(input("请输入一个数："))
# while number:
#     num1 = number - 1
#     while num1:
#         print(' ',end = "")
#         num1 -= 1
#     num2 = number
#     while num2:
#         print("*", end = "")
#         num2 -= 1
#     print()
#     number -= 1