import random
print("请输入三个数字,前两个表示一个范围且,后一个表示中间隔多少")
print("\033[31m注意:此软件只适合10(最大)个随机数，但是程序会将大于10个数的列表剪切为10个数字\033[0m")
print("\033[32m提示:数与数之间用空格隔开\033[0m")
a, b, c = input().split(' ')
listname = []
alist = []
if a < b:
    for i in range(int(a), int(b), int(c)):
        listname.append(i)
    random.shuffle(listname)
    if len(listname) >= 10:
        for j in range(0, 10):
            alist.append(listname[j])
        print(alist)
    elif len(listname) < 10:
        for j in range(0, 10):
            alist.append(listname[j])
        print(alist)
else:
    print("\033[31m注意:后输入的数字一定比先输入的数字大\033[0m")
