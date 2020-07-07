# class CountList:
#     def __init__(self,*arg):
#         self.value = [x for x in arg]
#         self.count = {}.fromkeys(range(len(arg)),0)
#     def __len__(self):
#         return len(self.value)
#     def __getitem__(self,key):
#         self.count[key] += 1
#         return self.count[key]

# c1 = CountList(1,2,3,4,5,6)
# c2 = CountList(7,8,9,10)

# c1[1]
# c1[2]
# c1[3]
# print(c1.count)




class CountList(list):

    def __init__(self,*arg):
        super.__init__(arg)
        self.count = []
        for x in arg:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self,key):
        self.count[key] += 1
        return super.__getitem__(key)
    
    def __setitem__(self, key, value):
        self.count[key] += 1
        return super().__setitem__(key, value)
    
    def __delitem__(self, key):
        del self.count[key]
        return super().__delitem__(key)
    
    def counter(self, key):
        return self.count

    def append(self, object):
        self.count.append(0)
        return super().append(object)
    
    def pop(self, key):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        super().remove(value)
    
    def clear(self):
        self.count.clear()
        return super().clear()
    
    def reverse(self):
        self.count.reverse()
        return super().reverse()




