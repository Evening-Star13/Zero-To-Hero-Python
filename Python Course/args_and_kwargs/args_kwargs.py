# Args
# Without *args

def myfunc(a, b, c=0):
    # Returns 5% of the sum a and b
    return sum((a, b)) * 0.05

print (myfunc(40,60))


# With *args

def myfunc2(*args):
    # This will allow an unlimited amount of arguements
    print(args)
    return sum (args) * 0.2

print (myfunc2(12,15,34,67,93,57))


def myfunc3(*args):
    for item in args:
        print(item)
        
print(myfunc3(1,13,45,67,87,31))

# kwargs

def myfunc4(**kwargs):
    if 'fruit' in kwargs:
        print ('My fruit of choice is {}'.format(kwargs['fruit']))
        print ('My veggie of choice is {}'.format(kwargs['veggie']))
    else:
        print ("I didn't find ant fruit here")
        
print(myfunc4(fruit = 'Banana!', veggie = 'Brussel Sprouts!'))

def myfunc5(*args, **kwargs):
    # Can use both *args and **kwargs in combination
    print('I would like {} {}'.format(args[3],kwargs['animal']))
    
myfunc5(10,20,30,1,fruit='orange',food='pizza',animal='dragon')
