def user_choice():
    
    # Variables
    
    # Initial
    choice = 'Wrong'
    acceptable_range = range(0, 11)
    within_range = False
    
    # Two conditions to check
    # Digit or within range is false
    while choice.isdigit() == False or within_range == False:
    
        choice = input('Please a Number (0-10): ')
        
        # Digit Check
        if choice.isdigit()  == False:
            print('Sorry that is not a valid digit!')
            
        # Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
                print('Good Choice!')
            else:
                within_range = False
                print('The Number is not within Specified Range!')
        
    return int(choice)
print(user_choice())