# class Nint(int):
#     def __radd__(self, value):
#         print("__radd__被调用了！")
#         return int.__add__(self,value)

# a = Nint(5)
# b = Nint(3)
# print(a + b)
# print(1 + b)



#在继承的类中调用基态的方法：
# class Derived(Base):
#     def meth(self):
#         super(Derived,self).meth()



# BaseAlias = BaseClass #为基类取别名
# class Derived(BaseAlias):
#     def meth(self):
#         BaseAlias.meth(self) #通过别名访问基类


# class C:
#     count = 0

#     def __init__(self):
#         C.count += 1
    
#     def getCount(self):
#         return C.count



# class C:
#     @staticmethod #该修饰符表示 static() 是静态方法
#     def static(arg1, arg2, arg3):
#         print(arg1, arg2, arg3,arg1 + arg2 + arg3)
#     def nostatic(self):
#         print(r"i'm the f**king normal method")

# c1 = C()
# c2 = C()
# print(c1.static(1,2,3))
# print(C.static(1,2,3))


# class C:
#     def __init__(self, *args):
#         if not args:
#             print("没有参数传递！")
#         else:
#             print("传入了%d个参数，分别是:" % len(args), end = "\n")
#             for each in args:
#                 print(each,end = " \n")
# a = C(1,2,3,4)
# b = C("fishc")


import operator
class Word(str):

    def __new__(cls, word):
        if " " in word:
            word = word[:word.index(" ")]
        return str.__new__(cls,word)

    def __gt__(self, other):
        return len(self) > len(other)   
    def __lt__(self,other):
        return  len(self) < len(other)
    def __ge__(self,other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

a = Word("ilovexiaoniu")
b = Word("nihao")
print(operator.eq(a,b))