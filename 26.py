# a = {1:"one",2:"two",3:"three"}
# print(a)
# c = a
# b = a.copy()
# del a[1]
# print(b)
# print(a)
# print(c)


# def contact():
#     print("|-------新建用户：N/n--------|")
#     print("|-------登陆账户：E/e--------|")
#     print("|-------退出程序：Q/q--------|")
#     contact_dict = {}
#     while True:
#         instr = input("|-------请输出代码指令：")
#         print(instr,type(instr))

#         if instr == "N" or instr == "n":
#             name = input("请输入用户名：")
#             while name in contact_dict:
#                 name = input("此用户名已经被使用，请重新输入:")
#             if name not in contact_dict:
#                 contact_dict[name] = input("请输入密码：")
#                 print("注册成功，赶紧登陆试试吧！")
        
#         if instr == "E" or instr == "e":
#             name = input("请输入用户名：")
#             if name in contact_dict:
#                 password = input("请输入密码：")
#                 while password != contact_dict[name]:
#                     password = input("密码输入错误，请重新输入：")
#                 break
#             else:
#                 name = input("用户不存在，请重新输入:")
#                 if name in contact_dict:
#                     password = input("请输入密码：")
#                     while password != contact_dict[name]:
#                         password = input("密码输入错误，请重新输入：")
#                 else:
#                     continue
        
#         if instr == "Q" or  instr == "q":
#             break
#     print("欢迎进入XXOO系统，请点击右上角的x关闭程序")


# if __name__ == "__main__":
#     contact()



user_date = {}

def new_user():
    prompt = "请输入用户名："

    while True:
        name = input(prompt)
        if name  in user_date:
            prompt = "用户名已经被使用，请重新输入："
            continue
        else:
            break
        
    password = input("请输入密码：")
    user_date[name] = password
    print('注册成功，赶紧登陆试试吧(*^_^*)！')

def old_user():
    prompt = "请输入用户名："
    while True:
        name = input(prompt)
        if name not in user_date:
            prompt = "您输入的用户名不存在："
            continue
        else:
            break
    password = input('请输入密码：')
    pwd = user_date.get(name)
    if password == pwd:
        print("欢迎进入XXOO系统，请点击右上角的X结束程序！")
    else:
        print("密码错误！")

def showmenu():
    prompt = '''
|------新建用户：N/n------|
|------登陆账号：E/e------|
|------退出程序：Q/q------|
|------请输入指令代码：'''

    while True:
        chosen = False
        while not chosen:
            choice =  input(prompt)
            if choice not in "NnEeQq":
                print("您输入的指令代码错误，请重新输入：")
                continue
            else:
                chosen = True
        if choice == "q" or choice == "Q":
            break
        if choice == "n" or choice == "N":
            new_user()
        if choice == "e" or choice == "E":
            old_user()
showmenu()
