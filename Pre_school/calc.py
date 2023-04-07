def power(x, y):
    return x**y


def cubic(x):
    return power(x, 3)


def divide(x, y):
    return [x // y, x % y, x / y]


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


export = {
    "power": power,
    "cubic": cubic,
    "divide": divide,
    "factorial": factorial,
}
