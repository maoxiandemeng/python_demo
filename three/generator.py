# 生成器
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器

# 第一种方法很简单，只要把一个列表生成式的[]改成()
L = [x * x for x in range(1, 11)]
print(L)
G = (x * x for x in range(1, 11))
# 通过next()函数获得generator的下一个返回值
print(next(G))
for n in G:
    print(n)


def fib(max1):
    n1, a, b = 0, 0, 1
    while n1 < max1:
        yield b
        a, b = b, a + b
        n1 = n1 + 1
    return 'done'


for v in fib(1):
    print(v)


def triangles(max2):
    L2 = [1]
    n2 = 0
    while n2 < max2:
        yield L2
        # 先把头尾1去掉生产一个集合
        L2 = [L2[i] + L2[i+1] for i in range(0, len(L2) - 1)]
        L2.insert(0, 1)
        L2.append(1)
        n2 = n2 + 1
    return L2


for v in triangles(4):
    print(v)


