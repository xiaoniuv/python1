# def file_write(filename):
#     with open(filename,"x") as f:
#         print("请输入内容【单独输入\':w\'保存退出】:")
        
#         while True:
#             write_some = input()
#             if write_some != ":w":
#                 f.write("%s\n" % write_some)
#             else:
#                 break
#     f.close()

# filename = input("请输入文件名：")
# file_write(filename)



# def file_contract(filename1,filename2):
#     f1 = open(filename1,"r")
#     f2 = open(filename2,"r")
#     count = 0
#     differ = []

#     for line1 in f1:
#         line2 = f2.readline()
#         count += 1
#         if line1 != line2:
#             differ.append(count)
    
#     f1.close()
#     f2.close()
#     number = len(differ)
#     print("两个文件共有【%d】处不同：\n" % number)
#     for each in differ:
#         print("第 %d 行不一样\n" % each)
        
# filename1 = input("请输入需要比较的头一个文件名：")
# filename2 = input("请输入需要比较的另一个文件名：")
# file_contract(filename1,filename2)



# def file_print(filename,read_line):
#     count = 0
#     f = open(filename,"r")
#     print("文件 %s 的前 %s 行内容如下：" % (filename,read_line))
#     for each in range(int(read_line)):
#         print(f.readline(),"\n")
#     f.close()


# filename = input("请输入需要打开的文件(C:\\something.txt):")
# read_line = input("请输入需要显示该文件的前几行：")
# file_print(filename,read_line)



# def file_view(filename,line_num):
#     if line_num.strip(":"):
#         begin = '1'
#         end = '-1'
#     (begin,end) = line_num.split(":")
#     if begin == '':
#         begin = "1"
#     if end == "":
#         end = "-1"

#     if begin == '1' and end == '-1':
#         prompt = "的全文"
#     elif begin == "1":
#         prompt = "从开始到%s" % end
#     elif end == "-1":
#         prompt = "从%s开始到结束" % begin
#     else:
#         prompt = "从%s行到%s行" %(begin,end)
    
#     print("\n文件%s%s的内容如下：\n" % (filename,prompt))

#     begin = int(begin) - 1
#     end = int(end)
#     lines = end - begin

#     f = open(filename)
#     for i in range(begin):
#         f.readline()
    
#     if lines < 0:
#         print(f.read())
#     else:
#         for j in range(lines):
#             print(f.readline())
    
#     f.close()


# filename = input("请输入需要打开的文件(C:\\something.txt):")
# line_num = input("请输入需要显示该文件的行数【格式如 13:21 或 :21 或21：】：")
# file_view(filename,line_num)



def file_replace(filename,rep_word,new_word):
    f_read = open(filename,"r")

    content = []
    count = 0

    for each_line in f_read:
        if rep_word in each_line:
            count = each_line.count(rep_word)
            each_line = each_line.replace(rep_word,new_word)
        content.append(each_line)
    f_read.close()
    decide = input("\n文件 %s 中共有 %s 个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：\n" %(filename,count, rep_word,rep_word,new_word))

    if decide in ["yes","YES","Yes"]:
        f_write = open(filename,"w")
        f_write.writelines(content)
        f_write.close()

filename = "something.txt"
rep_word = "我"
new_word= "你"
file_replace(filename,rep_word,new_word)