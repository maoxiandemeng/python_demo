# 返回函数:函数作为返回值
def test_sum(*args):
    a = 0
    for i2 in args:
        a = a + i2
    return a


def l_sum(*args):
    def sum1():
        a = 0
        for i1 in args:
            a = a + i1
        return a
    return sum1


f = l_sum(1, 2, 3, 4, 5)
# 求和函数
print(f)
# 求和
print(f())
print('===================')


def count():
    def f1(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        # def f1():
        #     return i*i
        # f(i)立刻被执行，因此i的当前值被传入f()
        fs.append(f1(i))
    return fs


c1, c2, c3 = count()
print(c1(), c2(), c3())
print(c2())
print(c3())
print('===================')


def createCounter():
    def counter(j):
        def c():
            return j
        return c
    i = 1
    fs = []
    while True:
        fs.append(counter(i))
        i = i+1
    return fs


f1, f2, f3, f4 = createCounter()
print(f1(), f2(), f3(), f4())




