# Python不支持以下做法
# def MyFun((x,y),(a,b)):
#     return x * y - a * b
# print(MyFun((1,2),(3,4,)))

#正确的写法
# def MyFun(x,y):
#     return x[0]*x[1] - y[0]*y[1]
# print(MyFun((1,2),(3,4)))




#方法一：
# def Power(x,y):
#     return x**y

# print(Power(2,3))
#方法二：
# def Power(x,y):
#     result = 1
#     for i in range(y):
#         result *= x
    
#     return result
# print(Power(2,3))




#方法一：
# def gcd(x,y):
#     if y == 0:
#         return x
#     return gcd(y,x%y)
# print(gcd(4,6))
#方法二：
# def gcd(x,y):
#     while y:
#         t = x % y
#         x = y
#         y = t
#     return x
# print(gcd(4,6))


#方法一：
def bin2(x):
    str1 = ""
    while x:
        num = x % 2
        x = x // 2 
        str1  += str(num)
    return str1[::-1]
print(bin2(62))

#方法二：
def Dec2bin(dec):
    temp = []
    result = ""

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)
    
    while temp:
        result += str(temp.pop( ))
    
    return result
print(Dec2bin(62))


