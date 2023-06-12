work_hours = [("Billy", 200), ("Abby", 300), ("Karry", 400)]
def employee_check (work_hours):


    emp_name=''
    max_hours =0
    for employee_name,hours in work_hours:
        if hours>max_hours:
            max_hours = hours
            emp_name = employee_name

        else:
            pass

    return(emp_name,max_hours)
print(employee_check(work_hours))
print('hi')
for num in range(1,101):
    if num%3 ==0:
        print("Fizz")
    elif num%5 ==0:
        print("Buzz")
    elif num%3 ==0 and num%5 ==0:
        print("FizzBuzz")
    else:
        print(num)