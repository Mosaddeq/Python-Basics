calculate = 24 * 60
m = "mins"

def calculate_days_to_mins(num_days):
    return f"{num_days} days are {num_days * calculate}{m}"

u_input= ""

def validate_input():
    try:
        x= int (elements)
        if x>0:
            my_var= calculate_days_to_mins(x)
            print(my_var)
        elif x == 0:
            print("number cant be 0")
        elif x<0:
            print("number cant be negative")
    except:
        print("Enter a valid number")

while u_input != "exit":
    u_input = input("Enter you numbers:\n")

    for elements in set(u_input.split(",")):
        validate_input()
                
