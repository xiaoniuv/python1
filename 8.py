# # x = 1,y = 2,z = 3 如何迅速使三个变量互换


# x = 1; y = 2; z = 3
# x,y,z = z,y,x
# print(x,y,z)


# score = int(input("请输入分数："))
# if 80 > score >= 60:
#     temp = "C"
#     print(score,"->",temp)
# elif 90 > score >= 80:
#     temp = "B"
#     print(score, "->",temp)
# elif 100 > score >= 90:
#     temp = "A"
#     print(score, "->",temp)
# elif score < 60:
#     temp = "D"
#     print(score,"->",temp)
# else:
#     print("输入错误")


x = 4; y = 5;z = 6

#三元操作符的使用
small = x if(x < y and x < z) else (y if y < z else z)
print(small)