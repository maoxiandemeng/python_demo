# 列表生成式:非常简单却强大的可以用来创建list的生成式

import os


l1 = []
for x in range(1, 11):
    l1.append(x * x)
print(l1)

print([x*x for x in range(1, 11)])
# 筛选出仅偶数的平方
print([x*x for x in range(1, 11) if x % 2 == 0])
# 可以使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 返回当前目录
print([d for d in os.listdir('.')])
# 改变工作目录
print([d for d in os.listdir("F:\\")])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + "=" + v for k, v in d.items()])

# 使用内建的isinstance函数可以判断一个变量是不是字符串：
x = "123"
y = 123
print(isinstance(x, str))
print(isinstance(y, str))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [v for v in L1 if isinstance(v, str)]
print(L2)

