
# a = {"F":70,"C":67,"h":104,"i":105,"s":115}
# print(a["C"])
# b = dict((("f",70),("i",105),("s",115),("h",104),("c",67)))
# print(b["c"])


# brand = ["李宁","耐克","阿迪达斯","鱼C工作室"]
# slogan = ["一切皆有可能","Just do it","Impossible is nothing","让编程改变世界"]
# print("鱼C工作室的口号是：",slogan[brand.index("鱼C工作室")])


# a = dict(one = 1, two = 2, three = 3)
# print(a)
# b = {"one":1,"two":2,"three":3}
# print(b)
# c = dict(zip(["one","two","three"],[1,2,3]))
# print(c)
# d = dict([("one",1),("two",2),("three",3)])
# print(d)
# e = dict({"one":1,"two":2,"three":3})
# print(e)



def contact():
    print("|---------欢迎进入通讯录程序---------|")
    print("|---------1：查询联系人资料----------|")
    print("|---------2：插入新的联系人----------|")
    print("|---------3：删除已有联系人----------|")
    print("|---------4：退出通讯录程序----------|")
    
    contacts = dict()
    while True:
        instr = int(input("请输入相关的指令代码："))

        if instr == 1:
            name = input("请输入联系人姓名：")
            if name not in  contacts:
                if input("联系人不存在，是否添加【yes/no】") == "yes":
                    contacts[name] = input("请输入用户联系电话：")
            else:
                print(name + ":" + contacts[name])
        
        if instr == 2:
            name = input("请输入联系人姓名：")
            if name in contacts:
                print("联系人已存在 ->>",end ="")
                print(contacts + ":" + contacts[name])
                if input("是否修改【yes/no】") == "yes":
                    contacts[name] = input("请输入用户联系电话：")
            else:
                contacts[name] = input("请输入用户联系电话：")
        
        if instr == 3:
            name = input("请输入联系人姓名：")
            if name in contacts:
                del(contacts[name])
            else:
                print("您输入的联系人不存在")    
        
        if instr == 4:
            break
    print("|-----------感谢使用通讯录程序---------|")


if __name__ == "__main__":
    contact()



