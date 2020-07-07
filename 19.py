# def mfun(*param,base = 3):
#     result = 0
#     for each in param:
#         result += each
#     result *= base

#     return result

# print(mfun(1,2,3,4,5,base = 5))


# def Narcissus():
#     for each in range (100,1000):
#         temp = each 
#         result = 0
#         while temp:
#             result += (temp % 10)**3
#             temp = temp // 10
#         if result == each:
#             print(each,end = "\t")

# print("所有的水仙花数分别是:",end = "")

# if __name__ == "__main__":
#     Narcissus()



def findstr(desstr,substr):
    count = 0
    length = len(desstr)
    if substr not in desstr:
        print("在目标字符串中未找到字符串")
    else:
        for each in range(length - 1):
            if desstr[each] == substr[0]:
                if desstr[each + 1] == substr[1]:
                    count += 1
        print('字符串在目标字符串中出现了 %d 次' % count)

desstr = input("请输入目标字符串：")
substr = input("请输入字符串(两个字符串)：")
findstr(desstr,substr)