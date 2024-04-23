# 主函数设计----menu()
'''
0----退出系统
1----录入学生信息，调用insert()函数
2----查找学生信息，调用search()函数
3----删除学生信息，调用delete()函数
4----修改学生信息，调用modify()函数
5----对学生成绩排序，调用sort()函数
6----统计学生总人数，调用total()函数
7----显示所有学生信息，调用show()函数
'''

import os # 导入os模块
filename='students.txt' # 定义一个变量名称叫做'students.txt',为之后创建的文件夹的名称
def main(): # 主函数
   while True: # 加入循环，以便能够回到重新选择
       menu() # 调用menu()函数，开始显示主菜单
       choice=int(input('请选择使用的功能(输数字即可)：')) # 转为int类型 并且做出选择功能
       if choice in [0,1,2,3,4,5,6,7]:
           if choice==0: # 选择的是退出系统，即选择为0
               answer=input('您确定要退出系统吗？y/n')
               if answer=='y' or answer=='Y':
                   print('谢谢您的使用！！！')
                   break # 退出系统
               else: # 选择的不是'y'或'Y'
                   continue
           elif choice==1:
               insert() # 录入学生信息函数
           elif choice==2:
               search() # 查找学生信息函数
           elif choice==3:
               delect() # 删除学生信息函数
           elif choice==4:
               modify() # 修改学生信息函数
           elif choice==5:
               sort() # 对学生成绩排序函数
           elif choice==6:
               total() # 统计学生总人数函数
           elif choice==7:
               show() # 显示所有学生信息函数


def menu(): # 菜单函数
   print('=========================学生信息管理系统=========================')
   print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~注意事项~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   print('1.刚开始运行程序时，由于没有录入学生信息，请先执行”录入学生信息操作“')
   print('2.程序对部分代码已经进行优化，但仍有微小可能出现bug，请尽量按照程序要求输入')
   print('----------------------------功能菜单----------------------------')
   print('\t\t\t\t1.录入学生信息')
   print('\t\t\t\t2.查找学生信息')
   print('\t\t\t\t3.删除学生信息')
   print('\t\t\t\t4.修改学生信息')
   print('\t\t\t\t5.对学生成绩排序')
   print('\t\t\t\t6.统计学生总人数')
   print('\t\t\t\t7.显示所有学生信息')
   print('\t\t\t\t0.退出系统')
   print('---------------------------------------------------------------')


def insert(): # 录入学生信息功能(从控制台录入学生信息，并且把它们保存到磁盘文件中)
   student_list=[] # 用于存储录入的学生 此处的student_list是列表
   while True: # 循环去录入学生信息
       # 防止出现id，姓名为空的情况(恶意输入错误)
       id=input('请输入id(如1001、1002)：')
       if not id: # id为空时
           break
       name=input('请输入姓名：')
       if not name: # 姓名为空字符串时
           break
       # 防止出现成绩异常
       try:
           english=int(input('请输入英语成绩：'))
           python=int(input('请输入Python成绩：'))
           java=int(input('请输入Java成绩：'))
       except:
           print('输入无效，不是整数类型，请重新输入')
           continue # 若输入无效，则会跳转到while True处
       # 输入没有问题，将信息保存到字典当中 此处的student是字典
       student={'id':id,'name':name,'english':english,'python':python,'java':java}
       # 将学生信息添加到列表之中
       student_list.append(student)
       answer=input('是否继续添加下一个学生？y/n\n')
       if answer=='y':
           continue # 回到while True处，开始新一轮的循环
       else:
           break

   # 跳出while循环后，调用save()函数，用于存储学生信息
   save(student_list) # 新函数，在insert()函数外部定义
   print('学生信息录入完毕！！！')


def save(lst): # 定义save()函数 在其中传入的是列表 其用于传入学生信息到文件当中
   try:
       stu_txt=open(filename,'a',encoding='utf-8') # 以追加模式打开,同时防止出现中文乱码(此处无法创建文件)
   except: # 运行文件夹中如果不存在该文件 filename=='students.txt' 则可能报错
       # 出现异常的处理方式：
       stu_txt=open(filename,'w',encoding='utf-8') # 以写入模式打开，会创建一个该文件
   for item in lst: # 遍历lst中的所有数据
       stu_txt.write(str(item)+'\n') # 将列表内容转为str类型
   stu_txt.close() # 将打开的文件进行关闭


