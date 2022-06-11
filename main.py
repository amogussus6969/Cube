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
