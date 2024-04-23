import pd

fn = 'student.txt'

col = ['学号', '姓名', '语文成绩', '数学成绩', '英语成绩', 'python成绩']

dict1 = []

try:
    with open(fn, 'r') as f:
        for i in f:
            j = i.replace('\n', '')
            print(j, end='\n')
            dict1.append(j)
except:
    print('文件操作错误,请稍后重试!')


pd.set_option('display.unicode.east_asian_width', True)
# 输出位置对齐
df = pd.DataFrame(data=dict1, columns=col)
print(df)
