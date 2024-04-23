import time


a = "abcdefghijklmabcdiehjkecbnk"
b = "nopqrstuvwxyznopwstvzxypqtywr"
c = "198264818902901286478372547538923837843454743"
d = input("随便输入字母、数字,系统将在系统存储的列表中进行查重!!!:")

lista = list(a)
listb = list(b)
listc = list(c)
print("\033[31m系统将进行对系统自身列表查重,请稍后!!!\033[0m")

time.sleep(1)

print("提示:a1、b1为字母查重,c1为数字查重")

time.sleep(1)

# 字符串a自身去重
lista1 = []
for i in lista:
    if i not in lista1:
        lista1.append(i)
    else:
        pass
print("\033[31m已对系统列表a1进行查重,请稍后\033[0m")

time.sleep(1)

# 字符串b自身去重
listb1 = []
for i in listb:
    if i not in listb1:
        listb1.append(i)
    else:
        pass
print("\033[31m已对系统列表b1进行查重,请稍后\033[0m")

time.sleep(1)

# 字符串c自身去重
listc1 = []
for i in listc:
    if i not in listc1:
        listc1.append(i)
    else:
        pass
print("\033[31m已对系统列表c1进行查重,请稍后\033[0m")

time.sleep(1)

# 将d列表与系统列表查重
if d != "":
    listd = list(d)
    for i in listd:
        if i not in lista1:
            print("\033[32m输入字符串与系统列表a1无重复\033[0m", end="              ")
        else:
            print("\033[32m输入字符串与系统列表a1有重复,重复的是:\033[0m" + i, end="   ")
        if i not in listb1:
            print("\033[33m输入字符串与系统列表b1无重复\033[0m", end="              ")
        else:
            print("\033[33m输入字符串与系统列表b1有重复,重复的是:\033[0m" + i, end="   ")
        if i not in listc1:
            print("\033[34m输入字符串与系统列表c1无重复\033[0m", end="\n")
        else:
            print("\033[34m输入字符串与系统列表c1有重复,重复的是:\033[0m" + i, end="\n")
        time.sleep(0.1)
else:
    print("\033[31m您输入为空,无法进行查重处理\033[0m")
    time.sleep(0.3)
input("请按Enter退出")
