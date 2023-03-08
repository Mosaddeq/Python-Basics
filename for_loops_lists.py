from_days_to_mins = 24 * 60

u = "mins"

def days_to_units(num_days):
    return f"{num_days} days are {num_days * from_days_to_mins} {u}"


def validate_execute():
    try:
        x= int (elements) # using elements from the for loop instead of u_input because we watn to 
                          # USE EACH ELEMENT
        if x>0:           # therefore u_input replaced by elements
            my_var= days_to_units(x)
            print(my_var)
        elif x==0:
             print("Number cant be zero")
        
    except:
            print("ZZzzzz")
      
u_input=""

while u_input != "exit":
     u_input = input("enter days:")
     print(type(u_input.split(",")))
     print(u_input.split(","))
     for elements in u_input.split(","):  #elements represents each element in list 
          # we are using a list function to conver the input into a list
          validate_execute()
    
    
