from_days_to_mins = 24 * 60

u = "mins"

#Basic fucntion
def days_to_units():
    print (f"20 days are {20 * from_days_to_mins} {u}")
    print("this is non parameterized")
days_to_units()

# parameterized
def days_to_units2(num_days):
    print(f"{num_days} days are {num_days * from_days_to_mins} {u}")
    print("this is parameterized")

days_to_units2(35)

#function with return value
def days_to_units3(num_days):
    return f"{num_days} days are {num_days * from_days_to_mins} {u}"
   
my_var = days_to_units3(100)
print(my_var)



