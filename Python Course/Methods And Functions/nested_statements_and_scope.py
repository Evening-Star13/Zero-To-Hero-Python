"""Scope"""
x = 25

def printer():
    """Scope"""
    x = 50
    return x

print(x)
print(printer())

x = 50

def func(x):
    '''Global Function'''
    print(f'X is {x}')
    # Local Reassignment!
    x = 200
    print(f'I just locally changed X to {x}')
print(func(x))
