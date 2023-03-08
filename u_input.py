from_days_to_mins = 24 * 60

u = "mins"

def days_to_units3(num_days):
    return f"{num_days} days are {num_days * from_days_to_mins} {u}"
   
u_input = input("Enter Day: ")

x = int(u_input)

my_var = days_to_units3(x)
print(my_var)
