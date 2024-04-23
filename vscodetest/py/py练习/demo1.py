import random

# 生成随机数
num = random.randint(1, 50)

# 猜的次数
count = 0

# 最多猜的次数
max_count = 3

# 是否猜中
is_win = False

# 循环猜数字
while count < max_count:
    guess = int(input("请猜一个1到50之间的整数："))
    count += 1
    if guess == num:
        print("恭喜你，猜中了！")
        is_win = True
        break
    else:
        print("猜错了，加油！")
        if guess < num:
            print("再猜的数字要大一些哦！")
        else:
            print("再猜的数字要小一些哦！")

# 如果没有猜中，输出正确答案
if not is_win:
    print("很遗憾，你没有猜中，正确答案是：", num)
