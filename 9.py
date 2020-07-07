# for i in range(0,10,2):
#     print("i love xiaoniu")


# times = 3
# password = "i love xiaoniu"
# print("请您输入密码：", end = "")
# while times:
#     times -= 1
#     output = input()
#     if output == password:
#         print("密码输入正确！")
#         break
#     elif "*" in output:
#         print('密码中不能包含"*"您还有',times,"次机会")
#         continue
#     else:
#         print("密码输入错误，您还有",times,"次机会")





# number = 324
# print(number % 10)
# for i in range(1,3):
#     number = number // 10
#     number1 = number % 10
#     print(number1)


# for i in range(100,999):
#     sum = 0
#     temp = i
#     while temp:
#         sum = sum + (temp % 10)**3
#         temp = temp // 10
#     if sum == i:
#         print(i)
    
for red in range(0,4):
    for yellow in range(0,4):
        for green in range (2,7):
            if red + yellow + green == 8:
                print("红球 %d 个，绿球 %d 个，绿球 %d 个" % (red,yellow,green))