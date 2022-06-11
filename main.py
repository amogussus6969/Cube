#Cube a programming language






def condition(arg1, comparasion, arg2, code):
    if comparasion == "==":
        if arg1 == arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == "<<":
        if arg1 << arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == ">>":
        if arg1 >> arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == ">=":
        if arg1 >= arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == "<=":
        if arg1 <= arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == "not==":
        if not arg1 == arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == "not>>":
        if not arg1 >> arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == "not<<":
        if not arg1 << arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == "not<=":
        if not arg1 <= arg2:
            compile(code)
            return True
        else:
            return False
    if comparasion == "not>=":
        if not arg1 >= arg2:
            compile(code)
            return True
        else:
            return False


def add(arg1, arg2):
    return arg1 + arg2

def sub(arg1, arg2):
    return arg1 - arg2

def mul(arg1, arg2):
    return arg1 * arg2

def div(arg1, arg2):
    return arg1 / arg2
