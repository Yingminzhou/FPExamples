__author__ = 'yingminzhou'

# unfunctional one
a = 0

def increment1():
    global a
    a += 1

# functional one

def increment2(a):
    return a+1