def search(): # 查找学生信息(查询磁盘文件中，某个输入的学生所对应的信息)
   student_query=[] # 定义一个列表用于存放学生信息
   while True:
       id=''
       name=''
       if os.path.exists(filename): # 判断磁盘文件是否存在
           mode=input('按id查找请输入1，按姓名查找请输入2：') # 区分按什么方式进行查找
           if mode=='1': # 输入的类型是字符串类型，此处1需要加单引号
               id=input('请输入要查询的学生的id：') # 模式为id查找的情况
           elif mode=='2':
               name=input('请输入要查询的学生的姓名：') # 模式为姓名查找的情况
           else:
               print('您的输入有误，请重新输入')
               search() # 重新运行search()函数
           with open(filename,'r',encoding='utf-8') as rfile: # 读取磁盘上的文件
               student=rfile.readlines()
               for item in student:
                   d=dict(eval(item)) # 字符串转为字典类型 d为磁盘文件中所有学生信息的字典
                   if id!='':
                       if d['id']==id: # d字典中的id和输入中的id进行对比
                           student_query.append() # 将查找到的学生添加到student_query这个列表当中
                   elif name!='':
                       if d['name']==name: # d字典中的name和输入中的name进行对比
                           student_query.append()
           # 显示查询结果：
           show_studnet(student_query) # 新函数，在search()函数外部定义
           # 清空列表
           student_query.clear()
           answer=input('是否要继续查询？y/n\n')
           if answer=='y':
               continue
           else:
               break # 结束查询功能
       else:
           print('暂未保存录入学生信息')
           return


