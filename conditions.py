from_days_to_mins = 24 * 60

u = "mins"

""" # This code works

def days_to_units3(num_days):
    return f"{num_days} days are {num_days * from_days_to_mins} {u}"
   
u_input = input("Enter Day: ")

x = int(u_input)

if x<=0:
    print("invalid input")
else:
    my_var = days_to_units3(x)
    print(my_var)
"""

#But a more sophisticated method is this

""""
def days_to_units3(num_days):
    if x>0:
        return f"{num_days} days are {num_days * from_days_to_mins} {u}"
    elif x == 0:
        return "Write something greater than 0"
    else:
        return "Invalid Input"

u_input = input("Enter Day: ")

x = int(u_input)
my_var = days_to_units3(x)
print(my_var)

"""

#Adding some more validation

"""""

def days_to_units3(num_days):
    if x>0:
        return f"{num_days} days are {num_days * from_days_to_mins} {u}"
    elif x == 0:
        return "Write something greater than 0"
u_input = input("Enter Day: ")   

if u_input.isdigit():
    x = int(u_input)
    my_var = days_to_units3(x)
    print(my_var)
else:
    print("Enter a nymber only nothing else")

"""
## Encapsulate the validation

"""""
def days_to_units3(num_days):
    if num_days>0:
        return f"{num_days} days are {num_days * from_days_to_mins} {u}"
    elif num_days == 0:
        return "Write something greater than 0"   

def validate_execute():
    if u_input.isdigit():
        x = int(u_input)
        my_var = days_to_units3(x)
        print(my_var)
    else:
        print("Enter a nymber only nothing else")

u_input = input("Enter Day: ")

validate_execute()

"""
# Cleaner version of the code

def days_to_units3(num_days):
    
    return f"{num_days} days are {num_days * from_days_to_mins} {u}"
       
u_input = input("Enter Day: ")

def validate_execute():
    if u_input.isdigit():
        x = int(u_input)
        if x>0:
            my_var = days_to_units3(x)
            print(my_var)
        elif x==0:
            print("number cant be 0")
            
    else:
        print("Enter a nymber only nothing else")
        

validate_execute()



