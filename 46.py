# class MyDes:
#     def __get__(self,instance,owner):
#         print("getting...")

# class Test:
#     a = MyDes()
#     x = a


# test = Test()
# test.a
# test.x


# class MyDes:
#     def __init__(self,value = None):
#         self.value = value
#     def __get__(self,instance,owner):
#         return self.value - 20
#     def __set__(self,instance,value):
#         self.value = value + 10
#         print(self.value)
    
# class C:
#     x = MyDes()

# if __name__ == "__main__":
#     c = C()
#     c.x = 10
#     print(c.x)



# class MyDes:
#     def __init__(self,value = None):
#         self.value = value
#     def __get__(self,instance,owner):
#         return self.value ** 2
    
# class Test:
#     def __init__(self):
#         self.x = MyDes(3)

# test = Test()
# print(test.x)



# class MyDes:

#     def __init__(self,value = None,name = None):
#         self.value = value
#         self.name = name
#     def __get__(self,instance,owner):
#         print("正在获取变量：" + self.name)
#         return self.value
#     def __set__(self,instance,value):
#         print("正在修改变量：" + self.name)
#         self.value = value
#     def __delete__(self,owner):
#         print("正在删除变量：" + self.name )
#         print("噢~这个变量没法删除")

# class Test:
#     x = MyDes(10,'x')

# test = Test()
# y = test.x
# print(y)
# test.x = 8
# del test.x
# print(test.x)





# import time
# class Record:
#     def __init__(self,value = None,name = None):
#         self.value = value
#         self.name = name
#         self.filename = "Record.txt"

#         pass
    
#     def __get__(self,instance,owner):
#         with open(self.filename,"a",encoding = 'utf-8') as f:
#             f.write("%s 变量于北京时间 %s 被读取, %s = %s\n" %(self.name,time.asctime(),self.name,str(self.value)))
#         return self.value

#     def __set__(self,instance,value):
#         self.value = value
#         with open(self.filename,"a",encoding = 'utf-8') as f:
#             f.write("%s 变量于北京时间 %s 被修改, %s = %s\n" %(self.name,time.asctime(),self.name,str(self.value)))

#     def __delete__(self,instance):
#         with open(self.filename,"a",encoding = 'utf-8') as f:
#             f.write("%s 变量于北京时间 %s 被删除, %s = %s\n" %(self.name,time.asctime(),self.name,str(self.value)))

# class Test:
#     x = Record(10,'x')
#     y = Record(8.8,'y')

# test = Test()
# print(test.x)
# print(test.y)
# test.x = 123
# test.x = 1.23
# test.y = 'i love xiaoniu'


import pickle
import os

class MyDes:
    saved = []

    def __init__(self,name = None):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self,instance,owner):
        if self.name not in MyDes.saved:
            raise ArithmeticError("%s 属性还没有赋值！" % self.name)

        with open(self.filename,'rb') as f:
            value = pickle.load(f)
        return value

    def __set__(self,instance,value):
        with open(self.filename,'wb') as f:
            pickle.dump(value,f)
            MyDes.saved.append(self.name) 

    def __delete__(self,instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)

class Test:
    x = MyDes('x')
    y = MyDes('y')
test = Test()
test.x = 123
test.y = 'i love xiaoniu'
print(test.x)
print(test.y)
