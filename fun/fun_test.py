from fun.abstest import my_abs

print(my_abs(-3))


def test(name, age, city='shanghai'):
    print("name", name)
    print("age", age)
    print("city", city)


test('jing', 23)
test('jing', 23, "haha")


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


move(2, 'A', 'B', 'C')
