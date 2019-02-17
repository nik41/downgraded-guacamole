DEFAULT = object()
key = "none"

def zero(x=DEFAULT):
    if x is DEFAULT:
        return 0
    elif key is "plus":
        return 0 + x
    elif key is "minus":
        return 0 - x
    elif key is "times":
        return 0 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 0 // x
    else:
        return "wrong input"


def one(x=DEFAULT):
    if x is DEFAULT:
        return 1
    elif key is "plus":
        return 1 + x
    elif key is "minus":
        return 1 - x
    elif key is "times":
        return 1 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 1 // x
    else:
        return "wrong input"


def two(x=DEFAULT):
    if x is DEFAULT:
        return 2
    elif key is "plus":
        return 2 + x
    elif key is "minus":
        return 2 - x
    elif key is "times":
        return 2 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 2 // x
    else:
        return "wrong input"


def three(x=DEFAULT):
    if x is DEFAULT:
        return 3
    elif key is "plus":
        return 3 + x
    elif key is "minus":
        return 3 - x
    elif key is "times":
        return 3 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 3 // x
    else:
        return "wrong input"

def four(x=DEFAULT):
    if x is DEFAULT:
        return 4
    elif key is "plus":
        return 4 + x
    elif key is "minus":
        return 4 - x
    elif key is "times":
        return 4 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 4 // x
    else:
        return "wrong input"

def five(x=DEFAULT):
    if x is DEFAULT:
        return 5
    elif key is "plus":
        return 5 + x
    elif key is "minus":
        return 5 - x
    elif key is "times":
        return 5 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 5 // x
    else:
        return "wrong input"

def six(x=DEFAULT):
    if x is DEFAULT:
        return 6
    elif key is "plus":
        return 6 + x
    elif key is "minus":
        return 6 - x
    elif key is "times":
        return 6 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 6 // x
    else:
        return "wrong input"

def seven(x=DEFAULT):
    if x is DEFAULT:
        return 7
    elif key is "plus":
        return 7 + x
    elif key is "minus":
        return 7 - x
    elif key is "times":
        return 7 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 7 // x
    else:
        return "wrong input"

def eight(x=DEFAULT):
    if x is DEFAULT:
        return 8
    elif key is "plus":
        return 8 + x
    elif key is "minus":
        return 8 - x
    elif key is "times":
        return 8 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 8 // x
    else:
        return "wrong input"

def nine(x=DEFAULT):
    if x is DEFAULT:
        return 9
    elif key is "plus":
        return 9 + x
    elif key is "minus":
        return 9- x
    elif key is "times":
        return 9 * x
    elif key is "divide":
        if x is 0:
            return "the divisor can not be zero"
        else:
            return 9 // x
    else:
        return "wrong input"

def plus(j):
    global key
    key = "plus"
    return j

def minus(j):
    global key
    key = "minus"
    return j

def times(j):
    global key
    key = "times"
    return j

def division(j):
    global key
    key = "divide"
    return j

print(two(plus(six())))
print(five(minus(two())))
print(five(minus(nine())))
print(six(times(zero())))
print(six(times(two())))
print(five(division(zero())))
print(five(division(two())))