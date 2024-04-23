names = []
sizes = []
prices = []
n = int(input("请输入n(n>=2)"))
for i in range(n):
    name, size, price = input().split(' ')
    names.append(name)
    sizes.append(int(size))
    prices.append(int(price))
print(names, sizes, prices, round(sum(prices)/len(prices), 2), sep='\n')
