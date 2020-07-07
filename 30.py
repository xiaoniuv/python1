# import os

# print(os.curdir)
# all_files = os.listdir(os.curdir)
# print(all_files)
# type_dict = dict()

# for each_file in all_files:
#     if os.path.isdir(each_file):
#         type_dict.setdefault("文件夹",0)
#         type_dict['文件夹'] += 1
#     else:
#         ext = os.path.splitext(each_file)[1]
#         type_dict.setdefault(ext,0)
#         type_dict[ext] += 1
# for each_type in type_dict.keys():
#     print("该文件夹下共有类型为【%s】文件 %d 个" %(each_type,type_dict[each_type]))

# import os

# all_files = os.listdir(os.curdir)
# size_dict = dict()

# for each_file in all_files:
#     if os.path.isfile(each_file):
#         file_size = os.path.getsize(each_file)
#         size_dict[each_file] = file_size
# for each in size_dict.items():
#     print("%s【%dBytes】" % (each[0],each[1]))
# print(size_dict)



# import os

# def search_file(start_dir,target):
#     os.chdir(start_dir)

#     for each_file in os.listdir(os.curdir):
#         if each_file == target:
#             print(os.getcwd() + os.sep + each_file)
#         if os.path.isdir(each_file):
#             search_file(each_file,target)
#             os.chdir(os.pardir)

# start_dir = input("请输入需要查找的初始目录：")
# target = input("请输入需要查找的目标文件：")
# search_file(start_dir,target)



# import os
# def search_file(start_dir,target):
#     os.chdir(start_dir)

#     for each_file in os.listdir(os.curdir):
#         ext = os.path.splitext(each_file)[1]
#         if ext in target:
#             vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
#         if os.path.isdir(each_file):
#             search_file(each_file,target)
#             os.chdir(os.pardir)

# start_dir = input("请输入待查找的初始目录:")
# program_dir = os.getcwd()

# target = [".mp4",".avi",".rmvb"]
# vedio_list = []

# search_file(start_dir,target)

# f = open(program_dir + os.sep + "vediolist.txt","w")
# f.writelines(vedio_list)
# f.close()


import os

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys)
    for each_key in keys:
        print("关键字出现在第 %s 行，第 %s 个位置。" % (each_key,str(key_dict[each_key])))


def pos_in_line(line,key):
    pos = []
    begin =  line.find(key)
    while begin != -1:
        pos.append(begin + 1)
        begin = line.find(key,begin + 1)
    
    return pos

def search_in_file(file_name,key):
    f = open(file_name)
    count = 0
    key_dict = dict()

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line,key)
            key_dict[count] = pos
    
    f.close()
    return key_dict

def search_files(key,detail):
    all_files = os.walk(os.getcwd())
    print(all_files)
    txt_files = []

    for i in all_files:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == ".txt":
                each_file = os.path.join(i[0],each_file)
                txt_files.append(each_file)
    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file,key)
        if key_dict:
            print("========================================")
            print("在文件【%s】中找到关键字【%s】" % (each_txt_file,key))
            if detail in ["yes","YES","Yes"]:
                print_pos(key_dict)

key = input("请将该脚本放于带查找的文件夹内，请输入关键字：")
detail = input("请问是否需要打印关键字【%s】在文件中的具体位置（yes/no):" % key)
search_files(key,detail)
