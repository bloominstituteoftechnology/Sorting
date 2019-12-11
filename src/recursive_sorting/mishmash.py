# from camelcase import CamelCase


def recurse_factorial(n):
    if n == 0:
        return 1
    return n * recurse_factorial(n - 1)


print(recurse_factorial(100))


# c = CamelCase()
# print(c.hump('hello there world'))
