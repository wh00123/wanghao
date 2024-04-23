import time

# 格式化成2016-03-20 11:45:39形式
while True:
    time.sleep(0.1)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
input()
