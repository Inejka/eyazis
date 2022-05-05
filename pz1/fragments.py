def print_show():
    print("Hello world")


def serial_operators():
    a = 0
    a += 5
    b = 5
    a = b + b
    print(a)


def if_show():
    a = 3
    b = 5
    if b > a:
        print("bb")


def if_else_show():
    a = 3
    b = 5
    if a > b:
        print(a)
    else:
        print(b)


def while_show():
    a = 13241234
    while a > 1:
        print(a)
        a /= 10


def for_show():
    for i in range(10):
        print(i)


def type_show():
    print(type("adf"))
    print(type(112))
    print(type(1.1))


def for_show():
    for i in range(2):
        print("Hello World" + str(i))


def arithmetic_progression():
    n = 73
    for i in range(0, n, 2):
        print(i)


def geometric_progression():
    limit = 125251
    i = 1
    while i < limit:
        i *= 2
        print(i)


def factorial(number):
    if (number == 1): return 1
    return number * factorial(number - 1)


def starts_with_24(string):
    return "24".startswith(string)


def assert_equals(expected, actual):
    return expected == actual


def decrement(number):
    return number - 1


if __name__ == "__main__":
    print_show()
    serial_operators()
    if_show()
    if_else_show()
    while_show()
    for_show()
    type_show()
    for_show()
    arithmetic_progression()
    geometric_progression()
    factorial(5)
    starts_with_24("24asfhashfasughASY")
    assert_equals(1, 1)
    decrement(2)
