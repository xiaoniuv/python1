# str1 = '''Le vent se lève, il faut tenter de vivre. 
# 起风了，唯有努力生存。
# （纵有疾风起，人生不言弃。）'''

# str2 = ('Le vent se lève, il faut tenter de vivre. '
# '起风了，唯有努力生存。'
# '（纵有疾风起，人生不言弃。）')

# str3 = 'Le vent se lève, il faut tenter de vivre. \
# 起风了，唯有努力生存。\
# （纵有疾风起，人生不言弃。）'

# print(str1)
# print(str2)
# print(str3)



# str1 = '<a href="http://www.fishc.com/dvd" target="_blank"> '
# length = len(str1)
# print(length)
# str2 = str1[16:29]
# str3 = str1[-45:-32]
# str4 = str1[20:-27]
# print(str2)
# print(str3)
# print(str4)


# str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
# str2 =  str1[::3] 
# print(str2)




symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>''' 
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
nums = '0123456789' 

password = input("请输入密码：")
length = len(password)
symbol = 0

while (password.isspace() or length == 0):
    password = input("您输入的密码为空(空格),请重新输入：")

if length <= 8:
    flag_len = 1

if 8 <= length <= 16:
    flag_len = 2

else:
    flag_len = 3

flag = 0

for each in password:
    if each in  symbols:
        flag += 1
        break

for each in password:
    if each in chars:
        flag += 1
        break

for each in password:
    if each in nums:
        flag += 1
        break


while True:
    print("您的密码安全级别评定为：", end = "")
    if flag_len == 1 or flag == 1:
        print("低")
    elif flag_len == 2 or flag == 2:
        print("中")
    else:
        print("高")
        print("请继续保持")
        break
    print('''请按以下方式提升您的密码安全级别: \n\
    \t1.密码必须由数字、字母、及特殊字符三种组合 \n\
    \t2.密码只能由字母开头 \n\
    \t3.密码长度不能低于 16位''')
    break


