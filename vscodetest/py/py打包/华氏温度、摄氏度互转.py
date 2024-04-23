while True:
    n = int(input("请选择1.华氏温度转摄氏度,2摄氏度转华氏温度"))
    if n == 1:
        huashi = float(input("请输入需转换的华氏温度:"))
        sheshi = ((huashi-32)/1.8)
        print("摄氏度为："+str(sheshi))

    if n == 2:
        sheshi = float(input("请输入需转换的摄氏度:"))
        huashi = (sheshi * 1.8)+32
        print(huashi)

    message = input("请问是否需要继续转换?Y(是)/N(否)")
    if message in ["y", 'Y', 'yes']:
        continue
    elif message in ['N', 'n', 'no']:
        break
    else:
        print("\033[31m我不懂你想要干什么!\033[0m")
