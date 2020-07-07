# def showMaxFactor(num):
#     count = num // 2 
#     while count > 1:
#         if num % count == 0:
#             print("%d的最大公约数是%d" % (num,count))
#             break
#         count -= 1
#     else:
#         print("%d是素数" % num)

# num = int(input("请输入一个数："))
# showMaxFactor(num)


# try:
#     print("ABC")
# except:
#     print("DEF")
# else:
#     print("GHI")
# finally:
#     print("JKL")



# try:
#     with open("data.txt","w") as f:
#         for each_line in f:
#             print(each_line)
# except OSError as reason:
#     print("出错了：" + str(reason))



print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1:查询联系人资料  ---|')
print('|--- 2:插入新的联系人  ---|')
print('|--- 3:删除已有联系人  ---|')
print('|--- 4:退出通讯录程序  ---|')

contacts = dict()

while True:
    temp = input("\n请输入相关代码：")
    instr = int(temp)

    if instr == 1:
        name = input("请输入联系人姓名：")
        try:
            print(name + ":" + contacts[name])
        except KeyError:
            print("您输入的姓名不在通讯录中！")
    
    if instr == 2:
        name = input("请输入联系人姓名：")
        try:
            print(name + ":" + contacts[name])
            print("您输入的姓名在通讯录中已存在--->>",end = "\n")
            if input("是否修改用户资料（YES/NO):") == "YES":
                contacts[name] = input("请输入用户联系电话：")
        except KeyError:
            contacts[name] = input("请输入用户联系电话：")
    
    if instr == 3:
        name = input("请输入联系人姓名:")
        try:
            del(contacts[name])
        except KeyError:
            print("您输入的联系人不存在。")
    
    if instr == 4:
        break

print("|--- 感谢使用通讯录程序---|")


    

