
# list1 = [1, [1, 2, [' 小甲鱼 ']], 3, 5, 8, 13, 18] 
# list1[1][2] = ["xiaoniu"]
# print(list1)


# list1 = [1, [1, 2, [' 小甲鱼 ']], 3, 5, 8, 13, 18] 
# list1 = [1,2,3,4,5,6,7,8,9]
# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)
# list2 = list1.copy()
# print(list2)
# list1.clear()
# print(list1)


list1 = [(x,y) for x in range(10) for y in range(10) if x %2 == 0 if y % 2 ==0]
print(list1)

list1 = []
for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            if y % 2 == 0:
                list1.append((x,y))
print(list1)


# list3 = [name + ' ：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]] 