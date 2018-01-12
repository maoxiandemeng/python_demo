# 切片操作
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。
# 即索引0，1，2，正好是3个元素。
# L[-1]取倒数第一个元素

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
# 每5个取一个
print('R[::5] =', R[::5])
