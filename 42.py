# class Foo:

#     def foo(self):
#         self.foo = "i love 小牛！"
#         return self.foo

# foo = Foo()
# print(foo.foo())

# class Nstr(str):

#     def __sub__(self,other):
#         return self.replace(other," ")

# a = Nstr("i love xiaoniu lala")
# b = Nstr("lala")
# print(a - b)


# class Nstr(str):
#     def __lshift__(self, other):
#         return self[other:] + self[:other]
#     def __rshift__(self, other):
#         return self[:-other] + self[-other:]
# class Nstr(str):
#     def __lshift__(self,other):
#         for i in range(other):
#             hrad_str = self[0]
#             tail_str = self[1:len(self)]
#             self = tail_str + hrad_str
#         return self
#     def __rshift__(self,other):
#         for i in range(other):
#             tail_str = self[len(self)-1]
#             hrad_str = self[0:(len(self) - 1)]
#             self = tail_str + hrad_str
#         return self

# a = Nstr("i love xiaoniu")
# print(a << 1)
# print(a >> 1)

# class Nstr(int):

#     def __new__(cls,arg = 0):
#         if isinstance(arg,str):
#             total = 0
#             for i in arg:
#                 total += ord(i)
#             arg = total
#         return int.__new__(cls,arg)


class Nstr:
    def __init__(self,arg = ''):
        if isinstance(arg,str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("格式错误！")
    
    def __add__(self,other):
        return self.total + other.total
    
    def __sub__(self,other):
        return self.total - other.total
    
    def __mul__(self,other):
        return self.total * other.total

    def __truediv__(self,other):
        return self.total / other.total

    def __floordiv__(self,other):
        return self.total // other.total

    

a = Nstr("xioaniu")
b = Nstr("i love")
print(a + b)
print(a - b)
print(a // b)
