



def foo(n):
    if n == 0:
        print('cant stop wont stop')
        return
    print(n)

    foo(n-1)
    foo(n-1)
foo(30)