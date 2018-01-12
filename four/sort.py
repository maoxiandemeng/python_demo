# sort排序算法
# sorted()函数就可以对list进行排序
# sorted(iterable, cmp=None, key=None, reverse=False)
# 把iterable中的items进行排序之后，返回一个新的列表，原来的iterable没有任何改变
# 1） iterable：iteralbe指的是能够一次返回它的一个成员的对象。iterable主要包括3类：
#     第一类是所有的序列类型，比如list(列表)、str(字符串)、tuple(元组)。
#     第二类是一些非序列类型，比如dict(字典)、file(文件)。
#     第三类是你定义的任何包含__iter__()或__getitem__()方法的类的对象。
# 2） cmp： 指定一个定制的比较函数，这个函数接收两个参数（iterable的元素），
#       如果第一个参数小于第二个参数，返回一个负数；如果第一个参数等于第二个参数，返回零；如果第一个参数大于第二个参数，返回一个正数。默认值为None。
# 3）key：指定一个接收一个参数的函数，这个函数用于从每个元素中提取一个用于比较的关键字。默认值为None。
# 4）reverse：是一个布尔值。如果设置为True，列表元素将被降序排列，默认为升序排列。
#          通常来说，key和reverse比一个等价的cmp函数处理速度要快。这是因为对于每个列表元素，cmp都会被调用多次，而key和reverse只被调用一次。
from operator import itemgetter


def my_abs(n):
    if n <= 0:
        return -n
    else:
        return n


L = [1, 4, 65, -12, 8, 9, 3, -6]
print(sorted(L))
print(sorted(L, reverse=True))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted(L, key=my_abs))

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，
# 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
L2 = ['A', 'a', 'gf', 'ui', 'We']
print(sorted(L2))

L3 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(n):
    return n[0]


print(sorted(L3, key=lambda name: name[0]))
print(sorted(L3, key=itemgetter(1)))







