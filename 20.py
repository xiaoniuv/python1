# var = "Hi"

# def fun1():
#     global var
#     var = "baby "
#     return fun2(var)

# def fun2(var):
#     var += "i love you"
#     fun3(var)
#     return var
# def fun3(var):
#     var = "小甲鱼"

# print(fun1())


# def huiwenlian(desstr):
#     list1 = []
#     list2 = []
#     for each in desstr:
#         list1.append(each)
#         list2.append(each)
#     list1.reverse()
#     print(list1)
#     print(list2)
#     if list2 == list1:
#         print("是回文联！")
#     else:
#         print("不是回文联！")

# desstr = input("请输入一句话：")
# huiwenlian(desstr)


def count(*arg):
    length = len(arg)
    
    for i in range(length):
        letter = 0
        number = 0
        space = 0
        other = 0
        for each in arg[i]:
            if each.isalpha():
                letter += 1
            elif each.isdigit():
                number += 1
            elif each == " ":
                space += 1
            else:
                other += 1
        print("第%d个字符串共有：英文字符 %d 个，数字 %d 个，空格 %d 个，其他 %d 个" % (i+1,letter,number,space,other))

if __name__ == "__main__":
    count("i love xiaoniu","i love you, you love me.")