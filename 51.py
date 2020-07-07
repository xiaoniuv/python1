# import sys

# print(sys.path)



# def func():
#     pass
# print(type(func()))


# print(type(1J))

# print(type(lambda:None)) 

# class A:
#     def __init__(self,x):
#         x = x + 1
#         self.v1 = x

# class B(A):
#     def __init__(self,x):
#         x = x + 1
#         self.v2 = x

# b = B(8)
# print("%d" % (b.v2))



# values = [1,1,2,3,5]
# nums = set(values)

# def checkit(num):
#     if num in nums:
#         return True
#     else:
#         return False

# for i  in filter(checkit,values):
#     print(i,end = "")



# class A:
#     def __init__(self):
#         pass
#     def get(self):
#         print(__name__)

# a = A()
# print(a.get())



# dict1 = {}
# dict1[1] = 1
# dict1['1'] = 2
# dict1[1.0] = 3

# result = 0
# for each in dict1:
#     result += dict1[each]
# print(dict1)


# def dostuff(param1,*param2):
#     print(type(param2))

# dostuff('apples','banans','cherry','dates')

# def dostuff(*param2):
#     print(type(param2))
# dostuff('apples','banans','cherry','dates')

# import copy

# list1 = [1,2]
# list2 = [3,4]

# dict1 = {'1':list1,'2':list2}

# dict2 = dict1.copy()
# dict3 = copy.deepcopy(dict1)

# dict1['1'][0] = 5
# result = dict1['1'][0] + dict2['1'][0]
# result1 = dict1['1'][0] + dict3['1'][0]
# print(dict2,dict3)
# print(result,result1)