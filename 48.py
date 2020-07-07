
# string = "Fishc"
# i = iter(string)
# while True:
#     try:
#         each = next(i)
#     except StopIteration:
#         break
#     print(each)


# class fib:

#     def __init__(self,n):
#         self.a = 0
#         self.b = 1
#         self.n = n
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.a,self.b = self.b,self.a + self.b
#         if self.a > self.n:
#             raise StopIteration
#         return self.a
# fib = fib(100)
# for each in fib:
#     print(each)


# string = range(5)
# i = iter(string)
# while True:
#     try:
#         each = next(i)
#     except StopIteration:
#         break
#     print(each)
    


# import datetime as t
# class LeapYear:

#     def __init__(self):
#         self.year = t.date.today().year
    
#     def isleapyear(self,year):
#         if ((self.year % 4 == 0 and self.year % 100 != 0)) or (self.year % 400 == 0):
#             return True
#         else:
#             return False


#     def __iter__(self):
#         return self

#     def __next__(self):
#         while not self.isleapyear(self.year):
#             self.year -= 1
#         temp = self.year 
#         self.year -= 1
#         return temp
        
    
# leapyear = LeapYear()
# for i in leapyear:
#     if i >= 2000:
#         print(i)
#     else:
#         break





# class MyRev:

#     def __init__(self,arg):
#         self.data = arg
#         self.list = []
#         for each in arg:
#             self.list.append(each)
#         self.len = len(self.list)
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.len == 0:
#             raise StopIteration
#         self.len -= 1
#         return self.list[self.len]

# MyRev =  MyRev('xiaoniu')
# for i in MyRev:
#     print(i,end = "")

        


        
