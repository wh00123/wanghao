import re

def menu():
    print('''╔———————————————学生信息管理系统————————————————╗
│                                            
│   =============== 功能菜单 ===============  
│                                            
│   1 录入学生信息                             
│   2 查找学生信息                             
│   3 删除学生信息                             
│   4 修改学生信息                             
│   5 排序                                   
│   6 统计学生总人数                           
│   7 显示所有学生信息                         
│   0 退出系统                                
│  =========================================
│  说明：通过数字选择菜单功能                    
╚———————————————————————————————————————————╝''')


def main():
    flag=True
    menu()
    while flag:
        option=input('请输入一个数字来选择对应的功能:')
        option_str=re.sub("\D","",option)
        if option_str in ["0","1","2","3","4","5","6","7"]:
            option_int=int(option_str)
            print(option_str)
            print(option_int)
            print(type(option_int),type(option_str))
            if option_int == 0:
                print('\033[32m系统已退出!\033[0m')
                flag=False

        else:
            print("\033[31m不存在此功能,请重新选择!\033[0m")
            main()
    
        


main()