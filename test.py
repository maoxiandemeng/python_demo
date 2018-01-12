def add():
    # i = int(input("请输入第一个数字："))
    # j = int(input("请输入第二个数字："))
    i = int(one())
    j = int(two())
    print(type(i))
    print(i + j)


def one():
    i = input("请输入第一个数字：")
    if i.isdigit():
        return i
    else:
        one()


def two():
    i = input("请输入第二个数字：")
    if i.isdigit():
        return i
    else:
        two()


add()
