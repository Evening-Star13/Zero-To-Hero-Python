"""Employee Of The Month Check Max Hours"""




def employee_check(work_hours):
    """Employee Of The MOnth"""
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    #Return
    return (employee_of_month, current_max)
