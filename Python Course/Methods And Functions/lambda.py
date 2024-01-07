"""Lambda Expressions"""
def square(num):
    """Returning Squares Using The Map Function"""
    return num**2

my_nums= [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))

def splicer(mystring):
    """This Will Tell You If The Amount Of Letters In Strings 
    Are Even If Not Will Return The First Letter Only"""
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return mystring[0]
names = ['Andy','Eve','Randy']
print(list(map(splicer,names)))

def check_even(num):
    """Filter Function This Will Function Will Return Even Numbers"""
    return num % 2 == 0
mynums = [1,2,3,4,5,6]
print(list(filter(check_even,mynums)))

for n in filter(check_even,my_nums):
    print(n)

square = lambda num: num ** 2
"""Lambda Function For Square"""
print(square(6))

print(list(map(lambda num: num ** 2, my_nums)))

print(list(filter(lambda num:num%2 == 0,my_nums)))

print(list(map(lambda name:name[0],names)))
print(list(map(lambda name:name[::-1],names)))
