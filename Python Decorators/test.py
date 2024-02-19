from decorators import dog_decorator

@dog_decorator
def bow_wow_func():
    print('Bow WOW')
    
bow_wow_func()   

help('decorators')
