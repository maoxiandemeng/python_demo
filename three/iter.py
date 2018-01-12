# 迭代
# 给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们称为迭代（Iteration）

# 迭代器
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。


from collections import Iterable

d = {1: "123", "a": "asd", 2: 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key)
    print(value)

# 字符串也是可迭代对象，因此，也可以作用于for循环
for ch in "asdfghj":
    print(ch)

# 判断一个对象是可迭代对象,方法是通过collections模块的Iterable类型判断
print(isinstance('123', Iterable))
print(isinstance(d, Iterable))
print(isinstance(1, Iterable))

# enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


def findMinAndMax(l):
    if l is None:
        return ()
    if not l:
        return ()
    minL = l[0]
    maxL = l[0]
    for v in l:
        if v < minL:
            minL = v
        if v > maxL:
            maxL = v
    return minL, maxL


list_find = [1, 4, 6, 5, 8, 2, 3]
find = findMinAndMax([])
print(find)
