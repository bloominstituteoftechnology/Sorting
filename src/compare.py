############################################################
#   COMPARE
############################################################


def sign(a):

    r = None

    if a < 0:
        r = -1
    elif 0 < a:
        r = +1
    else:
        r = 0

    return r


def difference(a, b):

    return a - b


def compare(a, b):

    return sign(difference(a, b))


def compare_ascending(a, b):

    return +compare(a, b)


def compare_descending(a, b):

    return -compare(a, b)
