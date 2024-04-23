import re

import pandas as pd

filename = 'student.txt'


# 定义菜单系统,使用户看到菜单
def menu():
    print('''╔———————————————学生信息管理系统——————————————————————╗
│                  注意事项
│   1.第一次执行程序请先录入学生信息,再执行下列命令
│   2.程序代码正在优化,依旧有小bug,请按照程序步骤进行操作               
│   =============== 功能菜单 ======================== 
│                                            
│   1 录入学生信息                             
│   2 查找学生信息                             
│   3 删除学生信息                             
│   4 修改学生信息    （暂未完成）                         
│   5 排序     （暂未完成）                              
│   6 统计学生总人数                           
│   7 显示所有学生信息                         
│   0 退出系统                                
│  ==================================================
│  说明：通过数字选择菜单功能                    
╚—————————————————————————————————————————————-——————╝''')


# 定义选择系统,定义数字对应的功能
def main():
    menu()  # 执行定义菜单
    flag = True
    while flag:  # 循环，以便再次选择功能
        # 输入数字选择需要使用的功能
        option = input('请输入菜单中的数字使用功能:')
        option_str = re.sub("\D", "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            # print('在范围内:')
            option_int = int(option_str)
            if option_int == 0:  # 退出系统/返回系统
                answer = input('\033[31m是否要退出系统(y/n):\033[0m')
                if answer in ['y', 'Y', 'yes', 'Yes']:
                    print('\033[32m已退出系统!!!\033[0m')
                    flag = False  # 退出系统
            elif option_int == 1:
                insert()  # 录入学生信息
            elif option_int == 2:
                search()  # 查找学生信息
            elif option_int == 3:
                delete()  # 删除学生信息
            elif option_int == 4:
                modify()  # 修改学生信息
            elif option_int == 5:
                sort()  # 排序
            elif option_int == 6:
                total()  # 统计所有学生信息
            elif option_int == 7:
                show()  # 显示所有学生信息
            else:
                print('\033[31m范围不存在\033[0m')
                # print('\033[31m输入0-7: \033[0m')
                main()
        else:
            print('\033[31m不在范围内,请重新输入\033[0m')
            main()


def insert():  # 录入学生信息
    list1 = []
    while True:  # 循环录入学生信息
        id = input('请输入ID(如1001):')
        if not id:  # ID为空
            print('\033[31m请输入正确的ID:\033[0m')
            continue  # 返回while循环重新输入

        name = input('请输入姓名:')
        if not name:  # name为空
            print('\033[31m请输入姓名:\033[0m')
            continue  # 返回while循环重新输入

        studentNumber = input('请输入学号:')
        if not studentNumber:  # studentNumber为空
            print('\033[31m请输入正确的studentNumber:\033[0m')
            continue  # 返回while循环重新输入

        # 录入成绩是否有误
        try:  # 成绩正常,录入并转为列表
            age = int(input('请输入年龄:'))
            tall = int(input('请输入身高(cm):'))
            weight = int(input('请输入体重(kg):'))
            chinese = int(input('请输入语文成绩:'))
            math = int(input('请输入数学成绩:'))
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩:'))
            total = chinese+math+english+python
            # 将ID name studentNumber age tall weight chinese math english python变量保存至字典students
            students = {"ID": id,
                        "name": name,
                        'studentNumber': studentNumber,
                        'age': age,
                        'tall': tall,
                        'weight': weight,
                        'chinese': chinese,
                        'math': math,
                        'english': english,
                        'python': python,
                        'total': total,
                        'avg': total/3
                        }
            # 字典保存成功，将字典添加至列表中
            list1.append(students)
        except:  # 成绩异常返回菜单
            print('\033[31m成绩数据有误,返回系统\033[0m')  # 提示用户成绩录入异常
            break  # 退出录入

        answer = input('是否添加下一个学生？(y/n):\n')  # 询问用户是否继续添加学生信息
        if answer == 'y' or answer == 'Y':
            continue  # 返回while循环,继续录入
        else:
            break  # 终止循环，执行下一行命令
    # 终止循环,保存学生信息
    save(list1)
    print('\033[36m学生信息录入完毕,返回菜单\033[0m')


# 定义save(保存)函数，将录入的学生信息保存至本地文件中(此代码将信息保存至 student.txt )
def save(listname):
    # 检测文件是否错在
    try:
        # 文件存在，追加写入
        f = open(filename, 'a', encoding='UTF-8')
    except:
        # 文件不存在，创建并写入
        f = open(filename, 'w', encoding="UTF-8")

    # 将列表中各元素依次保存
    for item in listname:
        f.write(str(item)+'\n')

    # 录入完成一定要记得关闭文件
    f.close()


# 定义search()(查询)函数
def search():
    # nlist=[]
    try:
        n = int(input('请输入数字进行查找(1.按姓名查找,2.按学号查找,3.按ID查找):'))
        if n not in [1, 2, 3]:
            print("\033[31m没有此查询规则,请重新输入\033[0m")
        else:
            # with open(filename, "r")as f:
            #     nlist = f.readlines()
            if n == 1:
                # print("\033[33m按学生姓名查找\033[0m")
                name = input('请输入要查询的学生姓名')
            elif n == 2:
                # print('\033[33m按学生学号查找\033[0m')
                studentNumber = input('请输入要查询的学生学号')
            elif n == 3:
                # print('\033[33m按学生ID查找\033[0m')
                id = input('请输入要查询的学生ID')
            else:
                print('您输入有误,请重新输入')
                search()
    except:
        print('\033[31m读取文件失败,请重试\033[0m')


def delete():
    # print('删除信息')
    a = int(input("1.删除所有学生信息，2.删除一个学生信息，3.删除单个学生的单个信息:"))
    if a == 1:
        pass
    elif a == 2:
        pass
    elif a == 3:
        pass
    else:
        print('\033[31m请选择功能!!!\033[0m')


def modify():
    pass


def sort():
    print('排序')


# 定义total()(总和)函数
def total():

    # 文件读取是否正常
    try:  # 读取正常,读取并展示学生信息
        with open(filename, 'r') as f:
            nlist = f.readlines()
            print('当前有'+str(len(nlist))+'个学生')
        f.close
    except:  # 读取失败,给用户返回错误原因
        print('打开文件出错')


# 定义show()(展示)函数
def show():
    # 文件读取是否正常
    scores = []
    names = ['a', 'b', 'b', 'd']
    courses = []

    try:  # 读取正常
        with open(filename, "r") as f:
            student_list = f.readlines()
            student_dict = {}
            for i in range(len(student_list)):
                student_list_i = student_list[i + 1].replace("\n", "")
                student_dict = eval(student_list_i)
            for j in student_dict:
                courses.append(j)
    except:  # 读取失败
        print('\033[31m打开文件错误,请检查文件位置是否正确\033[0m')
        main()
    pd.set_option('display.unicode.east_asian_width', True)
    df = pd.DataFrame(data=scores, columns=courses)
    print(df)


main()
