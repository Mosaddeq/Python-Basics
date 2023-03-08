from_days_to_mins = 24 * 60

u = "mins"

def days_to_units(num_days):
    return f"{num_days} days are {num_days * from_days_to_mins} {u}"


def validate_execute():
    try:
        x= int (u_input)
        if x>0:
            my_var= days_to_units(x)
            print(my_var)
        elif x==0:
             print("Number cant be zero")
        
    except:
            print("ZZzzzz")
u_input = ""         
 
while u_input != "exit":
    u_input = input("Enter Days: ")

    validate_execute()

    