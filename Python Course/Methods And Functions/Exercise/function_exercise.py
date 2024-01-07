"""Capitalizing Multiple Letters"""
def old_macdonald(name):
    """Module showing functions"""
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

# Check
print(old_macdonald('macdonald'))

# Reversing words in a sentence
def master_yoda(text):
    """Module showing functions"""
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return ' '.join(reverse_word_list)

# Check
print(master_yoda('I am home'))

# Check
print(master_yoda('We are ready'))

# Almost there
def almost_there(n):
    """Numbers within 10 of 100"""
    return(abs(100-n) <= 10) or (abs(200-n) <= 10)
# Check
print(almost_there(104))
# Check
print(almost_there(150))
# Check
print(almost_there(209))

# Find 33
def has_33(nums):
    """See if list of numbers has two 3's beside eachother"""
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#Check
print(has_33([1,3,3]))
#Check
print(has_33([3,1,3]))

# Paper Doll
def paper_doll(text):
    """Add 3 letters for every letter"""
    result = ''
    for char in text:
        result += char*3
    return result

# Check
print(paper_doll('Hello'))
# Check
print(paper_doll('Mississippi'))
# Check
print(paper_doll('Christopher EveningStar'))

# Black Jack
def blackjack(a,b,c):
    """Checking to see if we have blackjack"""
    if sum([a,b,c]) <= 21:
        return sum(([a,b,c]))
    elif 11 in ([a,b,c]) and sum([a,b,c]) <= 31:
        return sum([a,b,c]) -10
    else:
        return 'BUST'

# Check
print(blackjack(9,9,9))
# Check
print(blackjack(5,11,7))
# Check
print(blackjack(9,11,11))

# Summer of 69
def summer_69(arr):
    """Removing all numbers 6 and 9 and finding the sum"""
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

# Check
print(summer_69([1,2,3,5]))
# Check
print(summer_69([12,34,6,7,8,9,12]))

# Spy Game
def spy_game(nums):
    """Find 007"""
    code =[0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# Prime Numbers
def count_primes(num):
    """Checking For Prime Numbers"""
    # Check for 0 or 1 input
    if num < 2:
        return 0
    ##############
    # 2 or greater
    ##############
    # Store our prime numbers
    primes = [2]
    # Counter going up to the input number
    x = 3
    # x is going going through every number up to input number
    while x <= num:
        # Check if x is prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))

count_primes(10)
