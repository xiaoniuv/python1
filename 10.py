# member = [1, "小甲鱼",3.14,[1,2,3]]
# member.append(['lalal',"wo shi xiao niu"])
# member.extend(['lalal',"wo shi xiao niu"])
# member.insert(2,"xiaoniu")
# print(member)


# member = [' 小甲鱼 ', ' 黑夜', ' 迷途', ' 怡静', ' 秋舞斜阳 '] 
# member.insert(1,88)
# print(member)


# member = [' 小甲鱼 ', 88, ' 黑夜 ', 90, ' 迷途 ', 85, ' 怡静 ', 90, ' 秋舞斜阳 ', 88] 
# length = len(member)
# for each in range(length):
#     if each % 2 == 0:
#         print(member[each],member[each + 1])

member = [' 小甲鱼 ', 88, ' 黑夜 ', 90, ' 迷途 ', 85, ' 怡静 ', 90, ' 秋舞斜阳 ', 88] 
new = member
old = member.copy()
member = [6]
print(new)
print(member)
print(old)