# def __setattr__(self,name,value):
#     self.__dict__[name] = value + 1

# def __setattr__(self,name,value):
#     super().__setattr__ = value + 1



# class C:
#     def __getattr__(self, name):
#         print(1)
#     def __getattribute__(self,name):
#         print(2)
#     def __setattr__(self, name, value):
#         print(3)
#     def __delattr__(self, name):
#         print(4)
# c = C()
# c.x = 1
# print(c.x)


# class C:
#     def __getattr__(self,name):
#         print(1)
#         return super().__getattr__(name)
    
#     def __getattribute__(self, name):
#         print(2)
#         return super().__getattribute__(name)

#     def __setattr__(self, name, value):
#         print(3)
#         super().__setattr__(name, value)

#     def __delattr__(self, name):
#         print(4)
#         super().__delattr__(name)

# c = C()
# c.x


# class Counter:
#     def __init__(self):
#         self.counter = 0 #这里会触发__setattr__
#     def __setattr__(self,name,value):
#         self.counter += 1 #既然需要__setattr__调用后才能真正设置self.counter的值，所以这时候self.counter 还没有定义，所以没法 += 1，错误的根源
#         super.__setattr__(name,value)
#     def __delattr__(self, name):
#         self.counter -= 1
#         super().__delattr__(name)


# class Demo:
#     def __getattr__(self,name):
#         return "该属性不存在！"
# demo = Demo()
# print(demo.c)


# class Demo:
    
#     def __getattr__(self,name):
#         self.name = "FishC"
#         return self.name


# demo = Demo()
# print(demo.x)
# demo.x = "X-man"
# print(demo.x)
    

class Counter:

    def __init__(self):
        super().__setattr__('counter',0)

    def __setattr__(self,name,value):
        super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name,value)

    def __delattr__(self, name):
        super().__setattr__('counter', self.counter - 1)  
        super().__delattr__(name)

c = Counter()
c.x = 1
print(c.counter)
c.y = 1
c.z = 1
print(c.counter)
del c.x
print(c.counter)