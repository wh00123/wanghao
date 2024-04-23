# 自定义函数
# 练习，自定义函数，名字自拟
'''
功能：
1.输入两个参数
2.计算两个参数的差
3.输出两个数的差
'''

'''
def sub_():
    a = int(input('输入数字1：'))
    b = int(input("输入数字2："))
    c = a - b
    print('两数之差为:',c)

sub_()
'''


def say_hi(**name):
    for i in range(1, int(len(name)+1)):
        a = str('name')+str(i)
        print("{},你好".format(name[a]))


say_hi(
    name1='王',
    name2='胡',
    name3='宋',
    name4='黄'
)
