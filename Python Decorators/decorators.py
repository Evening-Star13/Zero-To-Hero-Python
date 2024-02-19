"""_summary_"""
# def new_decorator(original_function):       
#     def wrap_func():
        
#         original_function()
        
#     return wrap_func
    
  
# @new_decorator
# def func_needs_decorator():
    
#     print('Hi There!!')

# func_needs_decorator()


def dog_decorator(bark_function):
    def woof_func():
        bark_function()
    return woof_func

@dog_decorator
def bow_wow_func():
    
    # print('WWOOF WOOF WOOF!!!')
    pass
bow_wow_func()