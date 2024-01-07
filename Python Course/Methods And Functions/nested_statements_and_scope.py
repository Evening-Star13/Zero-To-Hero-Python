"""Scope"""
x = 25

def printer():
    """Scope"""
    x = 50
    return x

print(x)
print(printer())
