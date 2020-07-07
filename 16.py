print("{{1}}".format("打印","不打印"))

print('{0}{1:.2f}'.format('Pi = ', 3.1415)) 


q = True
while q:
    number = input("输入一个数（若想退出，输出Q即可）：")
    if number == ("q" or "Q"):
        q = False
    else:
        num = int(number)
        print("十进制 -> 十六进制: %d -> 0x%x" %(num,num)  )
        print("十进制 -> 八进制:   %d -> 0o%o" %(num,num))
        print("十进制 -> 二进制:   %d -> " % num,bin(num))