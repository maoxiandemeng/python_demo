# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回
# 通过list()函数让它把整个序列都计算出来并返回一个list


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4])
print(list(r))




