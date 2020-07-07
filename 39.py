# class c:
#     num = 0
#     def __init__(self):
#         self.x = 4
#         self.y = 5
#         C.count = 6


# class C:
#     count = 0
#     def __init__(self):
#         C.count += 1
    
#     def __delattr__(self):
#         C.count -= 1

# a = C()
# b = C()
# c = C()
# print(C.count)


class Stack:
    def __init__(self,start = []):
        self.stack = []
        for x in start:
            self.push(x)
    
    def isEmpty(self):
        return not self.stack
    
    def push(self,obj):
        self.stack.append(obj)
    
    def pop(self):
        if not self.stack:
            print("栈为空！")
        else:
            return self.stack.pop()
    
    def top(self):
        if not self.stack:
            print("栈为空！")
        else:
            return self.stack[-1]
    
    def bottom(self):
        if not self.stack:
            print("栈为空！")
        else:
            return self.stack[0]