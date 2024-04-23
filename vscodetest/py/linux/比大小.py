'''
try:
    num1 = int(input("请输入第一个数："))
    num2 = int(input("请输入第二个数："))

    if num1 > num2:
        print("第一个数大于第二个数")
    elif num1 < num2:
        print("第一个数小于第二个数")
    else:
        print("两个数相等")
except:
    print('你输入的不是整数')
'''

'''
try:
    num1 = int(input("请输入第一个数："))
    num2 = int(input("请输入第二个数："))

    print("第一个数大于第二个数" if num1 > num2 else "第一个数小于第二个数" if num1 < num2 else "两个数相等")
except:
    print('你输入的不是整数')
'''

a = eval(input('请输入一个整数:'))
b = eval(input('请输入另一个整数:'))
if isinstance(a, int) == True and isinstance(b, int) == True:
    print('第一个数大于第二个数' if a > b else '第一个数小于第二个数' if a < b else '两个数相等')
else:
    print('您输入的不是整数')