def show_studnet(lst): # 显示学生信息函数
   if len(lst)==0:
       print('没有查询到学生信息，无数据显示')
       return
   # 定义标题的显示格式
   ''' ^12 为居中对齐，后面的数字为总的字符数'''
   format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}' # 分别是 id 姓名 英语成绩 Python成绩 Java成绩 总成绩
   print(format_title.format('id','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
   # 定义内容的显示格式
   format_date='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
   for item in lst: # 由于不知道有多少个对象，需要使用遍历
       print(format_date.format(item.get('id')+\
           item.get('name'),item.get('english'),item.get('python')+\
               item.get('java'),int(item.get('english'))+int(item.get('python'))+int(item.get('java'))))


def delect(): # 删除学生信息功能(在磁盘中找到对应学生的信息，并进行删除)
   while True:
       student_id=input('请输入要删除的学生的id：')
       if student_id!='':
           if os.path.exists(filename): # 判断文件是否存在
               with open(filename,'r',encoding='utf-8') as file:
                   student_old=file.readlines() # 读取文件中的所有信息，并放到一个列表当中
           else: # 文件不存在的情况下
               student_old=[] # 定义列表为空即可
           # Flag用于标记是否删除(默认没有删除)
           flag=False # 表示没有删除
           if student_old: # 空列表的布尔值为False；如果为True，则说明其中有内容
               with open(filename,'w',encoding='utf-8') as wfile:
                   d={} # 创建一个字典，用于去存储文件中的学生对象信息
                   for item in student_old:
                       d=dict(eval(item)) # 将字符串去转成字典
                       if d['id']!=student_id: #如果要删除的学生的id和字典中的学生id不相同的话
                           wfile.write(str(d)+'\n')
                       else:
                           flag=True # 表示删除
                   if flag:
                       print(f'id为{student_id}的学生的信息已被删除')
                   else:
                       print(f'没有找到id为{student_id}的学生')
           else: # 从磁盘上没有读到数据(没有数据的情况)
               print('无学生信息')
               break
           show() # 删除之后将重新显示所有学生信息
           answer=input('是否继续删除？y/n\n')
           if answer=='y':
               continue
           else:
               break


def modify(): # 修改学生信息功能(找到已有学生信息，并进行修改)
   show()
   if os.path.exists(filename): # 判断文件是否存在
       with open(filename,'r',encoding='utf-8') as rfile:
           student_old=rfile.readlines()
   else:
       return # 结束修改操作
   student_id=input('请输入要修改的学员的id：')
   with open(filename,'w',encoding='utf-8') as wfile:
       for item in student_old: # 遍历读取到的学生信息
           d=dict(eval(item)) # 将字符串转为字典类型
           if d['id']==student_id:
               print('找到学生信息，可以修改ta的相关信息！')
               while True:
                   try:
                       d['name'] = input('请输入新的姓名：')
                       d['english'] = int(input('请输入新的英语成绩：'))
                       d['python'] = int(input('请输入新的Python成绩：'))
                       d['java'] = int(input('请输入新的Java成绩：'))
                   except:
                       print('您的输入有误，请重新输入！！！') # 会返回到while True处
                   else:
                       break # 退出循环结构(退出修改学生信息功能)
               wfile.write(str(d)+'\n') # 输入没有错误，则进行转入到文件中去
               print('修改成功！！！')
           else:
               wfile.write(str(d)+'\n') # 将无需修改的也原封不动地写进去
       answer=input('是否继续修改其他学生信息？y/n\n')
       if answer=='y':
           modify() # 即继续运行程序，进行修改其他学生的信息


def sort(): # 对学生成绩排序功能
   show() # 显示全部学员信息
   if os.path.exists(filename): # 文件在磁盘上存在
       with open(filename,'r',encoding='utf-8') as rfile:
           student_list=rfile.readlines()
       student_new=[]
       for item in student_list:
           d=dict(eval(item))
           student_new.append(d)
   else: # 文件在磁盘上不存在
       return
   # 排序方式选择
   asc_or_desc=input('请选择排序类型(0表示升序，1表示降序)：\n')
   if asc_or_desc=='0': # 升序
       asc_or_desc_bool=True
   elif asc_or_desc=='1': # 降序
       asc_or_desc_bool=False
   else:
       print('您的输入有误，请重新输入')
       sort()
   mode=input('请选择排序方式(1.按英语成绩排序；2.按Python成绩排序；3.按Java成绩排序；0.按总成绩排序)(输数字即可)：')
   if mode=='1':
       student_new.sort(key=lambda x :int(student_new['english']),reverse=asc_or_desc_bool) # 匿名函数
       ''' 上行代码相当于：x是一个参数，这个参数是一个字典，在student_new中根据键'english'去获取值，并进行一个int类型转换，最后将结果赋给key '''
   elif mode=='2':
       student_new.sort(key=lambda x :int(student_new['python']),reverse=asc_or_desc_bool)
   elif mode=='3':
       student_new.sort(key=lambda x :int(student_new['java']),reverse=asc_or_desc_bool)
   elif mode=='0':
       student_new.sort(key=lambda x :int(student_new['english'])+int(student_new['python'])+int(student_new['java']),reverse=asc_or_desc_bool)
   else:
       print('您的输入有误，请重新输入')
       sort()
   show_studnet(student_new)


def total(): # 统计学生总人数(输出磁盘上文件中学生信息的总人数)
   if os.path.exists(filename): # 判断文件是否存在
       with open(filename,'r',encoding='utf-8') as rfile:
           students=rfile.readlines() # 读取文件信息并放在列表students中
           if students: # 如果students不为空列表
               print(f'一共有{len(students)}名学生') # 列表中元素的个数
           else: # students列表为空列表，证明还没有录入学生信息
               print('暂未录入学生信息！！！')
   else: # 文件不存在
       print('暂未保存数据......')


def show(): # 显示所有学生信息功能(将学生信息文件中保存的全部学生信息获取并显示)
   student_list=[] # 用于存储学员信息
   if os.path.exists(filename): # 文件存在的情况
       with open(filename,'r',encoding='utf-8') as rfile:
           students=rfile.readlines()
           for item in students: # 遍历读取到信息的列表
               student_list.append(eval(item))
           if student_list: # 如果这个列表不为空
               show_studnet(student_list) # 上面163行定义的函数，用于输出学生信息
   else:
       print('暂未保存过数据！！！')


if __name__ == '__main__': # 以主程序方式去运行
   main()