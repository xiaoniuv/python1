
# def fun_A(x,y = 3):
#     return x * y
# p = lambda x,y = 3 : x * y
# print(p(2,3))

lambda x : x if x % 2 else None
def fun_B(x):
    if x % 2 :
        return x
    else:
        return None



# a = filter(lambda x:x % 3 == 0,range(100))
# print(a)


# print(list(map(lambda x,y:[x,y],[1,3,5,7,9],[2,4,6,8,10])))


