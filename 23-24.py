# def Dec2Bin(num):
#     list1 = []
#     str1 = ""
#     while num:
#         quo = num % 2
#         num = num // 2
#         str1 += str(quo)
#     return str1[::-1]

# print(Dec2Bin(20))


# def Dec2Bin(num):
#     result = ""
#     if num == 0:
#         return result
#     else:
#         result  = Dec2Bin(num // 2)
#         return result +str(num % 2)
# print(Dec2Bin(62))


# def get_digits(n):
#     list1 = []
#     while n:
#         quo = n % 10
#         n = n // 10
#         list1.append(quo)
#     list1.reverse() 
#     return list1
# print(get_digits(12345))


# list1 = []
# def get_digits(n):
#     if n == 0:
#         return n
#     else:
#         quo = n % 10
#         list1.append(quo)
#         get_digits(n // 10)
# get_digits(123456)
# list1.reverse()
# print(list1)



# def Sub(n):
#     result = 0
#     if n == 1:
#         return 10
#     else:
#         return result + 2 + Sub(n - 1)
# print(Sub(5))


def palindrome(n,start,end):
    if start > end:
        return 1
    else:
        return palindrome(n,start+1,end-1) if n[start] == n[end] else 0

string = input("请输入一串字符串：")
length = len(string) - 1

if palindrome(string,0,length):
    print('\"%s\"是回文字符串：' % string)
else:
    print('\"%s\"不是回文字符串：' % string)