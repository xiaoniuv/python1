# def power(x,y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x,y-1)
# print(power(2,3))


# def gcd(x,y):
#     if y == 0:
#         return x
#     else:
#         return gcd(y,x%y)
# print(gcd(4,6))


# def feibonaqi(max):
#     x = 1;y = 1
#     while max > 0:
#         x,y = y,x+y
#         max -= 1
#     return x
# for i in range(20):
#     print(feibonaqi(i), end = " ")


def feibonaqi(n):
    assert n >= 0,"n > 0"
    if n <= 1:
        return n
    return feibonaqi(n-1) + feibonaqi(n-2)
for i in range(20):
    print(feibonaqi(i),end = " ")
