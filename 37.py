# class Ticket:
#     def __init__(self,child = False,weekend = False):
#         self.exp = 100
#         if child == True:
#             self.inc = 0.5
#         else:
#             self.inc = 1
#         if weekend == True:
#             self.discout = 1.2
#         else:
#             self.discout = 1
#     def calcPrice(self,num):
#         return self.exp * self.inc * self.discout * num


# adult = Ticket()
# child = Ticket(child = True)
# print("2个成人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))
        


import random as r

legal_x = [0, 10]
legal_y = [0, 10]

class Turtle:
    def __init__(self):
        self.power = 100

        self.x = r.randint(legal_x[0],legal_x[1])
        self.y = r.randint(legal_y[0],legal_y[1])
    
    def move(self):
        new_x = self.x + r.choice([1,2,-1,-2])
        new_y = self.y + r.choice([1,2,-1,-2])
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        if new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        if new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
    
        self.power -= 1
        return(self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100
class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
    
    def move(self):
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        if new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        if new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        return (self.x, self.y)
    
turtle = Turtle()
fish = []

for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼儿都吃完了，游戏结束！")
        break
    if not turtle.power:
        print("乌龟体力耗尽，挂掉了！")
        break
    pos = turtle.move()
    print("乌龟的位置：",pos)

    for each_fish in fish[:]:
        print("鱼的位置：" , each_fish.move())
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼儿被吃掉了......")
